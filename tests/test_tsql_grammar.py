import tests.utils as utils
import os
from .context import ParserFactory
from .context import GRAMMARS_PATH


def test_syntax():
    """ tsql grammar smoke tests. """
    path = GRAMMARS_PATH + "/tsql/examples/"
    parser = ParserFactory.create("tsql")
    files = os.listdir(path)
    for file in files:
        fname = path + file
        tests = utils.get_tests(fname, "#begin", "#end")
        for query in tests:
            test = parser.check_syntax(query)
            if not test:
                print("File: " + file)
                print("SQL Query: \n" + query)
                assert False
