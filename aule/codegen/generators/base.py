import jinja2
from os import path
from typing import List

from aule.config import BASE_DIR
from aule.codegen import ust

from .helpers import Jinja2RaiseExtension


class BaseGenerator(object):
    TEMPLATE_DIR = path.join(BASE_DIR, "resources", "templates")
    TEMPLATE_FILE = ""
    # BAD_WORDS will be redefined by derived classes to mask keywords.
    BAD_WORDS: List[str] = []

    # Declarations of class properties
    classes: List[ust.ClassDeclaration]
    functions: List[ust.FunctionDeclaration]
    vars: List[ust.VariableDeclaration]
    enums: List[ust.EnumDeclaration]

    def __init__(self) -> None:
        self.__prepare_env()
        self.inject_tests(
            block=is_block
        )
        self.inject_filters(
            name=self.get_name
        )
        self.classes = None
        self.functions = None
        self.vars = None

    def use_tree(self, tree):
        self.classes = []
        self.functions = []
        self.vars = []
        self.enums = []
        for node in tree:
            if isinstance(node, ust.ClassDeclaration):
                self.classes.append(node)
            elif isinstance(node, ust.FunctionDeclaration):
                self.functions.append(node)
            elif isinstance(node, ust.VariableDeclaration):
                self.vars.append(node)
            elif isinstance(node, ust.EnumDeclaration):
                self.enums.append(node)
        return self

    def generate(self, **env_vars):
        return self.env.get_template(self.TEMPLATE_FILE).render(
            classes=self.classes,
            functions=self.functions,
            variables=self.vars,
            enums=self.enums,
            **env_vars,
        )

    def get_name(self, node, bad_words=None) -> str:
        """ jinja filter which gets name of the node. We have it in a class to
        have a possibility to redefine it in child classes.

        :type node: Identifier | Any UST node which was .name property
        :param bad_words: list of bad identifiers (self.BAD_WORDS by default)
        """
        if isinstance(node, ust.Identifier):
            name = node.name
            immutable = node.immutable
        elif hasattr(node, "name") and isinstance(node.name, ust.Identifier):
            name = node.name.name
            immutable = node.name.immutable
        else:
            name = str(node)
            immutable = False
        bad_words = bad_words if bad_words is not None else self.BAD_WORDS
        if not immutable and name in bad_words:
            return name + "_"
        return name

    def inject_vars(self, **vars):
        for k, v in vars.items():
            self.env.globals[k] = v

    def inject_filters(self, **filters):
        for k, v in filters.items():
            self.env.filters[k] = v

    def inject_tests(self, **tests):
        for k, v in tests.items():
            self.env.tests[k] = v

    def __prepare_env(self):
        self.env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(self.TEMPLATE_DIR),
            trim_blocks=True,
            lstrip_blocks=True,
            autoescape=False,
            extensions=[Jinja2RaiseExtension]
        )


def is_block(node):
    """ jinja test which tests whether the @node is Block """
    return isinstance(node, ust.Block)
