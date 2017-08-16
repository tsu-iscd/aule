import os
import tests.utils as utils
from .context import ParserFactory
from .context import GRAMMARS_PATH


def test_kotlin_syntax():
    """ Kotlin grammar smoke tests. """
    path = GRAMMARS_PATH + "/kotlin/examples/"
    parser = ParserFactory.create("kotlin")
    files = os.listdir(path)
    for file in files:
        fname = path + file
        tests = utils.get_tests(fname, "#begin", "#end")
        for text in tests:
            test = parser.check_syntax(text)
            if not test:
                print("File: " + file)
                print("Text: \n" + text)
                assert False
