import sys
from setuptools import setup, find_packages

from .aule.__metadata__ import *

if sys.version_info < (3, 6):
    sys.exit("Python < 3.6 is not supported")

setup(
    name=__title__,
    version=__version__,
    description=__description__,
    author=__author__,
    author_email=__author_email__,
    url='https://gitlab.ptsecurity.ru/dbfw/aule/',
    license="GPL",
    keywords="Parser Compiler IDL Codegen",
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        "antlr4-python3-runtime>=4.7",
        "jsonpickle==0.9.4",
        "Jinja2>=2.9.6",
        "jsl>=0.2.4"
    ],
)