from aule.codegen import ust


def json_type_annotation(cls: ust.ClassDeclaration) -> str:
    return "@JsonTypeName(\"{}\")".format(cls.name)


def json_field_annotation(field: ust.FieldDeclaration) -> str:
    return "@JsonProperty(\"{}\")".format(field.name)
