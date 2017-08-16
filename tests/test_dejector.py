import shutil
import os
from .context import DejectorFactory, OUTPUT_PATH, OUTPUT_GRAMMARS_PATH


LOOSE_QUERIES_FILE = "./tests/resources/loose_dejector_queries.txt"
STRICT_QUERIES_FILE = "./tests/resources/strict_dejector_queries.txt"

def remove_folder(path):
    if os.path.exists(path):
         shutil.rmtree(path)


def test_mysql_based_dejector():
    """ Test dejector for base mysql-grammar """
    modes = ["loose", "strict"]
    name = "testMySql"
    for mode in modes:
        dejector = DejectorFactory.create("mysql", name, mode)

        parser = dejector.get_from_file(LOOSE_QUERIES_FILE)
        assert os.path.exists(OUTPUT_GRAMMARS_PATH + "/" + name)
        assert parser.check_syntax("SELECT 4")
        
        DejectorFactory.dispose(dejector)
        assert not os.path.exists(OUTPUT_GRAMMARS_PATH + "/" + name)
        assert not os.path.exists(OUTPUT_PATH + "/" + name + "Lexer.py")

        json = []
        with open(LOOSE_QUERIES_FILE) as f:
            for line in f:
                json.append(str(line))

        parser = dejector.get_from_json(json)
        assert os.path.exists(OUTPUT_GRAMMARS_PATH + "/")
        assert parser.check_syntax("SELECT 4")
        
        DejectorFactory.dispose(dejector)
        assert not os.path.exists(OUTPUT_GRAMMARS_PATH + "/" + name)
        assert not os.path.exists(OUTPUT_PATH + "/" + name + "Lexer.py")


def test_tsql_based_dejector():
    """ Test dejector for base tsql-grammar """
    name = "testTsql"
    dejector = DejectorFactory.create("tsql", name, "loose")

    parser = dejector.get_from_file(LOOSE_QUERIES_FILE)
    assert os.path.exists(OUTPUT_GRAMMARS_PATH + "/" + name)
    assert parser.check_syntax("SELECT 4")

    DejectorFactory.dispose(dejector)
    assert not os.path.exists(OUTPUT_GRAMMARS_PATH + "/" + name)
    assert not os.path.exists(OUTPUT_PATH + "/" + name + "Lexer.py")

    json = []
    with open(LOOSE_QUERIES_FILE) as f:
        for line in f:
            json.append(str(line))

    parser = dejector.get_from_json(json)
    assert os.path.exists(OUTPUT_GRAMMARS_PATH + "/" + name)
    assert parser.check_syntax("SELECT 4")
    
    DejectorFactory.dispose(dejector)
    assert not os.path.exists(OUTPUT_GRAMMARS_PATH + "/" + name)
    assert not os.path.exists(OUTPUT_PATH + "/" + name + "Lexer.py")


def test_loose_dejector_from_file():
    name = "looseSQL"
    dejector = DejectorFactory.create("mysql", name,  "loose")

    parser = dejector.get_from_file(LOOSE_QUERIES_FILE)
    assert os.path.exists(OUTPUT_GRAMMARS_PATH + "/" + name)
    assert parser.check_syntax("SELECT 4")
    
    DejectorFactory.dispose(dejector)
    assert not os.path.exists(OUTPUT_GRAMMARS_PATH + "/" + name)
    assert not os.path.exists(OUTPUT_PATH + "/" + name + "Lexer.py")


def test_strict_dejector_from_json():
    name = "strictSQL"
    dejector = DejectorFactory.create("mysql", name, "strict")
    json = []
    with open(STRICT_QUERIES_FILE) as f:
        for line in f:
            json.append(str(line))

    parser = dejector.get_from_json(json)
    assert os.path.exists(OUTPUT_GRAMMARS_PATH + "/" + name)
    assert parser.check_syntax("SELECT * from `aaaaaa`")
    assert parser.check_syntax("SELECT * FROM passbook LIMIT 10")
    assert not parser.check_syntax("SELECT 1 union SELECT 2")

    DejectorFactory.dispose(dejector)
    assert not os.path.exists(OUTPUT_GRAMMARS_PATH + "/" + name)
    assert not os.path.exists(OUTPUT_PATH + "/" + name + "Lexer.py")
