import jsonpickle

from antlr4 import ParseTreeVisitor

# Internal
from aule.locator import Locator
from aule.parser import ParserFactory, Parser


class ASTParser:
    """
    A Parser for creating abstract syntax trees (AST).
    """
    vendor: str
    parser: Parser

    def __init__(self, parser: Parser, visitor: ParseTreeVisitor) -> None:
        """
        :param visitor: visitor for creating AST
        :type visitor: ParseTreeVisitor
        :param parser: parser for creating CST
        :type parser: Parser
        """
        self.visitor = visitor
        self.parser = parser

    def parse(self, text: str):
        """
        Parses input text into AST.

        AST is created by the following way:
        1. Parser creates CST.
        2. Appropriate visitor walks this CST.

        :param text: string we are going to parse
        :type  text: str
        :return Resulting AST
        """
        cst = self.parser.parse(text)
        if cst is None:
            return None

        node = self.visitor.visit(cst)
        return node

    @staticmethod
    def dumps(node) -> str:
        """
        Dumps given AST to the json string.
        :rtype: str
        """
        return jsonpickle.encode(node, unpicklable=False)

    @staticmethod
    def loads(vendor: str, json_str: str):
        """
        Parses given JSON string and translates it into the AST.
        :param vendor: name that will be used to find appropriate decoder
        :type vendor: str
        :param json_str: IDL grammar tree in JSON format
        :type  json_str: str
        :return Resulting AST
        """
        decoder = Locator.decoder(vendor)
        return decoder.from_json(json_str)


class ASTParserFactory:
    """
    Produces parsers for creating AST.
    """

    @staticmethod
    def create(vendor: str, is_validating: bool = False) -> ASTParser:
        """
        Creates an ASTParser with the specified configuration.
        :param vendor
        :type vendor: str
        :param is_validating: indicates whether or not the factory is configured to produce AST parsers
            which validate input and output errors during CST parse.
        :type is_validating: bool
        :return: parser
        :rtype: ASTParser
        """
        parser = ParserFactory.create(vendor, is_validating)
        visitor = Locator.visitor(vendor)
        return ASTParser(parser, visitor)
