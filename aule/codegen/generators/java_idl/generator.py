from ..base import BaseGenerator
from . import helpers

class Generator(BaseGenerator):

    TEMPLATE_FILE = "java.jinja2"

    DECODER_TEMPLATE_FILE = "javaDecoder.jinja2"

    BAD_WORDS = [
        "abstract",   "continue",    "for",            "new",          "switch",
        "assert",     "default",     "goto",           "package",      "synchronized",
        "boolean",    "do",           "if",            "private",      "this",
        "break",      "double",      "implements",     "protected",    "throw",
        "byte",       "else",        "import",         "public",       "throws",
        "case",       "enum",        "instanceof",     "return",       "transient",
        "catch",      "extends",     "int",            "short",        "try",
        "char",       "final",       "interface",      "static",       "void",
        "class",      "finally",     "long",           "strictfp",     "volatile",
        "const",      "float",       "native",         "super",        "while"
    ]

    def __init__(self, **options) -> None:
        super(Generator, self).__init__()
        self.inject_filters(
            gen_modifiers=helpers.gen_modifiers,
            typed=helpers.typed,
            translate_type=helpers.translate_type,
            gen_property=helpers.gen_property,
            gen_enum_body=helpers.gen_enum_body
        )

    def use_tree(self, tree, mutableAST=False):
        super(Generator, self).use_tree(tree)
        return self

    def generate_decoder(self):
        return self.env.get_template(self.DECODER_TEMPLATE_FILE).render(
            classes=self.classes,
            functions=self.functions,
            variables=self.vars,
            enums=self.enums,
        )