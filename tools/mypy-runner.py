from mypy import api
import glob
from aule.config import BASE_DIR,ROOT_DIR

opts = [
    "--python-version", "3.6",
    "--ignore-missing-imports",
    "--follow-imports", "skip"
]
exclude = [
    "generated",
    "resources",
    "__pycache__"
]

include = [
    "tools"
]

excluded_files = set([BASE_DIR + "/" + postfix for postfix in exclude])
included_files = set([ROOT_DIR + "/" + postfix for postfix in include])
all_files = set(glob.glob(BASE_DIR + "/*"))
target_files = (all_files - excluded_files) | included_files
cmd = opts + list(target_files)
print("Command: mypy {}".format(" ".join(cmd)))
result = api.run(cmd)

if result[0]:
    print("\nType checking report:\n")
    print(result[0])  # stdout

if result[1]:
    print("\nError report:\n")
    print(result[1])  # stderr

print("\nExit status:", result[2])