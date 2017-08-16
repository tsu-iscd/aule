from antlr4 import InputStream, CommonTokenStream
from .context import sqlLexer

    
def test_sqllexer():
    """ sql lexer smoke tests. """
    char_stream = InputStream("select 1")
    lexer = sqlLexer(char_stream)
    stream = CommonTokenStream(lexer)
    stream is not None
    tokens = lexer.getAllTokens()
    assert len(tokens) == 3
    assert tokens[0].text == "select"
    assert tokens[1].text == " "
    assert tokens[2].text == "1"

    char_stream = InputStream("select select select 1")
    lexer = sqlLexer(char_stream)
    stream = CommonTokenStream(lexer)
    stream is not None
    tokens = lexer.getAllTokens()
    assert len(tokens) == 7
    assert tokens[0].text == "select"
    assert tokens[1].text == " "
    assert tokens[2].text == "select"
    assert tokens[3].text == " "
    assert tokens[4].text == "select"
    assert tokens[5].text == " "
    assert tokens[6].text == "1"
    

    
    
    

