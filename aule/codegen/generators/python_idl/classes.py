from collections import defaultdict

from aule.codegen.ust import *
from ..python.generator import Generator as PythonGenerator


"""
Pickler is a class that will be inherited by all nodes to give them
a possibility to unmangle names before dumping to json using jsonpickle:
"""
PICKLER_CLASS = Identifier("Pickler")
PICKLER = """
class Pickler(object):
    def __init__(*args, **kwargs):
        # We have it for compatibility reasons (all node classes has same
        # init signature)
        pass

    @classmethod
    def get_mangled(cls):
        mangled_names = {}
        for c in cls.mro():
            mangled_names.update(getattr(c, "__mangled__", {}).items())
        return mangled_names

    @classmethod
    def mangle_dict(cls, obj):
        # mangle_map is map form normal name to python mangled one.
        mangle_map = cls.get_mangled()
        for k, v in obj.items():
            if k in mangle_map:
                del obj[k]
                obj[mangle_map[k]] = v

    def __getstate__(self):
        # mangled_names is a map from python name to unmangled one.
        mangled_names = {k: v for v, k in self.get_mangled().items()}
        to_pickle = {}
        for k, v in self.__dict__.items():
            to_pickle[mangled_names.get(k,k)] = v
        return {"type": self.__class__.__name__, **to_pickle}
"""


def create_factory(classes):
    """ ASTFactory is class that's able to create AST node classes from
    the dict of its fields.

    Factory should be used to create AST nodes python dicts or json strings.

    To create AST nodes from JSON serialized data use `self.from_json(json_str)`,
    to init from  python dicts, use `self.create(obj)` method.

    Both methods look for appropriate construction method and returns its result.
    Each AST node has its own construction method `.create{NodeName}(self, obj)`.
    N.B: Construction methods for abstract classes should be overridden by the user!
    """
    create_methods = [
        MethodDeclaration(
            name=Identifier("create{}".format(cls.name)),
            arguments=[
                Argument(
                    name=Identifier("obj"),
                    type=TypeReference(PythonGenerator.OBJECT_CLASS)
                )
            ],
            returns=[TypeReference(PythonGenerator.OBJECT_CLASS)],
            body=Block([
                "return {}(**obj)".format(cls.name)
            ]),
        )
        for cls in classes
    ]
    entry_method = gen_factory_entry(classes)
    from_json = MethodDeclaration(
            name=Identifier("from_json"),
            arguments=[
                Argument(
                    name=Identifier("json_str"),
                    type=TypeReference(SimpleType.STRING)
                )
            ],
            returns=[TypeReference(PythonGenerator.OBJECT_CLASS)],
            body=Block([
                "import json",
                "return json.loads(json_str, object_hook=self.create)"
            ]),
        )
    class_node = ClassDeclaration(
        name=Identifier("ASTFactory"),
        parents=[PythonGenerator.OBJECT_CLASS],
        methods=[from_json, entry_method] + create_methods,
    )
    # Add empty body to constructor
    # noinspection PyTypeChecker
    class_node.constructor.body = Block(
        ['"""'] +
        [x.lstrip() for x in create_factory.__doc__.split('\n')[:-1]] +
        ['"""']
    )
    return class_node


def gen_factory_entry(classes):
    """ Creates MethodDeclaration for the factory entry point.
    Generated method looks like:

    def create(self, obj):
        obj_type = obj.get("type","")
        if len(obj_type) == 4:
            if obj_type == "Fart":
                Fart.mangle_dict(obj)
                return self.createFart(**obj)
            if obj_type == "Dumb":
                Dumb.mangle_dict(obj)
                return self.createDumb(**obj)

     :type classes: list[ClassDeclaration]
    """
    len_map = defaultdict(list)
    for cls in classes:
        len_map[len(str(cls.name))].append(cls)

    body = ['obj_type = obj.get("type","")']
    for l, classes in len_map.items():
        body.append('if len(obj_type) == {}'.format(l))
        ifblock = []
        for cls in classes:
            ifblock.extend([
                "if obj_type == \"{}\"".format(cls.name),
                Block([
                    "{}.mangle_dict(obj)".format(cls.name),
                    "return self.create{}(obj)".format(cls.name),
                ])
            ])
        body.append(Block(ifblock))

    return MethodDeclaration(
        name=Identifier("create"),
        arguments=[
            Argument(
                name=Identifier("obj"),
                type=TypeReference(PythonGenerator.OBJECT_CLASS)
            )
        ],
        returns=[TypeReference(PythonGenerator.OBJECT_CLASS)],
        body=Block(body)
    )


def create_listener(classes):
    """
    :type classes: list[ClassDeclaration]
    """
    methods = []
    for cls in classes:
        methods.append(gen_enter(cls.name))
        methods.append(gen_exit(cls.name))
    class_node = ClassDeclaration(
        name=Identifier("ASTListener"),
        parents=[PythonGenerator.OBJECT_CLASS],
        methods=methods
    )
    # Add empty body to constructor
    class_node.constructor.body = Block(["pass"])
    return class_node


def create_visitor(classes):
    """
    :type classes: list[ClassDeclaration]
    """
    class_node = ClassDeclaration(
        name=Identifier("ASTVisitor"),
        parents=[PythonGenerator.OBJECT_CLASS],
        methods=[
            MethodDeclaration(
                name=Identifier("visit{}".format(cls.name)),
                arguments=[
                    Argument(
                        name=Identifier("tree"),
                        type=TypeReference(PythonGenerator.OBJECT_CLASS)
                    )
                ],
                returns=[],
                body=Block(["pass"]),
            )
            for cls in classes
            ]
    )
    # Add empty body to constructor
    class_node.constructor.body = Block(["pass"])
    return class_node


def gen_enter(name):
    """
    :type name: Identifier
    :rtype MethodDeclaration
    """
    return MethodDeclaration(
        name=Identifier("enter{}".format(name)),
        arguments=[
            Argument(
                name=Identifier("ctx"),
                type=TypeReference(PythonGenerator.OBJECT_CLASS)
            )
        ],
        returns=[],
        body=Block(["pass"]),
    )


def gen_exit(name):
    """
    :type name: Identifier
    :rtype MethodDeclaration
    """
    return MethodDeclaration(
        name=Identifier("exit{}".format(name)),
        arguments=[
            Argument(
                name=Identifier("ctx"),
                type=TypeReference(PythonGenerator.OBJECT_CLASS)
            )
        ],
        returns=[],
        body=Block(["pass"]),
    )
