# Stubs for antlr4.ParserInterpreter (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from antlr4.Parser import Parser

class ParserInterpreter(Parser):
    grammarFileName = ...  # type: Any
    atn = ...  # type: Any
    tokenNames = ...  # type: Any
    ruleNames = ...  # type: Any
    decisionToDFA = ...  # type: Any
    sharedContextCache = ...  # type: Any
    pushRecursionContextStates = ...  # type: Any
    def __init__(self, grammarFileName, tokenNames, ruleNames, atn, input) -> None: ...
    state = ...  # type: Any
    def parse(self, startRuleIndex): ...
    def enterRecursionRule(self, localctx, state, ruleIndex, precedence): ...
    def getATNState(self): ...
    def visitState(self, p): ...
    def visitRuleStopState(self, p): ...
