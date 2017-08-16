import importlib
from aule import config


class Locator(object):
    """
    A Locator class.

    Imports and returns parsers tools.
    """

    @classmethod
    def parser(cls, vendor: str):
        parser_file = config.GENERATED_MODULE_LOCATION + "." + vendor + "Parser"

        try:
            parser_module = importlib.import_module(parser_file)
        except Exception as err:
            print(err)
            raise ImportError("Unknown vendor type during parser import")

        try:
            parser = getattr(parser_module, vendor + "Parser")(None)
        except AttributeError as err:
            print(err)
            raise ImportError("Parser attribute does not exist")

        return parser

    @classmethod
    def lexer(cls, vendor: str):
        lexer_file = config.GENERATED_MODULE_LOCATION + "." + vendor + "Lexer"

        try:
            lexer_module = importlib.import_module(lexer_file)
        except Exception as err:
            print(err)
            raise ImportError("Unknown vendor type during lexer import")

        try:
            lexer = getattr(lexer_module, vendor + "Lexer")(None)
        except AttributeError as err:
            print(err)
            raise ImportError("Lexer attribute does not exist")

        return lexer

    @classmethod
    def visitor(cls, vendor: str):
        visitor_file = config.VISITOR_MODULE_LOCATION + "." + vendor + "ASTVisitor"

        try:
            visitor_module = importlib.import_module(visitor_file)
        except Exception as err:
            print(err)
            raise ImportError("Unknown vendor type during visitor import")

        try:
            visitor = getattr(visitor_module, vendor + "ASTVisitor")()
        except AttributeError as err:
            print(err)
            raise ImportError(vendor + "ASTVisitor class does not exist")

        return visitor

    @classmethod
    def decoder(cls, vendor: str):
        decoder_file = config.GENERATED_MODULE_LOCATION + "." + vendor + "ASTDecoder"

        try:
            decoder_module = importlib.import_module(decoder_file)
        except Exception as err:
            print(err)
            raise ImportError("Unknown vendor type during AST decoder import")

        try:
            decoder = getattr(decoder_module, "ASTFactory")()
        except AttributeError as err:
            print(err)
            raise ImportError("ASTFactory class does not exist")

        return decoder
