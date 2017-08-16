# Stubs for antlr4.tree.ParseTreeMatch (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class ParseTreeMatch:
    tree = ...  # type: Any
    pattern = ...  # type: Any
    labels = ...  # type: Any
    mismatchedNode = ...  # type: Any
    def __init__(self, tree, pattern, labels, mismatchedNode) -> None: ...
    def get(self, label): ...
    def getAll(self, label): ...
    def succeeded(self): ...
