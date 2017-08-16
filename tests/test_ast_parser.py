from .context import ASTParserFactory, ASTParser
from .context import ust
import json


def test_dumps():
    node = ust.TypeReference(ust.SimpleType.STRING, is_pointer=False, is_sequence=False)
    node_str = ASTParser.dumps(node)
    json_ = json.loads(node_str)
    assert json_.get("is_pointer") is False
    assert json_.get("is_sequence") is False
    assert json_.get("type") == "SimpleType.STRING"


def test_parse():
    ast_parser = ASTParserFactory.create("idl")
    ast = ast_parser.parse("interface foo {}")
    assert ast is not None

