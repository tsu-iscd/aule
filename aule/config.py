import os

CODEGEN_NAME = "generated"
WALKERS_NAME = "visitors"

# Root project directory
ROOT_DIR = os.getcwd()

# Project directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Output directory where all output is generated
GRAMMARS_PATH = os.path.join(BASE_DIR, "resources", "grammars")
OUTPUT_PATH = os.path.join(BASE_DIR, CODEGEN_NAME)
OUTPUT_GRAMMARS_PATH = os.path.join(OUTPUT_PATH, "resources", "grammars")
IDL_PATH = os.path.join(BASE_DIR, "resources", "idl")

# Generated module prefix
CURRENT_DIR = os.path.basename(BASE_DIR)
GENERATED_MODULE_LOCATION = ".".join([CURRENT_DIR, CODEGEN_NAME])
VISITOR_MODULE_LOCATION = ".".join([CURRENT_DIR, WALKERS_NAME])
