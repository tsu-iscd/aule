import os
import sys
import argparse

from aule import ASTParserFactory
from aule.codegen import GeneratorFactory, Language

if sys.version_info < (3, 6):
    sys.exit("Python < 3.6 is not supported")

# Add arguments declaration
parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i",
                    action="store",
                    type=str,
                    required=True,
                    help="Specify input IDL file.")
parser.add_argument("--output", "-o",
                    action="store",
                    type=str,
                    required=True,
                    help="Specify output directory.")
parser.add_argument("--visitor", "-v",
                    action="store_true",
                    help="Generate a visitor.")
parser.add_argument("--listener", "-l",
                    action="store_true",
                    help="Generate a listener.")
parser.add_argument("--decoder", "-d",
                    action="store_true",
                    help="Generate a JSON decoder.")
parser.add_argument("--name", "-n",
                    action="store",
                    type=str,
                    required=True,
                    help="Specify prefix name (e.g. mysql, tsql).")
parser.add_argument("--target", "-t",
                    choices=GeneratorFactory.list_languages(),
                    action="store",
                    type=str,
                    required=True,
                    help="Specify a target language")
parser.add_argument("--package", "-p",
                    action="store",
                    type=str,
                    required=False,
                    help="Specify a package for Java or Kotlin language")


# Place arguments to variables (simplifies future refactoring)
args = parser.parse_args()
gen_visitor = args.visitor
gen_listener = args.listener
gen_decoder = args.decoder
output_dir = args.output
name = args.name
input_spec = args.input
target_lang = args.target
package = args.package

if package and target_lang not in [Language.kotlinIDL.value, Language.kotlin.value]:
    raise ValueError("Unexpected argument package")

# Get the IDL specification and try to parse it
with open(input_spec) as f:
    text = f.read()
ast_parser = ASTParserFactory.create("idl", is_validating=True)
tree = ast_parser.parse(text)

# Check for errors
errors = ast_parser.parser.get_errors()
if errors:
    for e in errors:
        print(e)
    exit(1)

# Create generator
generator = GeneratorFactory.create(
    package=package,
    language=target_lang,
    add_visitor=gen_visitor,
    add_listener=gen_listener,
)
generator.use_tree(tree)

# Prepare target directory
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Module name extensions
name_extensions = {
    "python3": ".py",
    "golang": ".go",
    "json_scheme": ".json",
    "cpp": ".h",
    "cppIDL": ".h",
    "pythonIDL": ".py",
    "lua": ".lua",
    "ecmascript": ".js",
    "kotlin": ".kt",
    "kotlinIDL": ".kt"
}

filename_extension = name_extensions.get(target_lang, "")

# Generate module name
ast_module = "{}AST".format(name)

import_line = ""
if target_lang == Language.pythonIDL.value:
    import_line = "from .{} import *\n\n".format(ast_module)

# Write the code itself
code = generator.generate()
if target_lang == Language.cppIDL.value and (gen_listener or gen_visitor):
    cls_def_idx = code.find("/* Classes definitions */")
    code = code[:cls_def_idx]\
            + ('#include "{0}Listener.h"\n'.format(ast_module) if gen_listener else '') \
            + ('#include "{0}Visitor.h"\n'.format(ast_module) if gen_visitor else '') \
            + '\n' + code[cls_def_idx:]
output_file = "{}".format(ast_module) + filename_extension
with open(os.path.join(output_dir, output_file), "w") as f:
    f.write(code)

# Write additional classes if necessary
if gen_visitor:
    code = import_line + str(generator.generate_visitor())
    output_file = "{}ASTVisitor".format(name) + filename_extension
    with open(os.path.join(output_dir, output_file), "w") as f:
        f.write(code)

if gen_listener:
    code = import_line + str(generator.generate_listener())
    output_file = "{}ASTListener".format(name) + filename_extension
    with open(os.path.join(output_dir, output_file), "w") as f:
        f.write(code)

if gen_decoder:
    code = import_line + str(generator.generate_decoder())
    output_file = "{}ASTDecoder".format(name) + filename_extension
    with open(os.path.join(output_dir, output_file), "w") as f:
        f.write(code)
