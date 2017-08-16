"""
Parser is a facade for working with ANTLR-based parsers.
"""

# General
import json
from enum import Enum

# ANTLR
from antlr4 import CommonTokenStream, BailErrorStrategy, InputStream
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Trees import Trees
from antlr4.error.Errors import *
from antlr4.error.ErrorStrategy import DefaultErrorStrategy
from antlr4.atn.PredictionMode import PredictionMode
from antlr4.Utils import escapeWhitespace
from antlr4.error.Errors import ParseCancellationException

# Internal
from aule.locator import Locator

# Types
from typing import Set, List


class TreePrinter(Trees):
    """
    It is used to print a parse tree.
    """
    @classmethod
    def toDictionaryTree(cls, t, ruleNames=None, recog=None):
        """ Converts  a parse tree to a dictionary. """
        tree = {"name": "", "children": []}
        if recog is not None:
            ruleNames = recog.ruleNames
        s = escapeWhitespace(cls.getNodeText(t, ruleNames), False)
        tree["name"] = s
        if t.getChildCount() == 0:
            return tree
        for i in range(0, t.getChildCount()):
            tree["children"].append(cls.toDictionaryTree(t.getChild(i), ruleNames))
        return tree


class Vendors(Enum):
    """
    Supported vendors in Parser.
    """
    mysql = 1
    tsql = 2
    idl = 3
    alfa = 4
    lua = 5
    sqllexer = 6
    kotlin = 7


class ListErrorListener(ErrorListener):
    """
    Implements custom error listener for getting errors.
    """
    def __init__(self) -> None:
        super(ListErrorListener, self).__init__()
        self.errors: Set[str] = set()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e) -> None:
        line = "line {0} : {1} {2}".format(line, column, msg)
        self.errors.add(line)


    @property
    def get_errors(self) -> List[str]:
        return list(self.errors)


class Parser:
    """
    A Parser for creating concrete syntax trees (CST).
    """

    def __init__(self, lexer, parser, vendor: str) -> None:
        self.vendor = vendor
        self.lexer = lexer
        self.parser = parser

    def _tokenize(self, text: str) -> CommonTokenStream:
        """ Internal ANTLR4 tokenizer. """
        self.lexer.reset()
        char_stream = InputStream(text)
        self.lexer.inputStream = char_stream
        token_stream = CommonTokenStream(self.lexer)
        return token_stream

    def _preprocess(self, text: str) -> str:
        return text

    def set_validating(self) -> None:
        """
        Specifies that the parser will validate text.
        In this mode you can use 'validate' method only.
        """
        self.parser._listeners = [ListErrorListener()]
        self.parser._errHandler = DefaultErrorStrategy()

    def unset_validating(self) -> None:
        """
        Specifies that the parser will not validate text.
        You can not use 'validate' methd in this mode.
        """
        self.parser.removeErrorListeners()
        self.parser._errHandler = BailErrorStrategy()

    def get_errors(self):
        for listener in self.parser._listeners:
            if isinstance(listener, ListErrorListener):
                return listener.get_errors

    def get_tokens(self, text: str):
        """ Call tokenizer and emit tokens. """
        token_stream = self._tokenize(text)
        token_stream.fill()
        tokens = []
        for token in token_stream.tokens:
            if token.text != "<EOF>":
                tokens.append({
                    "type": self.lexer.symbolicNames[token.type],
                    "text": token.text,
                    "start": token.start,
                    "stop": token.stop,
                    "index": token.tokenIndex,
                    "channel": token.channel
                })
        return tokens

    def get_lexems(self, text: str) -> List[str]:
        """ Call tokenizer and emit lexems. """
        token_stream = self._tokenize(text)
        token_stream.fill()
        lexems = []
        for token in token_stream.tokens:
            if token.text != "<EOF>":
                lexems.append(token.text)
        return lexems

    def validate(self, text: str) -> None:
        """
        Validates syntax only.
        It uses DefaultErrorStrategy, so parser should be in 'validating' mode.
        Syntax errors are reported to console.
        """
        self.parser.reset()
        text = self._preprocess(text)
        token_stream = self._tokenize(text)
        self.parser.setInputStream(token_stream)
        self.parser.root()

    def check_syntax(self, text: str) -> bool:
        """
        Silently checks if syntax of SQL query is valid or not.
        It uses BailErrorStrategy, so parser should be in 'non_validating' mode.
        Syntax errors are not being reported or logged.
        """
        if self.parse(text):
            return True
        return False

    def parse(self, text: str) -> ParserRuleContext:
        """
        Parses input text into CST.

        We use two-stage parsing based on SLL-mode.
        Source: https://github.com/antlr/antlr4/blob/master/doc/faq/general.md#why-is-my-expression-parser-slow
        """
        self.parser.reset()
        text = self._preprocess(text)
        token_stream = self._tokenize(text)
        self.parser.setInputStream(token_stream)

        # Initial SLL(*)-parsing
        self.parser._interp.predictionMode = PredictionMode.SLL
        try:
            tree = self.parser.root()
        except ParseCancellationException:
            pass
        else:
            return tree

        # Default LL(*)-parsing
        token_stream.reset()
        self.parser.reset()
        self.parser._interp.predictionMode = PredictionMode.LL

        try:
            tree = self.parser.root()
        except ParseCancellationException:
            tree = None
        return tree

    def print_string_tree(self, text: str) -> None:
        """ Debug function to print parse tree in LISP form. """
        tree = self.parse(text)
        if tree:
            print(Trees.toStringTree(tree, None, self.parser))
        else:
            print("Error: AST is None")

    def get_dictionary_tree(self, text: str):
        """ Get dictionary parse tree. """
        tree = self.parse(text)
        if tree:
            return TreePrinter.toDictionaryTree(tree, None, self.parser)
        else:
            return None

    def print_json_tree(self, text: str) -> None:
        """ Debug function to print tree in JSON form. """
        dictionary_tree = self.get_dictionary_tree(text)
        if dictionary_tree:
            print(json.dumps(dictionary_tree, indent=2))
        else:
            print("Error: AST is None")


