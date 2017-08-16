#!/usr/bin/env/python
"""
This module contains a Dejector.
"""
# General
import os
import shutil
from collections import OrderedDict
from typing import Dict, List

# Internal
from aule.parser import Parser, ParserFactory, Vendors
from aule import config


def is_terminal(node) -> bool:
    """Check if a node is terminal (leaf)."""
    if len(node["children"]) == 0:
        return True
    return False


class Dejector(object):
    """
    A Dejector class.

    Implements Dejector protection mechanism. 
    """

    def __init__(self, vendor: str, name: str, parser: Parser, mode: str) -> None:
        self.vendor = vendor
        self.name = name
        self.parser = parser
        self.mode = mode
        self.merge_func = None
        self.ruleNameDict: Dict = {}
        self.cur_level = 0  # start from empty level where nothing exists (root`s level - it is 1)
        self.merge_level = 1  # start level where we can merge trees
        self.is_unique_nodes = True
        if mode == "strict":
            self.merge_func = self._merge_extend
        elif mode == "loose":
            self.merge_func = self._merge_full
            self.is_unique_nodes = False
        else:
            raise ValueError("Unknown mode {}".format(mode))

    def _generate_parser_grammar(self, ucst) -> str:
        """ Generate parser code based on UCST dictionary. """
        grammar = "\n"
        dict_grammar = OrderedDict()  # type: OrderedDict
        self._generate_grammar_dict(ucst, dict_grammar)
        for rule in dict_grammar:
            grammar = grammar + rule + ":\n"
            is_first_alt = True  # TODO: make better
            for alt_subrule in dict_grammar[rule]:
                if is_first_alt:
                    is_first_alt = False
                    grammar = grammar + "   "
                else:
                    grammar = grammar + "\n   | "
                for lexem in alt_subrule:
                    grammar = grammar + lexem + " "
            grammar = grammar + "\n    ;\n\n"
        return grammar

    def _generate_grammar_dict(self, ucst: Dict, dict_grammar: OrderedDict):
        """ Generate grammar dictionary from UCST. 

        dict_grammar has special form, this is dictionary of list of lists:
        {"rule_name":[alt_subrule, alt_subrule], ... } where alt_subrule = [elem_rule, elem_rule, ...]

        """

        def write_rule_in_dict(dict_grammar: OrderedDict, ucst, is_first):
            """
            Fill rule for tree base on children of tree and saved information in dict_grammar

            forming list of alternatives for rule which according to argument of function "tree"
            dict_grammar[tree["name"]] is key dictionary consist of list alternatives, each alternatives
            are list of ust "node["name"]" is_first mean that value on key dict_grammar[tree["name"]]
            in dictionary is empty (we get it in first time)
            """

            def check_presented_branch(list_of_alts, current_branch_alt):
                """
                check_presented_branch.

                return True if current_branch_alt presents in list_of_alts
                list_of_alts list of ordered by elements alternatives
                current_branch_alt - ordered list of elements for current alternative
                """
                for alt in list_of_alts:
                    alt_elem_index = 0
                    is_find = True
                    for elem in current_branch_alt:
                        if alt_elem_index >= len(alt):
                            is_find = False
                            break
                        if elem != alt[alt_elem_index]:
                            is_find = False
                        alt_elem_index += 1
                    if is_find == True and alt_elem_index == len(alt):
                        return True
                return False

            current_tree_name = ucst["rule_name"]
            finding_alternatives = []  # This is a list of that branch_num for tree, whose already present in dictionary
            if not is_first:
                # Finding is current alternative has already present in dictionary for rule dict_grammar[tree["name"]]
                # In current tree node can be several alternatives.
                # It is necessary handle all this alternatives separately
                current_branch_in_tree: List[str] = []  # this is a list of that "branch_num" which need not to add for current rule in grammar
                current_branch = 1
                for node in ucst["children"]:
                    if node["branch_num"] != current_branch:
                        # Process current formed branch
                        is_find_cur_alternative = check_presented_branch(dict_grammar[current_tree_name],
                                                                         current_branch_in_tree)
                        if is_find_cur_alternative:
                            finding_alternatives.append(current_branch)

                        # Add current node in a new branch
                        current_branch += 1
                        current_branch_in_tree = []
                    # And now after check we can add next element of subrule in list
                    # But before we must check if this leaf
                    if is_terminal(node) and node["name"] != "<EOF>":
                        tokens = self.parser.get_tokens(node["name"])
                        current_branch_in_tree.append(tokens[0]["type"])
                    else:
                        current_branch_in_tree.append(node["rule_name"])

                # if we out from previous "for" then we must handle last formed branch
                is_find_cur_alternative = check_presented_branch(dict_grammar[current_tree_name],
                                                                 current_branch_in_tree)
                if is_find_cur_alternative:
                    finding_alternatives.append(current_branch)

            # Fill alternative for current rule (tree) only if we have no such alternative yet
            current_branch = 0
            adding_list_of_child: List[str] = []
            for child in ucst["children"]:
                if child["branch_num"] not in finding_alternatives:
                    if child["branch_num"] != current_branch:
                        current_branch = child["branch_num"]
                        if adding_list_of_child != []:
                            dict_grammar[current_tree_name].append(adding_list_of_child)
                        adding_list_of_child = []
                    # if current child with correct "branch_num" in all cases we add it into next list
                    # check for correct adding current element (terminal, EOF, etc)
                    if is_terminal(child):
                        if child["name"] == "<EOF>":
                            adding_list_of_child.append("EOF")
                        else:
                            tokens = self.parser.get_tokens(child["name"])
                            adding_list_of_child.append(tokens[0]["type"])
                    else:
                        adding_list_of_child.append(child["rule_name"])

            if adding_list_of_child:
                dict_grammar[current_tree_name].append(adding_list_of_child)

        if is_terminal(ucst):
            return dict_grammar

        if ucst["rule_name"] in dict_grammar:
            write_rule_in_dict(dict_grammar, ucst, False)
        else:
            dict_grammar[ucst["rule_name"]] = []
            write_rule_in_dict(dict_grammar, ucst, True)

        for child in ucst["children"]:
            self._generate_grammar_dict(child, dict_grammar)

        return dict_grammar

    def _init_cst(self, tree, cnt_branches=1) -> None:
        """
        Init CST.

        Set defined count of branches for each node in CST.
        Each node according rule in grammar. Example, rule1: subrule1 | subrule2 |...|subruleN; 
        N is cnt_branches for node according rule1.
        """
        tree["branch_num"] = cnt_branches
        tree["cnt_branches"] = cnt_branches
        if self.is_unique_nodes:
            # First check if current node is LEAF?
            if is_terminal(tree):
                return
            else:
                # if cur node has only one element and it is terminal
                #  then not need build "rule_name" and account in self.ruleNameDict
                if len(tree["children"]) == 1 and is_terminal(tree["children"][0]):
                    single_child = tree["children"][0]
                    tree["rule_name"] = tree["name"]
                    single_child["branch_num"] = cnt_branches
                    single_child["cnt_branches"] = cnt_branches
                    return
                else:
                    # And here we have REAL rule name
                    if tree["name"] in self.ruleNameDict:
                        tree["rule_name"] = tree["name"] + str(self.ruleNameDict[tree["name"]])
                        self.ruleNameDict[tree["name"]] += 1
                    else:
                        self.ruleNameDict[tree["name"]] = 1
                        tree["rule_name"] = tree["name"]
        else:
            tree["rule_name"] = tree["name"]
        if tree["children"] is None:
            return
        for node in tree["children"]:
            self._init_cst(tree=node, cnt_branches=cnt_branches)

    def _core_merge(self, UCST, CST, all_branches_UCST, start_branch_UCST=1):
        """
        Find <num_branch_of_equal_subCST> - that number of branch of UCST for which we get
        full-curlevel-match with CST. Start search from <start_branch_UCST> branch
        """

        num_branch_of_equal_subCST = 0
        # Integrity check
        if start_branch_UCST > all_branches_UCST:
            return num_branch_of_equal_subCST

        # Preinstall before compare levels inside branches
        cur_compare_branch = start_branch_UCST
        cur_UCST_index = 0
        cur_CST_index = 0
        count_added_CST_nodes = len(CST)
        count_UCST_nodes = len(UCST)
        position_CST_node = 1
        position_UCST_node = 1
        is_equality_must_be_checked = False
        is_exit = False
        is_CST_exhausted = False
        is_changed_branch = False

        # REWIND UCST to start_branch_UCST
        # for speed up check if it is necessary rewind?
        if cur_compare_branch > 1:
            while cur_UCST_index < count_UCST_nodes:
                if UCST[cur_UCST_index]["branch_num"] < cur_compare_branch:
                    cur_UCST_index += 1
                else:
                    break
        # It is CAN NOT be possible this situation:
        # (start_branch_UCST <= all_branches_UCST) AND (cur_UCST_index >= count_UCST_nodes)
        # that is mean that UCST corrupt!

        # compare level inside branches
        while cur_compare_branch <= all_branches_UCST:
            # check if we can get next node from UCST
            if cur_UCST_index < count_UCST_nodes:
                cur_node_UCST = UCST[cur_UCST_index]
            else:
                # finished walk on UCST ust on first level in current call of _merge()
                is_equality_must_be_checked = True
                is_exit = True

            # check if we can get next node from UCST
            if cur_CST_index >= count_added_CST_nodes:
                is_CST_exhausted = True
                is_equality_must_be_checked = True
            else:
                cur_node_CST = CST[cur_CST_index]

            # if changed branch
            if cur_node_UCST["branch_num"] != cur_compare_branch:
                is_changed_branch = True
                is_equality_must_be_checked = True

            if is_equality_must_be_checked:
                # levels equal when all ust from CST in all ust of some branch in UCST
                if is_CST_exhausted == True and (is_changed_branch == True or is_exit == True):
                    num_branch_of_equal_subCST = cur_compare_branch
                    is_exit = True
                if is_exit:
                    break;
                if is_CST_exhausted:
                    cur_CST_index = 0
                    cur_node_CST = CST[cur_CST_index]
                    position_CST_node = 1
                if is_changed_branch:
                    cur_CST_index = 0
                    cur_compare_branch = cur_node_UCST["branch_num"]  # it must be (cur_compare_branch + 1)
                    position_CST_node = 1
                    position_UCST_node = 1

            # DO CHECK
            if cur_node_CST["name"] == cur_node_UCST["name"] and position_CST_node == position_UCST_node:
                is_sync = True
            else:
                # current branch in UCST NOT EQUAL to CST => we need pass current branch in UCST
                while cur_compare_branch == cur_node_UCST["branch_num"]:
                    if cur_UCST_index < count_UCST_nodes - 1:
                        cur_UCST_index += 1
                        cur_node_UCST = UCST[cur_UCST_index]
                    else:
                        break
                if cur_UCST_index == (count_UCST_nodes - 1) and cur_compare_branch == cur_node_UCST["branch_num"]:
                    # there is no tree2 in all branches in UCST tree1 => just exit from search:
                    # num_branch_of_equal_subUCST == 0
                    break
                else:
                    # we get next node from UCST with next branch, this situation controlled on
                    # next iteration here we only step back, because in common we do cur_UCST_index++
                    # on the end iteration
                    cur_UCST_index -= 1
                    # such as we must reset CST
                    cur_CST_index = -1

            # prepare to get next UCST node
            cur_UCST_index += 1
            cur_CST_index += 1
            is_equality_must_be_checked = False
            is_CST_exhausted = False
            is_changed_branch = False
        return num_branch_of_equal_subCST

    def _merge_full(self, sumTree, addedTree):
        """
        Merge two common syntax trees.

        Recursive function for merge two CST for sql-queries into one union CST (UCST).
        addedTree merged into sumTree, result in sumTree. UCST is sum of several CST.
        UCST in each node consists info about "branch_num of current node" and
        "total child branch: cnt_branches"
        :param sumTree: UCST (union common syntax tree)
        :param addedTree: CST (common syntax tree)
        """
        if addedTree["children"] is None or addedTree["children"] == []:
            return
        # Work data init
        UCST = sumTree["children"]
        CST = addedTree["children"]
        all_branches_UCST = sumTree["cnt_branches"]
        count_added_CST_nodes = len(CST)
        # we must find in UCST (sumTree) that branch that equal to CST (addedTree)

        num_branch_of_equal_subCST = self._core_merge(UCST, CST, all_branches_UCST)

        # now we find branch in which we have same tree (CST) like UCST
        if num_branch_of_equal_subCST != 0:
            cur_UCST_index = 0
            while UCST[cur_UCST_index]["branch_num"] != num_branch_of_equal_subCST:
                cur_UCST_index += 1

            cur_CST_index = 0
            while cur_CST_index < count_added_CST_nodes:
                self._merge_full(UCST[cur_UCST_index], CST[cur_CST_index])
                cur_CST_index += 1
                cur_UCST_index += 1
        else:
            sumTree["cnt_branches"] += 1
            for node2 in CST:
                self._init_cst(node2, 1)
                node2["branch_num"] = sumTree["cnt_branches"]
                node2["cnt_branches"] = 1
                UCST.append(node2)
        return sumTree

    def _merge_extend(self, sumTree, addedTree):
        """
        Merge two common syntax trees.

        Recursive function for merge two CST for sql-queries into one common UCST.
        addedTree merged into sumTree, result in sumTree.

        UCST is sum of several CST. UCST in each node consists info about
        "branch_num of current node" and "total child branch: cnt_branches"

        :param sumTree: UCST (union common syntax tree)
        :param addedTree: CST (common syntax treee)
        :return tuple (is_curlvl_full_imposition, is_curlvl_need_merge)
        :rtype tuple(bool,bool)
                where
                is_curlvl_full_imposition:
                    True - if full imposition of CST on some branch UCST
                    False - if there are no branches in UCST, wich full imposition with CST
                is_curlvl_need_merge:
                    True - it is possible make merge on sublevel, but this action translated on
                           current level
                    False - no need merge - this value not analyze
        """
        # if we have a leaf then end recursion
        if addedTree["children"] is None or addedTree["children"] == []:
            return True, False
        # Work data init
        UCST = sumTree["children"]
        CST = addedTree["children"]
        all_branches_UCST = sumTree["cnt_branches"]
        count_added_CST_nodes = len(CST)
        is_curlvl_full_imposition = False
        is_curlvl_need_merge = False
        # we must find in UCST (sumTree) that branch that equal to CST (addedTree)

        # Track level
        self.cur_level += 1

        # Check can we merge on next level
        # TODO: there are many options for optimizations; it is possible make more cleaver merge
        if self.cur_level <= self.merge_level and all_branches_UCST == 1:
            self.merge_level = self.cur_level + 1

        # It is necessary full-depth-check all branches in UCST
        #  * If we found branch that fully-depth equal to CST - nothing need to DO (that CST already include in UCST)
        #  * If we not found such branch we need add this CST to UCST (but we do it in some special way)
        is_still_finding_branch = True
        next_start_finding_branch = 0
        while is_still_finding_branch == True:
            num_branch_of_equal_subCST = self._core_merge(UCST, CST, all_branches_UCST, next_start_finding_branch)
            if num_branch_of_equal_subCST != 0:
                # rewind UCST to founded branch
                cur_UCST_index = 0
                while UCST[cur_UCST_index]["branch_num"] != num_branch_of_equal_subCST:
                    cur_UCST_index += 1
                # set index to start position in CST
                cur_CST_index = 0
                # DEEP check for founded branch: if next CST already exists in UCST
                while cur_CST_index < count_added_CST_nodes:
                    is_child_full_imposition, is_curlvl_need_merge = self._merge_extend(UCST[cur_UCST_index],
                                                                                        CST[cur_CST_index])
                    # if we get INFO from sublevel, that it is necessary merge we pass all next processing
                    if is_curlvl_need_merge:
                        is_still_finding_branch = False
                        break
                    # if there is no full imposition for current child-branch, we must try next
                    # TODO: there are many options for optimizations, 
                    #   ex.: we can count number of not-imposition and find branch with min numbers
                    if not is_child_full_imposition:
                        # current branch not matched; go to next in upper "while"
                        next_start_finding_branch = num_branch_of_equal_subCST + 1
                        # current level in UCST not matched for CST
                        is_curlvl_full_imposition = False
                        break
                    cur_CST_index += 1
                    cur_UCST_index += 1
                if cur_CST_index == count_added_CST_nodes:
                    # FIND full imposition for CST in UCST
                    is_curlvl_full_imposition = True
                    is_still_finding_branch = False
            else:
                is_still_finding_branch = False

        # Now check if we have full imposition on current level
        if not is_curlvl_full_imposition or is_curlvl_need_merge:
            # in ANY case we add on first level
            # but such as we can add if this is MERGE_LEVEL and CST consist one node
            #  remark: if CST consist more than one node we try MERGE on previous level
            if (self.cur_level <= self.merge_level and count_added_CST_nodes == 1) or self.cur_level == 1:
                # ADD CST to UCST
                sumTree["cnt_branches"] += 1
                for node2 in CST:
                    self._init_cst(node2, 1)
                    node2["branch_num"] = sumTree["cnt_branches"]
                    node2["cnt_branches"] = 1
                    UCST.append(node2)
                # return 1) True, such as we get imposition of CST in UCST (because we just add this imposition!)
                # return 2) False, because not need merge on previous level
                self.cur_level -= 1
                return True, False
            else:
                # if we have no full imposition and can not merge on current level
                # then return
                #  1) False, it is no full imposition
                #  2) False, because not need merge on previous level - this not option at all
                if self.cur_level > self.merge_level:
                    self.cur_level -= 1
                    return False, False
                else:
                    self.cur_level -= 1
                    return True, True
        # dummy return
        self.cur_level -= 1
        return is_curlvl_full_imposition, False

    def _generate_ucst_from_file(self, file_name: str) -> Dict:
        """ Generate a UCST from queries in file.
        Each request shuld be located on one line.
        """
        ucst = None
        try:
            f = open(file_name, "r")
        except IOError as err:
            print("Source grammar file IO error.")
            print(err)
            raise IOError("Source grammar file IO error.")
        else:
            line = f.readline()
            ucst = self.parser.get_dictionary_tree(line)
            self._init_cst(ucst)
            for line in f:
                tree = self.parser.get_dictionary_tree(line)
                if tree:
                    self.merge_func(ucst, tree)
                else:
                    print("\nError when parsing query for dejector. Query:\n ", line)
            f.close()
        return ucst

    def _generate_ucst_from_json(self, queries):
        """ Generate a UCST from queries in json.

        :param queries: queries in JSON Format: ["select 1", "select 2"].
        """
        ucst = self.parser.get_dictionary_tree(queries[0])
        self._init_cst(ucst)
        for q in queries:
            tree = self.parser.get_dictionary_tree(q)
            if tree:
                self.merge_func(ucst, tree)
            else:
                print("\nError when parsing query for dejector. Query:\n ", q)
        return ucst

    def generate_grammar(self, ucst, grammar_name):
        """ Generate grammar for text in file. 

        :param ucst: Dejector Union common syntax tree.
        :param grammar_name: name of the target grammar.
        """
        parser_grammar = self._generate_parser_grammar(ucst)
        original_lexer_file = os.path.join(config.GRAMMARS_PATH, self.vendor, self.vendor + "Lexer.g4")
        lexer_grammar = ""

        try:
            f = open(original_lexer_file, "r")
        except IOError as err:
            print(err)
            raise IOError("Original lexer file IO error.")
        else:
            for line in f:
                if not line.startswith("lexer"):
                    lexer_grammar += line
            f.close()

        # Prepare Lexer grammar
        lexer_prefix = "lexer grammar " + grammar_name + "Lexer;\n"
        lexer_grammar = lexer_prefix + lexer_grammar
        grammar_filename_lexer = grammar_name + "Lexer.g4"

        # Prepare Parser grammar
        parser_prefix = "parser grammar " + grammar_name + "Parser;"
        parser_prefix += "\noptions { tokenVocab=" + grammar_name + "Lexer; }"
        parser_grammar = parser_prefix + parser_grammar
        grammar_filename_parser = grammar_name + "Parser.g4"

        grammar_path = os.path.join(config.OUTPUT_GRAMMARS_PATH, grammar_name)
        if not os.path.exists(grammar_path):
            os.makedirs(grammar_path)

        # Write Lexer file
        try:
            g = open(os.path.join(grammar_path, grammar_filename_lexer), "w")
        except IOError as err:
            print(err)
            raise IOError("Output grammar lexer generation error.")
        else:
            g.write(lexer_grammar)
            g.close()

        # Write Parser file
        try:
            g = open(os.path.join(grammar_path, grammar_filename_parser), "w")
        except IOError as err:
            print(err)
            raise IOError("Output grammar generation error.")
        else:
            g.write(parser_grammar)
            g.close()

        os.system(f"cd {grammar_path};" +
                  "java -jar /usr/local/lib/antlr-4.7-complete.jar -Dlanguage=Python3" +
                  f" {grammar_filename_lexer} {grammar_filename_parser} -o {config.OUTPUT_PATH}"
        )

    def build_from_file(self, file_name: str) -> None:
        """ Generates lexer and parser for queries located in file. """
        ucst = self._generate_ucst_from_file(file_name)
        self.generate_grammar(ucst, self.name)

    def build_from_json(self, json) -> None:
        """ Generates lexer and parser for queries located in json. """
        ucst = self._generate_ucst_from_json(json)
        self.generate_grammar(ucst, self.name)

    def get_from_file(self, file_name: str) -> Parser:
        """ Generates and returns lexer and parser for queries located in file. """
        self.build_from_file(file_name)
        return ParserFactory.create(vendor=self.name)

    def get_from_json(self, json) -> Parser:
        """ Generates and returns lexer and parser for queries located in json. """
        self.build_from_json(json)
        return ParserFactory.create(vendor=self.name)


