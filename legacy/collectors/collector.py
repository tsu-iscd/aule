from aule.visitors.tree import ASTWalker

from .sqlAccessVectors import SQLAccessVectorsListener
from .sqlProfiler import SQLProfileListener


class SQLCollector(object):
    """
    A class implements different collectors that retrieve data from SQL queries.
    """

    @staticmethod
    def get_profile(ast):
        listener = SQLProfileListener()
        if ast:
            walker = ASTWalker(listener)
            walker.walk(ast)
        return listener.get_results()

    @staticmethod
    def get_access_vectors(ast):
        listener = SQLAccessVectorsListener()
        if ast:
            walker = ASTWalker(listener)
            walker.walk(ast)
        return listener.get_results()
