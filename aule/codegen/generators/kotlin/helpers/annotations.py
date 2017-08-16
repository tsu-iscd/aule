from typing import List

def annotate(node: object, annotations: List[str]):
    """ Adds property `annotations` to the node with list of strings """
    setattr(node, "annotations", annotations)