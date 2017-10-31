import enum

from aule.codegen.generators import GoGenerator
from aule.codegen.generators import SchemeGenerator
from aule.codegen.generators import CPPGenerator
from aule.codegen.generators import CPPIDLGenerator
from aule.codegen.generators import PythonGenerator
from aule.codegen.generators import PythonIDLGenerator
from aule.codegen.generators import LuaGenerator
from aule.codegen.generators import ECMAScriptGenerator
from aule.codegen.generators import KotlinGenerator
from aule.codegen.generators import KotlinIDLGenerator
from aule.codegen.generators import JavaIDLGenerator


class Language(enum.Enum):
    python3 = "python3"
    golang = "golang"
    jsonScheme = "json_scheme"
    cpp = "cpp"
    cppIDL = "cppIDL"
    pythonIDL = "pythonIDL"
    lua = "lua"
    ecmascript = "ecmascript"
    kotlin = "kotlin"
    kotlinIDL = "kotlinIDL"
    javaIDL = "javaIDL"


class GeneratorFactory(object):
    LANGUAGES = {
        Language.python3: PythonGenerator,
        Language.golang: GoGenerator,
        Language.jsonScheme: SchemeGenerator,
        Language.cpp: CPPGenerator,
        Language.cppIDL: CPPIDLGenerator,
        Language.pythonIDL: PythonIDLGenerator,
        Language.lua: LuaGenerator,
        Language.ecmascript: ECMAScriptGenerator,
        Language.kotlin: KotlinGenerator,
        Language.kotlinIDL: KotlinIDLGenerator,
        Language.javaIDL: JavaIDLGenerator
    }

    @classmethod
    def list_languages(cls):
        """
        :return: List of languages supported by generator
        :rtype: list[str]
        """
        return [lang.value for lang in cls.LANGUAGES.keys()]

    @classmethod
    def create(cls, language, **options):
        """
        Creates code generator object
        :param language: target language
        :type language: str | Language
        :param options: options passed to the generator init
        :return: generator object
        """
        if isinstance(language, str):
            try:
                language = Language(language)
            except ValueError:
                raise NotImplemented("Language is not supported")
        generator_cls = cls.LANGUAGES.get(language, None)
        if generator_cls is None:
            raise NotImplemented("Language support is paused")
        return generator_cls(**options)
