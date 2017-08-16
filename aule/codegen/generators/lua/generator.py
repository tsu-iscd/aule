from copy import deepcopy
from . import alfa2lua


class Generator(object):
    """ Very straightforward wrapper for the legacy alfa->lua generator. """
    def __init__(self) -> None:
        self.legacy_gen = alfa2lua.LegacyGenerator()
        self.tree = None

    def use_tree(self, tree, mutableAST: bool = False):
        self.tree = tree if mutableAST else deepcopy(tree)
        return self

    def generate(self):
        self.legacy_gen.reset()
        if self.tree is None:
            raise ValueError("Input AlfaScript AST in None")
        return self.legacy_gen.generate(self.tree)
