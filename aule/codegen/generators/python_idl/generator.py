from copy import deepcopy

from .. import python
from .methods import *
from .classes import *


class Generator(python.Generator):
    def __init__(self, add_listener=False, add_visitor=False, **options):
        super(Generator, self).__init__(**options)
        self.add_listener = add_listener
        self.add_visitor = add_visitor

    def use_tree(self, tree, mutableAST=False):
        super(Generator, self).use_tree(tree, mutableAST)
        # We are going to modify classes, so get a copy of them
        self.src_classes = deepcopy(self.classes)
        for cls in self.classes:
            # Replace the only object parent with pickler.
            if len(cls.parents) == 1 \
                    and cls.parents[0] == python.Generator.OBJECT_CLASS:
                cls.parents[0] = PICKLER_CLASS
            # Then inject Pickler as a parent for all classes that has no parents
            # inherited from it
            if not self.classes_reference.is_inherited_from(cls, PICKLER_CLASS, recursive=True):
                cls.parents.append(PICKLER_CLASS)
            # Inject listener and visitor methods if necessary
            if self.add_listener:
                inject_listener(cls)
            if self.add_visitor:
                inject_visitor(cls)
            # DBFW needs all arguments of constructor to be optional, so add
            # default value to all of them
            for arg in cls.constructor.arguments:
                arg.default = "None"
        return self

    def generate(self):
        self.mangled_names = {}
        self.inject_vars(
            mangled=self.pop_mangled,
        )
        code = super(Generator, self).generate()
        first_class_idx = code.find("class")
        return code[:first_class_idx] + PICKLER + "\n\n" + code[first_class_idx:]

    def generate_listener(self):
        self.env.globals.pop("mangled", None)
        return self.env.get_template(self.TEMPLATE_FILE).render(
            classes=[
                create_listener(self.src_classes)
            ],
        )

    def generate_visitor(self):
        self.env.globals.pop("mangled", None)
        return self.env.get_template(self.TEMPLATE_FILE).render(
            classes=[
                create_visitor(self.src_classes)
            ],
        )

    def generate_decoder(self):
        self.env.globals.pop("mangled", None)
        return self.env.get_template(self.TEMPLATE_FILE).render(
            classes=[
                create_factory(self.src_classes)
            ],
        )

    def get_name(self, node, bad_words=None):
        common_name = super(Generator, self).get_name(node, bad_words=[])
        python_name = super(Generator, self).get_name(node, bad_words)
        if python_name != common_name:
            self.mangled_names[common_name] = python_name
        return python_name

    def pop_mangled(self):
        """ Returns mangled from last call (or beginning) names and clear mangled """
        cur_mangled = self.mangled_names
        self.mangled_names = {}
        return cur_mangled
