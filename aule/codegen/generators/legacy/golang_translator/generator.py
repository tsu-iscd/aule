import jinja2

from aule.codegen import ust

from .translator import *

TEMPLATE_DIR = "templates"
TEMPLATE_FILE = "golang_legacy.jinja2"


class Generator(object):
    def __init__(self, program):
        self.structs = []
        self.functions = []
        self.vars = []
        for node in program:
            if isinstance(node, ust.ClassDeclaration):
                self.structs.append(
                    Struct.from_node(node)
                )
            elif isinstance(node, ust.FunctionDeclaration):
                self.functions.append(node)
            elif isinstance(node, ust.VariableDeclaration):
                self.vars.append(node)

    def __str__(self):
        return jinja2.Environment(
            loader=jinja2.FileSystemLoader(TEMPLATE_DIR),
            trim_blocks=True,
            lstrip_blocks=True,
            autoescape=False,
        ).get_template(TEMPLATE_FILE).render(
            structs=self.structs,
            functions=self.functions,
            variables=self.vars,
        )
