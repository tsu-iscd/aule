# Stubs for antlr4.xpath.XPath (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from antlr4 import Lexer

def serializedATN(): ...

class XPathLexer(Lexer):
    atn = ...  # type: Any
    decisionsToDFA = ...  # type: Any
    TOKEN_REF = ...  # type: int
    RULE_REF = ...  # type: int
    ANYWHERE = ...  # type: int
    ROOT = ...  # type: int
    WILDCARD = ...  # type: int
    BANG = ...  # type: int
    ID = ...  # type: int
    STRING = ...  # type: int
    modeNames = ...  # type: Any
    literalNames = ...  # type: Any
    symbolicNames = ...  # type: Any
    ruleNames = ...  # type: Any
    grammarFileName = ...  # type: str
    def __init__(self, input: Optional[Any] = ...) -> None: ...
    def action(self, localctx, ruleIndex, actionIndex): ...
    type = ...  # type: Any
    def ID_action(self, localctx, actionIndex): ...

class XPath:
    WILDCARD = ...  # type: str
    NOT = ...  # type: str
    parser = ...  # type: Any
    path = ...  # type: Any
    elements = ...  # type: Any
    def __init__(self, parser, path) -> None: ...
    def split(self, path): ...
    def getXPathElement(self, wordToken, anywhere): ...
    @staticmethod
    def findAll(tree, xpath, parser): ...
    def evaluate(self, t): ...

class XPathElement:
    nodeName = ...  # type: Any
    invert = ...  # type: bool
    def __init__(self, nodeName) -> None: ...

class XPathRuleAnywhereElement(XPathElement):
    ruleIndex = ...  # type: Any
    def __init__(self, ruleName, ruleIndex) -> None: ...
    def evaluate(self, t): ...

class XPathRuleElement(XPathElement):
    ruleIndex = ...  # type: Any
    def __init__(self, ruleName, ruleIndex) -> None: ...
    def evaluate(self, t): ...

class XPathTokenAnywhereElement(XPathElement):
    tokenType = ...  # type: Any
    def __init__(self, ruleName, tokenType) -> None: ...
    def evaluate(self, t): ...

class XPathTokenElement(XPathElement):
    tokenType = ...  # type: Any
    def __init__(self, ruleName, tokenType) -> None: ...
    def evaluate(self, t): ...

class XPathWildcardAnywhereElement(XPathElement):
    def __init__(self) -> None: ...
    def evaluate(self, t): ...

class XPathWildcardElement(XPathElement):
    def __init__(self) -> None: ...
    def evaluate(self, t): ...
