from typing import Iterable, List, Optional

from ..classnodes  import *
from ..simplenodes  import *
from .lca import LCA


class ClassesReference(object):
    """
    ClassesReference provides some useful helpers to work with UST classes
    inheritance.
    """
    def __init__(self,
                 classes: List[ClassDeclaration]) -> None:
        self.classes = {
            cls.name: cls for cls in classes
        }
        # N.B.: If inheritance of the classes would be changed - recall
        # `self.lca.compute_L_table()` and `self.lca.compute_P_table()`
        # by hand!
        self.lca = LCA(self.classes)

    def get_parents(self,
                    cls: ClassDeclaration) -> Iterable[ClassDeclaration]:
        """ Returns @cls parents from @other_classes """
        if len(cls.parents) == 0:
            return
        for parent_id in cls.parents:
            parent = self.classes.get(parent_id, None)
            if parent is not None:
                yield parent

    def get_constructor_args(self,
                             cls_id: Identifier) -> List[Argument]:
        """ Returns list of constructor arguments for the given class """
        cls = self.classes.get(cls_id, None)
        return cls.constructor.arguments if cls is not None else []

    def get_common_ancestor(self,
                            *cls_id: Identifier) -> Optional[Identifier]:
        """ Returns the nearest common ancestor of classes or None if there is none """
        # If we don't know a class - we have no chances to find a parent.
        for id_ in cls_id:
            if id_ not in self.classes:
                return None
        return self.lca.get_common_ancestor(*cls_id)

    def is_inherited_from(self,
                          cls: ClassDeclaration,
                          possible_parent: Identifier,
                          recursive=True) -> bool:
        """
        Checks whether the @cls is inherited from @ancient.

        With @recursive is False performs direct inheritance check, otherwise
        will try to find it out recursively
        """
        if possible_parent in cls.parents:
            return True
        if recursive:
            for parent in self.get_parents(cls):
                if self.is_inherited_from(parent, possible_parent):
                    return True
        return False

    def is_parent_for_somebody(self,
                               cls: ClassDeclaration) -> bool:
        """ Checks whether exists a class inherited from @cls """
        return any(
            cls.name in c.parents for c in self.classes.values()
        )

    def overrides(self,
                  member: Union[FieldDeclaration, MethodDeclaration],
                  cls: ClassDeclaration) -> Union[FieldDeclaration, MethodDeclaration, None]:
        """
        Checks whether the given class member overrides some of parents' one.
        Formally it's some kind of breadth-first search cos we wanted to
        find the nearest override.

        Returns the overridden member of parent's class if any found.
        N.B. We do not support multiple overrides to the same level
        """
        queue = [self.classes[x] for x in cls.parents]
        while len(queue) != 0:
            c = queue.pop(0)
            # Check field override
            field = next((field for field in c.fields if member.name == field.name), None)
            if field is not None:
                return field
            # Check method override (N.B. check only by name - for full function
            # signature check - refactor)
            method = next((method for method in c.methods if member.name == method.name), None)
            if method is not None:
                return method
            # Enqueue class parents
            queue.extend(self.classes[x] for x in c.parents)
        return None

    def __getitem__(self, item: Identifier):
        return self.classes[item]
