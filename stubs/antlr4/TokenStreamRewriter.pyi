# Stubs for antlr4.TokenStreamRewriter (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class TokenStreamRewriter:
    DEFAULT_PROGRAM_NAME = ...  # type: str
    PROGRAM_INIT_SIZE = ...  # type: int
    MIN_TOKEN_INDEX = ...  # type: int
    tokens = ...  # type: Any
    programs = ...  # type: Any
    lastRewriteTokenIndexes = ...  # type: Any
    def __init__(self, tokens) -> None: ...
    def getTokenStream(self): ...
    def rollback(self, instruction_index, program_name): ...
    def deleteProgram(self, program_name: Any = ...): ...
    def insertAfterToken(self, token, text, program_name: Any = ...): ...
    def insertAfter(self, index, text, program_name: Any = ...): ...
    def insertBeforeIndex(self, index, text): ...
    def insertBeforeToken(self, token, text, program_name: Any = ...): ...
    def insertBefore(self, program_name, index, text): ...
    def replaceIndex(self, index, text): ...
    def replaceRange(self, from_idx, to_idx, text): ...
    def replaceSingleToken(self, token, text): ...
    def replaceRangeTokens(self, from_token, to_token, text, program_name: Any = ...): ...
    def replace(self, program_name, from_idx, to_idx, text): ...
    def deleteToken(self, token): ...
    def deleteIndex(self, index): ...
    def delete(self, program_name, from_idx, to_idx): ...
    def lastRewriteTokenIndex(self, program_name: Any = ...): ...
    def setLastRewriteTokenIndex(self, program_name, i): ...
    def getProgram(self, program_name): ...
    def getText(self, program_name, interval): ...
    class RewriteOperation:
        tokens = ...  # type: Any
        index = ...  # type: Any
        text = ...  # type: Any
        instructionIndex = ...  # type: int
        def __init__(self, tokens, index, text: str = ...) -> None: ...
        def execute(self, buf): ...
    class InsertBeforeOp(RewriteOperation):
        def __init__(self, tokens, index, text: str = ...) -> None: ...
        def execute(self, buf): ...
    class ReplaceOp(RewriteOperation):
        last_index = ...  # type: Any
        def __init__(self, from_idx, to_idx, tokens, text) -> None: ...
        def execute(self, buf): ...
