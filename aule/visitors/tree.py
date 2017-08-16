class ASTVisitor(object):

    def visit(self, tree):
        return tree.accept(self)


class ASTWalker(object):
    def __init__(self, listener) -> None:
        if listener is None:
            raise ValueError("Listener must be created")
        self.listener = listener

    def walk(self, node) -> None:
        # Check end of recursion.
        if not hasattr(node, "__dict__"):
            return
        # Enter in a current node.
        node.enterNode(self.listener)
        # Get all children and its names.
        children = node.__dict__
        children_names = list(children.keys())
        # Walk through the Tree.
        for name in children_names:
            if name != "type":
                if isinstance(children[name], list):
                    for next_node in children[name]:
                        self.walk(next_node)
                else:
                    self.walk(children[name])

        # Exit from the current node.
        node.exitNode(self.listener)
