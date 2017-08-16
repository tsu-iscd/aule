import json
from copy import deepcopy
from typing import Union

from aule.codegen import ust
from ..base import BaseGenerator


class Generator(BaseGenerator):
    TEMPLATE_FILE = "json_schema.jinja2"
    BASE_CLASS = "PIPData"

    def __init__(self, **options):
        super(Generator, self).__init__()
        self.inject_filters(
            as_jsl_field=as_jsl_field,
        )
        self.inject_vars(
            BASE_CLASS=self.BASE_CLASS,
        )

    def use_tree(self, tree, mutableAST=False):
        super(Generator, self).use_tree(tree)
        for i, cls in enumerate(self.classes):
            if len(cls.parents) == 0:
                if mutableAST:
                    cls.parents.append(ust.Identifier("jsl.Document"))
                else:
                    cls_copy = deepcopy(cls)
                    cls_copy.parents.append(ust.Identifier("jsl.Document"))
                    self.classes[i] = cls_copy
        return self

    def generate_jsl(self):
        return super(Generator, self).generate()

    def generate_scheme(self):
        jsl_classes = self.generate_jsl()
        runtime = {}
        exec(jsl_classes, runtime, runtime)
        base = runtime[self.BASE_CLASS]()
        return json.dumps(base.get_schema(ordered=True), indent=4)

    def generate(self):
        return self.generate_scheme()


def as_jsl_field(f: ust.FieldDeclaration) -> str:
    """ Translates IDL field into the JSL field """
    return translate_type(f.type)


def translate_type(
        node: Union[ust.SimpleType, ust.Identifier, ust.UnionType, ust.TypeReference],
        recursive: bool = False) -> str:
    """ Recursively translates IDL type into specific JSL declaration """
    TYPES_MAP = {
        ust.SimpleType.INTEGER: "jsl.fields.IntField",
        ust.SimpleType.FLOAT: "jsl.fields.NumberField",
        ust.SimpleType.STRING: "jsl.fields.StringField",
        ust.SimpleType.BOOLEAN: "jsl.fields.BooleanField",
        ust.SimpleType.NULL: "jsl.fields.NullField",
    }
    DOCUMENT_FIELD = "jsl.DocumentField({}, as_ref=True)"
    ARRAY_FIELD = "jsl.ArrayField({})"
    UNION_FIELD = "jsl.OneOfField([{}])"
    if isinstance(node, ust.SimpleType) and node in TYPES_MAP:
        return "{}()".format(TYPES_MAP[node])
    elif isinstance(node, ust.Identifier):
        return DOCUMENT_FIELD.format(node)
    elif isinstance(node, ust.TypeReference):
        if node.is_sequence:
            return ARRAY_FIELD.format(
                translate_type(node.type, recursive=True)
            )
        else:
            return translate_type(node.type, recursive=True)
    elif isinstance(node, ust.UnionType):
        return UNION_FIELD.format(
            ', '.join(translate_type(alt, recursive=True)
                      for alt in node.types)
        )
    raise TypeError("Unknown node {}".format(node))
