import tests.utils as utils
from .context import GeneratorFactory, Language, ASTParserFactory
from .context import ParserFactory


LUA_POLICIES_FILE = "./tests/resources/alfa_policies.txt"


def test_lua_codegen():
    luagen = GeneratorFactory.create(language=Language.lua)
    parser = ParserFactory.create("lua")
    ast_parser = ASTParserFactory.create("alfa")
    tests = utils.get_tests(LUA_POLICIES_FILE, "#begin", "#end")
    for alfacode in tests:
        node = ast_parser.parse(alfacode)
        assert node
        luagen.use_tree(node)
        luacode = luagen.generate()
        assert parser.check_syntax(luacode)
