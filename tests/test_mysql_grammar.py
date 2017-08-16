import os
import tests.utils as utils
from .context import ParserFactory
from .context import GRAMMARS_PATH


def test_syntax():
    """ mysql grammar full tests. """
    path = GRAMMARS_PATH + "/mysql/examples/"
    parser = ParserFactory.create("mysql")
    files = os.listdir(path)
    for file in files:
        fname = path + file
        # check only files
        if os.path.isfile(fname):
            tests = utils.get_tests(fname, "#begin", "#end")
            for query in tests:
                try:
                    test = parser.check_syntax(query)
                except Exception as err:
                    print(err)
                    assert False
                if not test:
                    print("File: " + file)
                    print("SQL Query: \n" + query)
                    assert False