class TsqlParser(Parser):
    """
    TSQL Parser.
    """
    def __init__(self, lexer, parser) -> None:
        super().__init__(lexer, parser, "tsql")


class MysqlParser(Parser):
    """
    MySQL Parser.
    """
    def __init__(self, lexer, parser) -> None:
        super().__init__(lexer, parser, "mysql")

    def _preprocess(self, text: str) -> str:
        """ 
        Preprocess text with /*! */ comments and return actual query without them.
        Example: "select 1 /*! union select 2 */" -> "select 1 union select 2".
        """
        token_stream = self._tokenize(text)
        spec_mysql_comment_stream = CommonTokenStream(self.lexer, self.lexer.SPEC_MYSQL_COMMENT)
        number_of_tokens = spec_mysql_comment_stream.getNumberOfOnChannelTokens()
        if number_of_tokens > 0:
            self.lexer.reset()
            token_stream.fill()
            text = ""
            for token in token_stream.tokens:
                if token.channel == self.lexer.SPEC_MYSQL_COMMENT:
                    text += " " + token.text[3:-2]
                elif token.text != "<EOF>":
                    text += " " + token.text
        return text


class ParserFactory:
    """
    Produces parsers for creating CST.
    """
    @staticmethod
    def create(vendor: str, is_validating: bool = False) -> Parser:
        """
        Creates a Parser with the specified configuration.
        :param vendor
        :type vendor: str
        :param is_validating: indicates whether or not the factory is configured to produce CST parsers
            which validate input and output errors during parse.
        :type is_validating: bool
        :return: parser
        :rtype: Parser
        """
        lexer = Locator.lexer(vendor)
        parser = Locator.parser(vendor)

        if not is_validating:
            parser.removeErrorListeners()
            parser._errHandler = BailErrorStrategy()
        else:
            parser._listeners = [ListErrorListener()]
            parser._errHandler = DefaultErrorStrategy()

        if vendor == "mysql":
            return MysqlParser(lexer, parser)
        elif vendor == "tsql":
            return TsqlParser(lexer, parser)
        else:
            return Parser(lexer, parser, vendor)
