from typing import Optional, Dict
from ..classnodes import *


class LCA(object):
    """ LCA find lowest (nearest) common ancestor
        NB https://www.topcoder.com/community/data-science/data-science-tutorials/range-minimum-query-and-lowest-common-ancestor
    """
    def __init__(self, classes) -> None:
        self.classes = classes
        # Compute P and L tables if necessary
        ## Parents table
        self.P: Dict[Identifier, List[Identifier]] = None
        self.compute_P_table()
        ## Levels table
        self.L: Dict[Identifier, int] = {}
        self.compute_L_table()
        # L and P will compute once only after calling `get_common_ancestor`

    def get_common_ancestor(self,
                            *cls_id: Identifier) -> Optional[Identifier]:
        """ Returns the nearest common ancestor of classes or None if there is none """
        if len(cls_id) == 0:
            return None
        # Find the minimum level of cls_id's
        L_min = min({ c: self.L.get(c, -1) for c in cls_id }.values())
        if L_min == -1:
            # cls_id has id not from self.classes
            return None
        # Part of _L with IDs only from cls_id
        IDs = set()
        # Find the ancestor of node `c` situated on the L_min level
        for c in cls_id:
            if self.L[c] > L_min:
                for i in range(log(self.L[c]), -1, -1):
                    if ( self.L[c] - (1<<i) ) >= L_min:
                        c = self.P[c][i]
            IDs.add(c)
        if len(IDs) == 1:
            # In this case some of cls_id is LCA
            return IDs.pop()
        # cls_id has several roots
        if L_min == 0:
            return None
        # Compute LCA(p, q) using the values in P
        for i in range(log(L_min), -1, -1):
            next_set = {self.P[c][i] for c in IDs}
            if ( -1 not in next_set ) and len(next_set)==len(IDs):
                IDs = next_set
        return self.get_parent(IDs.pop())


    def get_parent(self, cls_id: Identifier) -> Identifier:
        """ Returns only first parent or None if there is none """
        return self.classes[cls_id].parents[0] if self.classes[cls_id].parents else None

    def compute_P_table(self):
        """ Compute a table P for dynamic programming method (see link above) """
        # Step 1 and step 2
        N = len(self.classes)
        P = { c: [self.get_parent(c)] + \
                 [None]*(N.bit_length()-1) \
                 for c in self.classes }
        # Step 3
        for j in range(1, N.bit_length()):
            for c in self.classes:
                if P[c][j-1]:
                    P[c][j] = P[P[c][j-1]][j-1]
        self.P = P

    def compute_L_table(self):
        """ L[i] is the level of node `i` in the tree"""
        for cls_id in self.classes:
            self.set_level(cls_id)

    def set_level(self, cls_id: Identifier) -> int:
        """ If lvl is not None then
                L[cls_id] := lvl
            elif cls_id has parent then
                L[cls_id] := L[cls_id.parent] + 1
            else
                L[cls_id] := 0
            Returns the set level
        """
        if self.L.get(cls_id, None):
            return self.L.get(cls_id)
        parent = self.get_parent(cls_id)
        if parent:
            self.L[cls_id] = self.set_level(parent) + 1
        else:
            self.L[cls_id] = 0
        return self.L[cls_id]

def log(N: int) -> Optional[int]:
    return N.bit_length() - 1 if N != 0 else None