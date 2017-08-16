from copy import deepcopy

from aule.codegen import ust
from ..base import BaseGenerator
from .helpers import TypeHelpers, ENUMEXCEPTION, INCLUDES


class Generator(BaseGenerator):
    TEMPLATE_FILE = "cpp.jinja2"
    BAD_WORDS = [
        "alignas",    "alignof",        "and",             "and_eq",         "asm",
        "auto",       "bitand",         "bitor",           "bool",           "break",
        "case",       "catch",          "char",            "char16_t",       "char32_t",
        "class",      "compl",          "const",           "constexpr",      "const_cast",
        "continue",   "decltype",       "default",         "delete",         "do",
        "double",     "dynamic_cast",   "else",            "enum",           "explicit",
        "export",     "extern",         "false",           "float",          "for",
        "friend",     "goto",           "if",              "inline",         "int",
        "long",       "mutable",        "namespace",       "new",            "noexcept",
        "not",        "not_eq",         "nullptr" ,        "operator",       "or",
        "or_eq",      "private",        "protected",       "public",         "register",
        "reinterpret_cast",             "return",          "short",          "signed",
        "sizeof",     "static",         "static_assert",   "static_cast",    "struct",
        "switch",     "template",       "this",            "thread_local",   "throw",
        "true",       "try",            "typedef",         "typeid",         "typename",
        "union",      "unsigned",       "using",           "virtual",        "void",
        "volatile",   "wchar_t",        "while",           "xor",            "xor_eq"
    ]

    def __init__(self, **options):
        super(Generator, self).__init__()

    def use_tree(self, tree, mutableAST=False):
        the_tree = tree if mutableAST else deepcopy(tree)
        # Build inner structures,
        super(Generator, self).use_tree(the_tree)
        self.class_references = ust.helpers.ClassesReference(self.classes)
        # Rewrite inner tree.
        self.rebuild_constructors()
        # IMPORTANT! Filter is a closure of the method owner so we need to
        # inject the them after all tree processing.
        self.helpers = TypeHelpers(self.class_references)
        self.inject_filters(
            gen_return=self.helpers.gen_return,
            gen_modifiers=self.helpers.gen_modifiers,
            typed=self.helpers.typed,
            is_nullable=self.helpers.is_nullable,
            translate_type=self.helpers.translate_type,
            separate_args=self.helpers.separate_args,
        )
        self.inject_tests(
            abstract=ust.helpers.is_abstract,
            parent=self.class_references.is_parent_for_somebody,
        )
        self.inject_filters(
            get_args=self.class_references.get_constructor_args,
        )
        return self

    def generate(self):
        code = super(Generator, self).generate()
        if self.enums:
            code = ENUMEXCEPTION + "\n" + code.strip()
        return INCLUDES + code

    def rebuild_constructors(self):
        """ Changes constructors definitions:
            - get all non-abstract fields
            - add arguments from all parent constructors
            - add custom fields from old constructor
        """
        for cls in self.classes:
            self._change_constructor(cls)

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
            if not any(field.name == arg.name for field in cls.fields):
                new_args[arg.name] = arg
        cls.constructor.arguments = sorted(list(new_args.values()), key=lambda ar: TypeHelpers.is_nullable(ar.type))
        setattr(cls, "constructor_created", True)