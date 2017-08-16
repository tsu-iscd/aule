from typing import List
from copy import deepcopy
from itertools import chain

from aule.codegen import ust
from ..base import BaseGenerator
from .helpers import TypeHelpers


class Generator(BaseGenerator):
    TEMPLATE_FILE = "kotlin.jinja2"

    # BAD_WORDS contains hard keywords of Kotlin language and will be used by
    # self.get_name(node) function of base generator.
    # NB: https://github.com/JetBrains/kotlin/blob/master/core/descriptors/src/org/jetbrains/kotlin/renderer/KeywordStringsGenerated.java
    BAD_WORDS = [
        "package", "as", "typealias", "class", "this", "super",
        "val", "var", "fun", "for", "null", "true",
        "false", "is", "in", "throw", "return", "break",
        "continue", "object", "if", "try", "else", "while",
        "do", "when", "interface", "typeof",
    ]

    # Declarations of class properties
    class_references: ust.helpers.ClassesReference

    def __init__(self,
                 package: str = "",
                 additional_imports: List[str] = None,
                 **options) -> None:
        """
        :param package: Destination package string that will be appended to all
                        generated code.
        :param additional_imports: List of additional import strings.
        """
        super(Generator, self).__init__()
        self.package = package
        self.imports = additional_imports or []

    def use_tree(self, tree, mutableAST=False):
        the_tree = tree if mutableAST else deepcopy(tree)
        # Build inner structures,
        super(Generator, self).use_tree(the_tree)
        self.class_references = ust.helpers.ClassesReference(self.classes)
        # Rewrite inner tree.
        self.rebuild_constructors()
        self.mark_overrides()
        # IMPORTANT! Filter is a closure of the method owner so we need to
        # inject the them after all tree processing.
        helpers = TypeHelpers(self.class_references)
        helpers.name_resolver = self.get_name
        self.inject_filters(
            gen_return=helpers.gen_return,
            gen_modifiers=helpers.gen_modifiers,
            typed_arg=helpers.typed_arg,
            typed_var=helpers.typed_var,
            translate_type=helpers.translate_type,
        )
        self.inject_tests(
            abstract=ust.helpers.is_abstract,
            parent=self.class_references.is_parent_for_somebody,
        )
        self.inject_filters(
            get_args=self.class_references.get_constructor_args,
        )
        return self

    def generate(self, **env_vars):
        prefix = ""
        if self.package:
            prefix += "package {0}\n\n".format(self.package)
        if self.imports:
            prefix += "{0}\n".format("\n".join(self.imports))
        code = super(Generator, self).generate(**env_vars)
        return prefix + "\n" + code

    def rebuild_constructors(self):
        """ Changes constructors definitions:
            - get all non-abstract fields
            - add arguments from all parent constructors
            - add custom fields from old constructor
        """
        for cls in self.classes:
            self._change_constructor(cls)

    def mark_overrides(self):
        """ Changes all fields and methods declarations marking them
            - 'overridden' if class member shadowed by some of the child's ones
            - 'overrides' if class member shadows some of the parents' ones
        """
        for cls in self.classes:
            for member in chain(cls.fields, cls.methods):
                overriden_member = self.class_references.overrides(member, cls)
                if overriden_member is not None:
                    setattr(member, "overrides", True)
                    setattr(overriden_member, "overridden", True)

    def _change_constructor(self, cls: ust.ClassDeclaration):
        """ Change constructor if it wasn't """
        if getattr(cls, "constructor_created", False):
            return
        new_args = {}
        # All non-abstract fields
        for field in cls.fields:
            if ust.Modifier.ABSTRACT not in field.modifiers:
                new_args[field.name] = ust.Argument(
                    name=field.name, type=field.type, default=field.default,
                )
        # Arguments from all parent constructors
        for parent_id in cls.parents:
            parent = self.class_references[parent_id]
            self._change_constructor(parent)
            for parg in parent.constructor.arguments:
                new_args[parg.name] = parg
        # Custom constructor arguments (if any)
        for arg in cls.constructor.arguments:
            # If there is no such field, that's custom argument - we need that guy
            if any(field.name == arg.name for field in cls.fields):
                new_args[arg.name] = arg
        cls.constructor.arguments = list(new_args.values())
        setattr(cls, "constructor_created", True)