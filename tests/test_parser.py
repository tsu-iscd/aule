from .context import ParserFactory


def test_parser():
    parser = ParserFactory.create("mysql")
    result = parser.check_syntax("SELECT 1")
    assert result

    result = parser.check_syntax("SELECT FROM")
    assert result is False


def test_errors():
    parser = ParserFactory.create("mysql", is_validating=True)
    parser.unset_validating()
    result = parser.check_syntax("SELECT FROM")
    assert result is False
    errors = parser.get_errors()
    assert errors is None

    parser = ParserFactory.create("mysql", is_validating=False)
    parser.set_validating()
    result = parser.check_syntax("SELECT FROM")
    assert result is True

    parser = ParserFactory.create("mysql", is_validating=True)
    result = parser.check_syntax("SELECT FROM")
    assert result is True
    errors = parser.get_errors()
    assert len(errors) == 1


