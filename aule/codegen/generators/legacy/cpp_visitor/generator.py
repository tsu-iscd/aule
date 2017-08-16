import enum
from contextlib import contextmanager

from aule.codegen import ust as nodes
from . import helpers


INDENT = " " * 4
EOL = ""


class Section(enum.Enum):
    CLASS = 1
    DECLARATION = 2
    DEFINITION = 3


class CodeLine(object):
    def __init__(self, level, line):
        self.line = line
        self.level = level

    def __str__(self):
        return INDENT * self.level + self.line


class Generator(object):
    def __init__(self, program):
        self._reset_code()
        for node in program:
            if isinstance(node, nodes.ClassDeclaration):
                self.visitClassDeclaration(node)
            else:
                raise NotImplemented()

    def visitClassDeclaration(self, cls_node):
        """
        :type cls_node: ust.ClassDeclaration
        """
        with self._section(Section.CLASS):
            self._write(helpers.gen_class_header(cls_node))
            with self._block():
                for f in cls_node.fields:
                    self.visitFieldDeclaration(f)
                self.visitConstructor(cls_node.constructor, cls_node)
                for m in cls_node.methods:
                    self.visitMethodDeclaration(m, cls_node)

    def visitFieldDeclaration(self, field_node):
        """
        :type field_node: ust.FieldDeclaration
        """
        declaration = "{modifiers} {type} {name};".format(
            modifiers=helpers.gen_modifiers(field_node.modifiers),
            type=self.visitTypeReference(field_node.type),
            name=field_node.name,
        )
        self._write(declaration)

    def visitMethodDeclaration(self, method_node, cls_node):
        """
        :type method_node: ust.MethodDeclaration
        :type cls_node: ust.ClassDeclaration
        """
        if len(method_node.returns) == 0:
            ret = nodes.TypeReference(nodes.SimpleType.VOID)
        else:
            ret = method_node.returns[0]
        declaration = "{modifiers} {type} {name}({args});".format(
            modifiers=helpers.gen_modifiers(method_node.modifiers),
            type=self.visitTypeReference(ret),
            name=method_node.name,
            args=', '.join(
                self.visitArgument(arg) for arg in method_node.arguments
            )
        )
        self._write(declaration)

        with self._section(Section.DEFINITION):
            definition = "{type} {namespace}::{name}({args})".format(
                type=self.visitTypeReference(ret),
                namespace=cls_node.name,
                name=method_node.name,
                args=', '.join(
                    self.visitArgument(arg) for arg in method_node.arguments
                )
            )
            self._write(definition)
            with self._block():
                for stmt in method_node.body:
                    self._write(stmt)

    def visitConstructor(self, init_node, cls_node):
        """
        :type init_node: ust.Constructor
        :type cls_node: ust.ClassDeclaration
        """
        declaration = "{name}({args});".format(
            name=cls_node.name,
            args=', '.join(
                self.visitArgument(arg) for arg in init_node.arguments
            )
        )
        self._write(declaration)
        with self._section(Section.DEFINITION):
            definition = "{namespace}::{name}({args})".format(
                namespace=cls_node.name,
                name=cls_node.name,
                args=', '.join(
                    self.visitArgument(arg) for arg in init_node.arguments
                )
            )
            self._write(definition)
            self._write(helpers.gen_init_list(init_node))
            with self._block():
                pass

    def visitArgument(self, arg_node):
        """
        :type arg_node: ust.Argument
        """
        return "{type} {name}".format(
            type=self.visitTypeReference(arg_node.type),
            name=arg_node.name,
        )

    def visitTypeReference(self, type_node):
        """
        :type type_node: ust.TypeReference
        :rtype: str
        """
        types_map = {
            nodes.SimpleType.INTEGER: "integer",
            nodes.SimpleType.FLOAT: "double",
            nodes.SimpleType.STRING: "string",
            nodes.SimpleType.BOOLEAN: "bool",
            nodes.SimpleType.VOID: "void",
        }
        field_type = types_map.get(type_node.name, type_node.name)
        if field_type == "string":
            self.imports.add("<string>")
        if type_node.is_pointer:
            return "{}*".format(field_type)
        return "{}".format(field_type)

    def _reset_code(self):
        self.code = {}
        for s in Section:
            self.code[s] = []
        self.imports = set()
        self.indent = 0
        self._cur_section = None

    @contextmanager
    def _section(self, section):
        """
        :type section: enum Section
        """
        bckp = self._cur_section, self.indent
        self.indent = 0
        self._cur_section = section
        yield
        self._cur_section, self.indent = bckp

    @contextmanager
    def _block(self):
        self._write("{")
        self.indent += 1
        yield
        self.indent -= 1
        self._write("}")
        self._write(EOL)

    def _write(self, code, section=None):
        """
        :type code: str
        :type section: Section
        """
        if section is None:
            section = self._cur_section
        for line in code.split('\n'):
            self.code[section].append(CodeLine(self.indent, line))

    def __str__(self):
        code = ''
        for i in self.imports:
            code += "#include {}\n".format(i)
        code += '\n'
        for s in Section:
            code += '\n'.join(str(line) for line in self.code[s])
            code += '\n'
        return code