class DejectorFactory:
    """
    A DejectorFactory class.

    Implements factory for dejectors.
    """

    @staticmethod
    def create(vendor: str, name: str,  mode: str) -> Dejector:
        """
        Creates Dejector.
        :param vendor: base language vendor name
        :type vendor: str
        :param name: generated sublanguage name
        :type name: str
        :param mode: Dejector mode
        :type name: str
        :return: Dejector object
        """
        parser = ParserFactory.create(vendor)
        return Dejector(vendor, name, parser, mode)

    @staticmethod
    def is_exist(dejector: Dejector) -> bool:
        """
        Checks if a specified dejector exists.
        :param dejector: dejector object
        :type dejector: Dejector
        :return: bool
        """
        return DejectorFactory.is_name_exist(dejector.name)

    @staticmethod
    def is_name_exist(name: str) -> bool:
        """
        Checks if a specified dejector exists.
        :param name: dejector name
        :type name: str
        :return: bool
        """
        if name in [v.value for v in Vendors]:
            raise ValueError("Incorrect grammar name in DejectorFactory 'is_exist' method.")

        grammar_path = os.path.join(config.OUTPUT_GRAMMARS_PATH, name)
        if not os.path.exists(grammar_path):
            return False

        files = ["Lexer.py", "Parser.py"]
        for f in files:
            filename = os.path.join(config.OUTPUT_PATH, name + f)
            if not os.path.exists(filename):
                return False
        return True

    @staticmethod
    def dispose(dejector: Dejector) -> None:
        """
        Disposes generated dejector by object.
        :param dejector: dejector object
        :type dejector: Dejector
        :return: None
        """
        DejectorFactory.dispose_by_name(dejector.name)


    @staticmethod
    def dispose_by_name(name: str) -> None:
        """
        Dispose generated dejector by name.
        Delete all auto-generated code and grammar for dejector.
        :param name: dejector sublanguage name
        :type name: str
        :return: None
        """

        # Check if a name is not protected.
        if name in [v.value for v in Vendors]:
            raise ValueError("Incorrect grammar name in DejectorFactory 'dispose' method.")

        grammar_path = os.path.join(config.OUTPUT_GRAMMARS_PATH, name)
        if os.path.exists(grammar_path):
            shutil.rmtree(grammar_path)

        files = ["Lexer.py", "Parser.py", ".tokens", "Lexer.tokens", "Listener.py",
                 "Parser.tokens", "ParserListener.py"]
        for f in files:
            filename = os.path.join(config.OUTPUT_PATH, name + f)
            if os.path.exists(filename):
                os.remove(filename)
