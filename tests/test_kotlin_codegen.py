import os
from .context import GeneratorFactory, Language
from .context import ParserFactory, ASTParserFactory
from .context import IDL_PATH
from nose.tools import nottest


SQL_IDl_FILE = os.path.join(IDL_PATH, "sql.idl")

@nottest
def test_kotlin_sql_ast_codegen():
    kotlin_generator = GeneratorFactory.create(language=Language.kotlin)
    kotlin_parser = ParserFactory.create("kotlin")
    idl_ast_parser = ASTParserFactory.create("idl")

    with open(SQL_IDl_FILE, "r") as f:
        idl_text = f.read()

    ust = idl_ast_parser.parse(idl_text)
    kotlin_code = kotlin_generator.use_tree(ust).generate()
    assert kotlin_parser.parse(kotlin_code)

