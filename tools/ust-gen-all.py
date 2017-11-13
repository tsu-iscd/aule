from aule.codegen import GeneratorFactory, Language
from aule.codegen.ust import *

parent_class = ClassDeclaration(
    name=Identifier("Fart"),
    fields=[
            FieldDeclaration(
                name=Identifier("type"),
                type=TypeReference(SimpleType.STRING),
                default="\"Fart\""
            ),
            FieldDeclaration(
                name=Identifier("fart"),
                type=TypeReference(SimpleType.STRING, True),
            ),
            FieldDeclaration(
                name=Identifier("cocos"),
                type=TypeReference(SimpleType.STRING),
                default="\"heeeelo, I'm constant\"",
                modifiers=[Modifier.ABSTRACT]
            )
        ],
    methods=[
        MethodDeclaration(
            name=Identifier("abstract_one"),
            arguments=[],
            returns=[TypeReference(SimpleType.STRING)],
            body=Block(["pass"]),
            modifiers=[Modifier.ABSTRACT]
        )
    ]
)

dumb_class = ClassDeclaration(
    name=Identifier("Dumb"),
    parents=[Identifier("Fart")],
    fields=[
        FieldDeclaration(
            name=Identifier("type"),
            type=TypeReference(SimpleType.STRING),
            default="\"Dumb\""
        ),
        FieldDeclaration(
            name=Identifier("bar"),
            type=TypeReference(
                UnionType([
                    TypeReference(SimpleType.INTEGER),
                    TypeReference(SimpleType.NULL),
            ])),
            modifiers=[Modifier.ABSTRACT],

        )
    ],
    methods=[
        MethodDeclaration(
            name=Identifier("foo"),
            arguments=[
                Argument(Identifier("foo_arg"), TypeReference(SimpleType.STRING, True), '"foo"')
            ],
            returns=[TypeReference(SimpleType.STRING, True)],
            body=Block([
                "if 1",
                Block([
                    "if 1",
                    Block(["return foo_arg"]),
                    "return foo_arg"
                ]),
                "return foo_arg"
            ]),
        ),
    ],
)

program = [parent_class, dumb_class]

if __name__ == "__main__":
    print("*"*30+"PYTHON"+"*"*30)
    pygen = GeneratorFactory.create(
        language=Language.python3,
    ).use_tree(program)
    print(pygen.generate())

    print("*"*30+"GOLANG"+"*"*30)
    gogen = GeneratorFactory.create(
        language=Language.golang,
    ).use_tree(program)
    print(gogen.generate())

    print("*"*30+"JSL"+"*"*30)
    schemegen = GeneratorFactory.create(
        language=Language.jsonScheme,
    ).use_tree(program)
    print(schemegen.generate_jsl())
    # print(schemegen.generate())

    print("*"*30+"CPP"+"*"*30)
    cppgen = GeneratorFactory.create(
        language=Language.cpp,
    ).use_tree(program)
    print(cppgen.generate())

    print("*"*30+"Python IDL"+"*"*30)
    dbfwgen = GeneratorFactory.create(
        language=Language.pythonIDL,
        add_visitor=True,
        add_listener=True,
    )
    dbfwgen.use_tree(program)
    print(dbfwgen.generate())
    print(dbfwgen.generate_listener())
    print(dbfwgen.generate_visitor())
    print (dbfwgen.generate_decoder())

    print("*"*30+"ECMAScript"+"*"*30)
    ecmascriptgen = GeneratorFactory.create(
        language=Language.ecmascript,
    ).use_tree(program)
    print(ecmascriptgen.generate())

    print("*"*30+"Kotlin"+"*"*30)
    kotlingen = GeneratorFactory.create(
        language=Language.kotlin,
    ).use_tree(program)
    print(kotlingen.generate())

    print("*" * 30 + "KotlinIDL" + "*" * 30)
    kotlingen = GeneratorFactory.create(
        language=Language.kotlinIDL,
        add_visitor=True,
        add_listener=True,
        add_decoder=True,
    ).use_tree(program)
    print(kotlingen.generate())
    print(kotlingen.generate_listener())
    print(kotlingen.generate_visitor())

    print("*" * 30 + "JavaIDL" + "*" * 30)
    javagen = GeneratorFactory.create(
        language=Language.javaIDL
    )
    javagen.use_tree(program)
    print(javagen.generate())

    print("*" * 30 + "JavaIDL DECODER" + "*" * 30)
    print(javagen.generate_decoder())
