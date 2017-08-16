from copy import deepcopy

from aule.codegen import ust

from ..base import BaseGenerator


class Generator(BaseGenerator):
    TEMPLATE_FILE = "python.jinja2"
    # BAD_WORDS contains all Python 3.6 keywords and keywords, protected in ANTLR, and will be used by
    # self.get_name(node) function of base generator.
    # NB: https://docs.python.org/3.6/reference/lexical_analysis.html#keywords
    #     https://github.com/antlr/antlr4/blob/master/tool/src/org/antlr/v4/codegen/target/Python3Target.java
    BAD_WORDS = [
        "False",       "class",       "finally",    "is",         "return",
        "None",        "continue",    "for",        "lambda",     "try",
        "True",        "def",         "from",       "nonlocal",   "while",
        "and",         "del",         "global",     "not",        "with",
        "as",          "elif",        "if",         "or",         "yield",
        "assert",      "else",        "import",     "pass",       "args",
        "break",       "except",      "in",         "raise",      "kwargs",

        "abs",         "all",         "any",        "apply",      "bin",
        "bool",        "buffer",      "bytearray",  "callable",   "chr",
        "classmethod", "coerce",      "compile",    "complex",    "delattr",
        "dict",        "dir",         "divmod",     "enumerate",  "eval",
        "execfile",    "file",        "filter",     "float",      "format",
        "frozenset",   "getattr",     "globals",    "hasattr",    "hash",
        "help",       "hex",          "id",         "input",      "int",
        "intern",     "isinstance",   "issubclass", "iter",       "len",
        "list",       "locals",       "map",        "max",        "min",
        "next",       "memoryview",   "object",     "oct",        "open",
        "ord",        "pow",          "print",      "property",   "range",
        "raw_input",  "reduce",       "reload",     "repr",       "return",
        "reversed",   "round",        "set",        "setattr",    "slice",
        "sorted",     "staticmethod", "str",        "sum",        "super",
        "tuple",      "type",         "unichr",     "unicode",    "vars",
        "zip",        "__import__"
    ]
    OBJECT_CLASS = ust.Identifier("object", immutable=True)
    ABSTRACT_PARENT = ust.Identifier("abc.ABC", immutable=True)

    def __init__(self, **options) -> None:
        super(Generator, self).__init__()
        self.inject_tests(
            object_derived=is_object_derived,
            abstract=ust.helpers.is_abstract,
        )
        self.has_abstract = None

    def use_tree(self, tree, mutableAST=False):
        super(Generator, self).use_tree(tree)
        self.classes_reference = ust.helpers.ClassesReference(self.classes)
        self.has_abstract = False
        for i, cls in enumerate(self.classes):
            # Copy class if necessary cos we are going to modify them
            if not mutableAST:
                cls_copy = deepcopy(cls)
                self.classes[i] = cls_copy
                cls = cls_copy
            # Check for abstractness
            if ust.helpers.is_abstract(cls):
                if not self.classes_reference.is_inherited_from(cls, self.ABSTRACT_PARENT):
                    cls.parents.insert(0, self.ABSTRACT_PARENT)
                    self.has_abstract = True
            # Append object to classes without parents
            if len(cls.parents) == 0:
                cls.parents.append(self.OBJECT_CLASS)
            # Remove abstract fields from init
            new_args = []
            for arg in cls.constructor.arguments:
                field = next((f for f in cls.fields if str(f.name) == str(arg.name)), None)
                # Skip the element if it's some custom argument or abstract property
                if field is None or ust.Modifier.ABSTRACT not in field.modifiers:
                    new_args.append(arg)
            cls.constructor.arguments = new_args
            # Add "pass" to empty init
            if len(cls.fields) == 0 and len(cls.constructor.body.body) == 0:
                cls.constructor.body = ust.Block(["pass"])
        return self

    def generate(self):
        # has_abstract set to True tells template to add "import abc" line.
        return super(Generator, self).generate(has_abstract=self.has_abstract)


def is_object_derived(cls):
    """
    Test for jinja template that tests whether the class derived only from
    object
    :type cls: ust.ClassDeclaration
    :rtype: bool
    """
    return len(cls.parents) == 1 and cls.parents[0].name == "object"
