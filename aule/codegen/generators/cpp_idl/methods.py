from typing import List

from ..cpp.helpers import TypeHelpers
from aule.codegen.ust import *
from ..cpp import Generator as CPPGenerator


def inject_listener(cls):
    """
    :type cls: ust.ClassDeclaration
    """
    cls.methods.append(
        MethodDeclaration(
            name=Identifier("enterNode"),
            arguments=[
                Argument(
                    name=Identifier("listener"),
                    type=TypeReference(Identifier("ASTListener"))
                )
            ],
            returns=[],
            body=Block([
                "listener->enter{}(this);".format(cls.name),
            ]),
            modifiers=[
                Modifier.ABSTRACT]
        )
    )

    cls.methods.append(
        MethodDeclaration(
            name=Identifier("exitNode"),
            arguments=[
                Argument(
                    name=Identifier("listener"),
                    type=TypeReference(Identifier("ASTListener"))
                )
            ],
            returns=[],
            body=Block([
                "listener->exit{}(this);".format(cls.name),
            ]),
            modifiers=[
                Modifier.ABSTRACT]
        )
    )


def inject_visitor(cls):
    """
    :type cls: ust.ClassDeclaration
    """
    cls.methods.append(
        MethodDeclaration(
            name=Identifier("accept"),
            arguments=[
                Argument(
                    name=Identifier("visitor"),
                    type=TypeReference(Identifier("ASTVisitor"))
                )
            ],
            returns=[TypeReference(Identifier("Any"))],
            body=Block([
                "return visitor->visit{}(this);".format(cls.name),
            ]),
            modifiers=[
                Modifier.ABSTRACT]
        )
    )


VECTOR2JSON = """\
'[';
first_ = true;
for(auto elem : {0}{1}){{
    if( !first_ )
        ss_ << \", \";
    ss_ << elem->toJSON();
}}
ss_ << ']'"""


def inject_toJSON(classes: List[ClassDeclaration]):
    l_helpers = TypeHelpers(helpers.ClassesReference(classes))
    for cls in classes:
        cls.methods.append(
            MethodDeclaration(
                name=Identifier("toJSON"),
                arguments=[],
                returns=[TypeReference(SimpleType.STRING)],
                body = gen_toJSON_body(l_helpers, cls),
                modifiers=[]
            )
        )


def gen_toJSON_body(helpers: TypeHelpers, cls: ClassDeclaration) -> Block:
    code  = "bool first_;\n"
    code += "stringstream ss_;\n"
    code += "ss_ << '{'"
    # In C++   << "\"type\": \"Node\""
    # In JSON "type": "Node"
    code += " << \"\\\"type\\\": \\\"" + cls.name.name + "\\\"\""
    # Add other fields (including inherited from ancestors)
    for arg in cls.constructor.arguments:
        code += " << \", \""
        code += " << \"\\\""+arg.name.name+"\\\": \" << "
        # Argument type is basic type => call auxiliary functions
        if arg.type.type in SimpleType:
            code += "simple_toJSON("+CPPGenerator.get_name(CPPGenerator, arg.name.name)+")"
        # Argument type is Optional
        elif helpers.translate_type(arg.type).find("Optional<") == 0:
            if helpers.is_array(arg.type):
                code += VECTOR2JSON.format("*", CPPGenerator.get_name(CPPGenerator, arg.name.name))
            else:
                code += "({0} ? simple_toJSON(*{0}) : \"null\")".format(CPPGenerator.get_name(CPPGenerator, arg.name.name))
        # Argument type is array of Id or Enum
        elif helpers.is_array(arg.type):
            code += VECTOR2JSON.format("", CPPGenerator.get_name(CPPGenerator, arg.name.name))
        # All other cases
        else:
            code += "({0} ? {0}->toJSON() : \"null\")".format(CPPGenerator.get_name(CPPGenerator, arg.name.name))
    code += " << '}';\n"
    code += "return ss_.str();"
    return Block([code])