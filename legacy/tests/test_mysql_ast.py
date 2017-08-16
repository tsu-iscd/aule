import os
import tests.utils as utils
import jsonpickle
from .context import ASTParserFactory
from .context import GRAMMARS_PATH
from aule.generated.sqlAST import *

ast_parser = ASTParserFactory.create("mysql", is_validating=True)


def te1st_mysql_ast_smoke():
    """ MYSQL AST smoke test. """
    script = ast_parser.parse("select 1")
    assert isinstance(script, Script)
    body = script.bodyStatements
    assert len(body) == 1
    stmt = body[0]
    assert isinstance(stmt, SelectStatement)
    assert stmt.where is None
    assert stmt.fromClause is None
    assert stmt.groupBy is None
    assert stmt.orderByElems is None
    assert stmt.having is None
    assert stmt.limitLines is None
    assert stmt.limitOffset is None
    assert stmt.export is None
    columns = stmt.columns
    column = columns[0]
    assert len(columns) == 1
    assert isinstance(column, ColumnClause)
    assert column.alias is None
    assert isinstance(column.value, NumberLiteral)
    assert column.value.value == "1"


def test_mysql_ast_syntax():
    """ mysql grammar full tests. """
    path = GRAMMARS_PATH + "/mysql/examples/"
    files = os.listdir(path)
    for file in files:
        fname = path + file
        # check only files
        if os.path.isfile(fname):
            tests = utils.get_tests(fname, "#begin", "#end")
            for query in tests:
                script = ast_parser.parse(query)
                if not script:
                    print("File: " + file)
                    print("SQL Query: \n" + query)
                    assert False


def test_mysql_special_functions():
    query = """ select convert('abc' using utf8) as cc,
                convert(12.1, decimal(5,2)) as c,
                cast(-5 as signed integer) as ccc,
                position(left('abcd', 3) in 'abcdef') as cccc"""
    script = ast_parser.parse(query)
    assert isinstance(script, Script)
    body = script.bodyStatements
    assert len(body) == 1
    stmt = body[0]
    assert isinstance(stmt, SelectStatement)
    assert len(stmt.columns) == 4
    assert stmt.limitLines is None
    assert stmt.limitOffset is None
    assert stmt.where is None
    assert stmt.having is None
    assert stmt.fromClause is None
    assert stmt.groupBy is None
    assert stmt.orderByElems is None
    assert stmt.export is None
    ## FirstColumn start
    col = stmt.columns[0]
    assert isinstance(col, ColumnClause)
    assert isinstance(col.alias, Identifier)
    assert col.alias.name.lower() == "cc"
    colValue = col.value
    assert isinstance(colValue, ExtArgFunctionCall)
    assert colValue.name.lower() == "convert"
    assert len(colValue.arguments) == 2
    arg = colValue.arguments[0]
    assert isinstance(arg, FuncExtExprArgument)
    assert arg.keyword is None
    assert arg.keywordPosition is None
    assert arg.separator is None
    assert isinstance(arg.value, StringLiteral)
    assert arg.value.value.lower() == "abc"
    arg = colValue.arguments[1]
    assert isinstance(arg, FuncExtCharsetArgument)
    assert arg.keyword.lower() == "using"
    assert arg.keywordPosition.lower() == "before"
    assert arg.separator is None
    assert isinstance(arg.value, CharSet)
    assert arg.value.name.lower() == "utf8"
    ## FirstColumn end
    ## SecondColumn start
    col = stmt.columns[1]
    assert isinstance(col, ColumnClause)
    assert isinstance(col.alias, Identifier)
    assert col.alias.name.lower() == "c"
    colValue = col.value
    assert isinstance(colValue, ExtArgFunctionCall)
    assert colValue.name.lower() == "convert"
    assert len(colValue.arguments) == 2
    arg = colValue.arguments[0]
    assert isinstance(arg, FuncExtExprArgument)
    assert arg.keyword is None
    assert arg.keywordPosition is None
    assert arg.separator is None
    assert isinstance(arg.value, RealLiteral)
    assert arg.value.value == "12.1"
    arg = colValue.arguments[1]
    assert isinstance(arg, FuncExtDataTypeArgument)
    assert arg.keyword is None
    assert arg.keywordPosition is None
    assert arg.separator == ","
    assert isinstance(arg.value, ConvertedDataType)
    assert arg.value.dataType.lower() == "decimal"
    ## SecondColumn end
    ## ThirdColumn start
    col = stmt.columns[2]
    assert isinstance(col, ColumnClause)
    assert isinstance(col.alias, Identifier)
    assert col.alias.name.lower() == "ccc"
    colValue = col.value
    assert isinstance(colValue, ExtArgFunctionCall)
    assert colValue.name.lower() == "cast"
    assert len(colValue.arguments) == 2
    arg = colValue.arguments[0]
    assert isinstance(arg, FuncExtExprArgument)
    assert arg.keyword is None
    assert arg.keywordPosition is None
    assert arg.separator is None
    argval = arg.value
    assert isinstance(argval, UnaryExpression)
    assert argval.operation == "-"
    assert isinstance(argval.value, NumberLiteral)
    assert argval.value.value == "5"
    arg = colValue.arguments[1]
    assert isinstance(arg, FuncExtDataTypeArgument)
    assert arg.keyword.lower() == "as"
    assert arg.keywordPosition.lower() == "before"
    assert arg.separator is None
    argval = arg.value
    assert isinstance(argval, ConvertedDataType)
    assert argval.firstDim is None
    assert argval.secondDim is None
    assert argval.dataType.lower() == "signed"
    assert argval.charSet is None
    ## ThirdColumn end
    ## FourthColumn start
    col = stmt.columns[3]
    assert isinstance(col, ColumnClause)
    assert isinstance(col.alias, Identifier)
    assert col.alias.name.lower() == "cccc"
    colValue = col.value
    assert isinstance(colValue, ExtArgFunctionCall)
    assert colValue.name.lower() == "position"
    assert len(colValue.arguments) == 2
    arg = colValue.arguments[0]
    assert isinstance(arg, FuncExtExprArgument)
    assert arg.keyword is None
    assert arg.keywordPosition is None
    assert arg.separator is None
    argval = arg.value
    assert isinstance(argval, SimpleFunctionCall)
    assert argval.name.lower() == "left"
    assert len(argval.arguments) == 2
    assert isinstance(argval.arguments[0], StringLiteral)
    assert argval.arguments[0].value.lower() == "abcd"
    assert isinstance(argval.arguments[1], NumberLiteral)
    assert argval.arguments[1].value == "3"
    arg = colValue.arguments[1]
    assert isinstance(arg, FuncExtExprArgument)
    assert arg.keyword.lower() == "in"
    assert arg.keywordPosition.lower() == "before"
    assert arg.separator is None
    assert isinstance(arg.value, StringLiteral)
    assert arg.value.value == "abcdef"
    ## FourthColumn end


def test_mysql_ext_special_function():
    query = """ select trim('  abc ') as c,
                trim('ff' from 'ffabcabcff') as cc,
                trim(leading 'aaa' from 'aaaaaabcdb') as ccc,
                substring(substring('abcdefgad' from 2 for sqrt(16)) from 1+2) as cccc"""
    script = ast_parser.parse(query)
    assert isinstance(script, Script)
    body = script.bodyStatements
    assert len(body) == 1
    stmt = body[0]
    assert isinstance(stmt, SelectStatement)
    assert len(stmt.columns) == 4
    assert stmt.limitLines is None
    assert stmt.limitOffset is None
    assert stmt.where is None
    assert stmt.having is None
    assert stmt.fromClause is None
    assert stmt.groupBy is None
    assert stmt.orderByElems is None
    assert stmt.export is None
    ## FirstColumn start
    col = stmt.columns[0]
    assert isinstance(col, ColumnClause)
    assert isinstance(col.alias, Identifier)
    assert col.alias.name.lower() == "c"
    colValue = col.value
    assert isinstance(colValue, SimpleFunctionCall)
    assert colValue.name.lower() == "trim"
    assert len(colValue.arguments) == 1
    arg = colValue.arguments[0]
    assert isinstance(arg, StringLiteral)
    assert arg.value.lower() == "  abc "
    ## FirstColumn end
    ## SecondColumn start
    col = stmt.columns[1]
    assert isinstance(col, ColumnClause)
    assert isinstance(col.alias, Identifier)
    assert col.alias.name.lower() == "cc"
    colValue = col.value
    assert isinstance(colValue, ExtArgFunctionCall)
    assert colValue.name.lower() == "trim"
    assert len(colValue.arguments) == 2
    arg = colValue.arguments[0]
    assert isinstance(arg, FuncExtExprArgument)
    assert arg.keyword is None
    assert arg.keywordPosition is None
    assert arg.separator is None
    assert isinstance(arg.value, StringLiteral)
    assert arg.value.value.lower() == "ff"
    arg = colValue.arguments[1]
    assert isinstance(arg, FuncExtExprArgument)
    assert arg.keyword.lower() == "from"
    assert arg.keywordPosition.lower() == "before"
    assert arg.separator is None
    assert isinstance(arg.value, StringLiteral)
    assert arg.value.value.lower() == "ffabcabcff"
    ## SecondColumn end
    ## ThirdColumn start
    col = stmt.columns[2]
    assert isinstance(col, ColumnClause)
    assert isinstance(col.alias, Identifier)
    assert col.alias.name.lower() == "ccc"
    colValue = col.value
    assert isinstance(colValue, ExtArgFunctionCall)
    assert colValue.name.lower() == "trim"
    assert len(colValue.arguments) == 3
    arg = colValue.arguments[0]
    assert isinstance(arg, FuncExtKeywordArgument)
    assert arg.keyword.lower() == "leading"
    assert arg.separator is None
    arg = colValue.arguments[1]
    assert isinstance(arg, FuncExtExprArgument)
    assert arg.keyword is None
    assert arg.keywordPosition is None
    assert arg.separator is None
    assert isinstance(arg.value, StringLiteral)
    assert arg.value.value.lower() == "aaa"
    arg = colValue.arguments[2]
    assert isinstance(arg, FuncExtExprArgument)
    assert arg.keyword.lower() == "from"
    assert arg.keywordPosition.lower() == "before"
    assert arg.separator is None
    assert isinstance(arg.value, StringLiteral)
    assert arg.value.value.lower() == "aaaaaabcdb"
    ## ThirdColumn end
    ## FourthColumn start
    col = stmt.columns[3]
    assert isinstance(col, ColumnClause)
    assert isinstance(col.alias, Identifier)
    assert col.alias.name.lower() == "cccc"
    colValue = col.value
    assert isinstance(colValue, ExtArgFunctionCall)
    assert colValue.name.lower() == "substring"
    assert len(colValue.arguments) == 2
    arg = colValue.arguments[0]
    assert isinstance(arg, FuncExtExprArgument)
    assert arg.keyword is None
    assert arg.keywordPosition is None
    assert arg.separator is None
    assert isinstance(arg.value, ExtArgFunctionCall)
    assert len(arg.value.arguments) == 3
    assert arg.value.name.lower() == "substring"
    subarg = arg.value.arguments[0]
    assert isinstance(subarg, FuncExtExprArgument)
    assert subarg.keyword is None
    assert subarg.keywordPosition is None
    assert subarg.separator is None
    assert isinstance(subarg.value, StringLiteral)
    assert subarg.value.value.lower() == "abcdefgad"
    subarg = arg.value.arguments[1]
    assert isinstance(subarg, FuncExtExprArgument)
    assert subarg.keyword.lower() == "from"
    assert subarg.keywordPosition.lower() == "before"
    assert subarg.separator is None
    assert isinstance(subarg.value, NumberLiteral)
    assert subarg.value.value.lower() == "2"
    subarg = arg.value.arguments[2]
    assert isinstance(subarg, FuncExtExprArgument)
    assert subarg.keyword.lower() == "for"
    assert subarg.keywordPosition.lower() == "before"
    assert subarg.separator is None
    assert isinstance(subarg.value, SimpleFunctionCall)
    assert subarg.value.name.lower() == "sqrt"
    assert len(subarg.value.arguments) == 1
    subarg_l2 = subarg.value.arguments[0]
    assert isinstance(subarg_l2, NumberLiteral)
    assert subarg_l2.value == "16"
    arg = colValue.arguments[1]
    assert isinstance(arg, FuncExtExprArgument)
    assert arg.keyword.lower() == "from"
    assert arg.keywordPosition.lower() == "before"
    assert arg.separator is None
    assert isinstance(arg.value, BinaryExpression)
    assert arg.value.operation == "+"
    subarg = arg.value.leftArg
    assert isinstance(subarg, NumberLiteral)
    assert subarg.value == "1"
    subarg = arg.value.rightArg
    assert isinstance(subarg, NumberLiteral)
    assert subarg.value == "2"
    ## FourthColumn end


def test_mysql_simple_sleect():
    query = r""" select *,
                sqrt(a) AS col1,
                lower(substring(str from 'a' for length(str)/2)) as col3,
                concat('abc', 'def', 'ghij') as col4 from tab1 where a is not \N"""
    script = ast_parser.parse(query)
    assert isinstance(script, Script)
    body = script.bodyStatements
    assert len(body) == 1
    stmt = body[0]
    assert isinstance(stmt, SelectStatement)
    assert len(stmt.columns) == 4
    assert stmt.limitLines is None
    assert stmt.limitOffset is None
    assert stmt.having is None
    assert stmt.groupBy is None
    assert stmt.orderByElems is None
    assert stmt.export is None
    ## FirstColumn start
    col = stmt.columns[0]
    assert isinstance(col, ColumnClause)
    assert col.alias is None
    colValue = col.value
    assert isinstance(colValue, ColumnName)
    assert colValue.table is None
    assert colValue.schema is None
    assert isinstance(colValue.column, Star)

    ## FirstColumn end
    ## SecondColumn start
    col = stmt.columns[1]
    assert isinstance(col, ColumnClause)
    assert isinstance(col.alias, Identifier)
    assert col.alias.name.lower() == "col1"
    colValue = col.value
    assert isinstance(colValue, SimpleFunctionCall)
    assert colValue.name.lower() == "sqrt"
    assert len(colValue.arguments) == 1
    arg = colValue.arguments[0]
    assert isinstance(arg, ColumnName)
    assert arg.table is None
    assert arg.schema is None
    assert isinstance(arg.column, Identifier)
    assert arg.column.name.lower() == "a"
    ## SecondColumn end
    ## ThirdColumn start
    col = stmt.columns[2]
    assert isinstance(col, ColumnClause)
    assert isinstance(col.alias, Identifier)
    assert col.alias.name.lower() == "col3"
    colValue = col.value
    assert isinstance(colValue, SimpleFunctionCall)
    assert colValue.name.lower() == "lower"
    assert len(colValue.arguments) == 1
    arg = colValue.arguments[0]
    assert isinstance(arg, ExtArgFunctionCall)
    assert arg.name.lower() == "substring"
    assert len(arg.arguments) == 3
    subarg = arg.arguments[0]
    assert isinstance(subarg, FuncExtExprArgument)
    assert subarg.keyword is None
    assert subarg.keywordPosition is None
    assert subarg.separator is None
    assert isinstance(subarg.value, ColumnName)
    assert subarg.value.table is None
    assert subarg.value.schema is None
    assert isinstance(subarg.value.column, Identifier)
    assert subarg.value.column.name.lower() == "str"
    subarg = arg.arguments[1]
    assert isinstance(subarg, FuncExtExprArgument)
    assert subarg.keyword.lower() == "from"
    assert subarg.keywordPosition.lower() == "before"
    assert subarg.separator is None
    assert isinstance(subarg.value, StringLiteral)
    assert subarg.value.value.lower() == "a"
    subarg = arg.arguments[2]
    assert isinstance(subarg, FuncExtExprArgument)
    assert subarg.keyword.lower() == "for"
    assert subarg.keywordPosition.lower() == "before"
    assert subarg.separator is None
    subargValue = subarg.value
    assert isinstance(subargValue, BinaryExpression)
    assert subargValue.operation == "/"
    assert isinstance(subargValue.leftArg, SimpleFunctionCall)
    assert subargValue.leftArg.name.lower() == "length"
    assert len(subargValue.leftArg.arguments) == 1
    subarg_l2 = subargValue.leftArg.arguments[0]
    assert isinstance(subarg_l2, ColumnName)
    assert subarg_l2.table is None
    assert subarg_l2.schema is None
    assert isinstance(subarg_l2.column,  Identifier)
    assert subarg_l2.column.name.lower() == "str"
    assert isinstance(subargValue.rightArg, NumberLiteral)
    assert subargValue.rightArg.value == "2"
    ## ThirdColumn end
    ## FourthColumn start
    col = stmt.columns[3]
    assert isinstance(col, ColumnClause)
    assert isinstance(col.alias, Identifier)
    assert col.alias.name.lower() == "col4"
    colValue = col.value
    assert isinstance(colValue, SimpleFunctionCall)
    assert colValue.name.lower() == "concat"
    assert len(colValue.arguments) == 3
    arg = colValue.arguments[0]
    assert isinstance(arg, StringLiteral)
    assert arg.value.lower() == "abc"
    arg = colValue.arguments[1]
    assert isinstance(arg, StringLiteral)
    assert arg.value.lower() == "def"
    arg = colValue.arguments[2]
    assert isinstance(arg, StringLiteral)
    assert arg.value.lower() == "ghij"
    ## FourthColumn end
    ## From_clause start
    fromCl = stmt.fromClause
    assert isinstance(fromCl, FromClause)
    assert len(fromCl.tableRefs) == 1
    tblRef = fromCl.tableRefs[0]
    assert isinstance(tblRef, TableSource)
    assert tblRef.alias is None
    assert tblRef.indexHints is None
    assert tblRef.partitions is None
    assert isinstance(tblRef.name, TableName)
    assert tblRef.name.schema is None
    assert isinstance(tblRef.name.table, Identifier)
    assert tblRef.name.table.name.lower() == "tab1"
    ## From_clause end
    ## where_definition start
    whereDef = stmt.where
    assert isinstance(whereDef, WhereClause)
    whereVal = whereDef.value
    assert isinstance(whereVal, IsNullPredicate)
    assert whereVal.isNot is True
    val = whereVal.value
    assert isinstance(val, ColumnName)
    assert val.schema is None
    assert val.table is None
    assert isinstance(val.column, Identifier)
    assert val.column.name.lower() == "a"
    ## where_definition end


def test_mysql_weight_string_function():
    query = """ select weight_string(substring('abcdbedd' from 3 for 4) as binary(2) level 1 asc, 2, 3) as col """
    script = ast_parser.parse(query)
    assert isinstance(script, Script)
    body = script.bodyStatements
    assert len(body) == 1
    stmt = body[0]
    assert isinstance(stmt, SelectStatement)
    assert len(stmt.columns) == 1
    assert stmt.limitLines is None
    assert stmt.limitOffset is None
    assert stmt.where is None
    assert stmt.having is None
    assert stmt.fromClause is None
    assert stmt.groupBy is None
    assert stmt.orderByElems is None
    assert stmt.export is None
    ## FirstColumn start
    col = stmt.columns[0]
    assert isinstance(col, ColumnClause)
    assert isinstance(col.alias, Identifier)
    assert col.alias.name.lower() == "col"
    colValue = col.value
    assert isinstance(colValue, ExtArgFunctionCall)
    assert colValue.name.lower() == "weight_string"
    assert len(colValue.arguments) == 3
    arg = colValue.arguments[0]
    assert isinstance(arg, FuncExtExprArgument)
    assert arg.keyword is None
    assert arg.keywordPosition is None
    assert arg.separator is None
    assert isinstance(arg.value, ExtArgFunctionCall)
    assert arg.value.name.lower() == "substring"
    assert len(arg.value.arguments) == 3
    subarg = arg.value.arguments[0]
    assert isinstance(subarg, FuncExtExprArgument)
    assert subarg.keyword is None
    assert subarg.keywordPosition is None
    assert subarg.separator is None
    assert isinstance(subarg.value, StringLiteral)
    assert subarg.value.value.lower() == "abcdbedd"
    subarg = arg.value.arguments[1]
    assert isinstance(subarg, FuncExtExprArgument)
    assert subarg.keyword.lower() == "from"
    assert subarg.keywordPosition.lower() == "before"
    assert subarg.separator is None
    assert isinstance(subarg.value, NumberLiteral)
    assert subarg.value.value == "3"
    subarg = arg.value.arguments[2]
    assert isinstance(subarg, FuncExtExprArgument)
    assert subarg.keyword.lower() == "for"
    assert subarg.keywordPosition.lower() == "before"
    assert subarg.separator is None
    assert isinstance(subarg.value, NumberLiteral)
    assert subarg.value.value == "4"
    arg = colValue.arguments[1]
    assert isinstance(arg, FuncExtExprArgument)
    assert arg.keyword.lower() == "as binary"
    assert arg.keywordPosition.lower() == "before"
    assert arg.separator is None
    assert isinstance(arg.value, NumberLiteral)
    assert arg.value.value == "2"
    arg = colValue.arguments[2]
    assert isinstance(arg, FuncExtNestedArgument)
    assert arg.keyword.lower() == "level"
    assert arg.keywordPosition.lower() == "before"
    assert len(arg.values) == 3
    subarg = arg.values[0]
    assert isinstance(subarg, FuncExtExprArgument)
    assert subarg.keyword.lower() == "asc"
    assert subarg.keywordPosition.lower() == "after"
    assert subarg.value == "1"
    assert subarg.separator is None
    subarg = arg.values[1]
    assert isinstance(subarg, FuncExtExprArgument)
    assert subarg.keyword is None
    assert subarg.keywordPosition is None
    assert subarg.value == "2"
    assert subarg.separator == ","
    subarg = arg.values[2]
    assert isinstance(subarg, FuncExtExprArgument)
    assert subarg.keyword is None
    assert subarg.keywordPosition is None
    assert subarg.value == "3"
    assert subarg.separator == ","
    ## FirstColumn end


def test_mysql_table_based_create():
    script = ast_parser.parse("create temporary table t1 like t2")
    assert isinstance(script, Script)
    body = script.bodyStatements
    assert len(body) == 1
    stmt = body[0]
    assert isinstance(stmt, CreateTableCopyStatement)
    assert stmt.ifNotExist is False
    assert stmt.isTemporary is True
    tbl = stmt.table
    assert isinstance(tbl, TableName)
    assert tbl.schema is None
    assert isinstance(tbl.table, Identifier)
    assert tbl.table.name.lower() == "t1"
    tbl = stmt.tableCopy
    assert isinstance(tbl, TableName)
    assert tbl.schema is None
    assert isinstance(tbl.table, Identifier)
    assert tbl.table.name.lower() == "t2"


def test_mysql_create_table_by_column():
    query = """ create temporary table t1(
                    c1 char(1) comment 'comment 1' storage memory default 'a' column_format fixed unique key comment 'comment 2' key column_format dynamic
                )"""
    script = ast_parser.parse(query)
    assert isinstance(script, Script)
    assert len(script.bodyStatements) == 1
    stmt = script.bodyStatements[0]
    assert isinstance(stmt, CreateTableColumnStatement)
    assert stmt.ifNotExist is False
    assert stmt.isTemporary is True
    assert stmt.constraints == []
    sql_options = stmt.optionSet
    assert isinstance(sql_options, TableOptionSet)
    for next_atr in dir(sql_options):
        if callable(getattr(sql_options, next_atr)) == True:
            continue
        if next_atr[0] == "_":
            continue
        if next_atr in ["type"]:
            continue
        assert getattr(sql_options, next_atr) is None
    tbl = stmt.table
    assert isinstance(tbl, TableName)
    assert tbl.schema is None
    assert isinstance(tbl.table, Identifier)
    assert tbl.table.name.lower() == "t1"
    assert len(stmt.columns) == 1
    col = stmt.columns[0]
    assert isinstance(col, ColumnDefClause)
    assert col.comment.lower() == "comment 2"
    assert col.storage.lower() == "memory"
    assert col.columnFormat.lower() == "dynamic"
    assert col.isAutoIncrement is False
    assert col.isUnique is True
    assert col.isNotNull is False
    assert col.isPrimary is True
    assert col.refDef is None
    assert isinstance(col.defaultValue, StringLiteral)
    assert col.defaultValue.value.lower() == "a"
    assert isinstance(col.name, Identifier)
    assert col.name.name.lower() == "c1"
    datatype = col.dataType
    assert isinstance(datatype, CharDataTypeClause)
    assert datatype.typeName.lower() == "char"
    assert datatype.length == "1"
    assert datatype.collationName is None
    assert datatype.isBinary is None
    assert datatype.charSetName is None


def test_mysql_create_with_spec_datatype():
    query = """ create table tt(
                    c1 varchar(200) not null, `1e2` decimal(5, 3) unique,
                    list set('one', 'two', 'five', 'ten', 'hundred') character set cp866
                )"""
    script = ast_parser.parse(query)
    assert isinstance(script, Script)
    assert len(script.bodyStatements) == 1
    stmt = script.bodyStatements[0]
    assert isinstance(stmt, CreateTableColumnStatement)
    assert stmt.ifNotExist is False
    assert stmt.isTemporary is False
    assert stmt.constraints == []
    sql_options = stmt.optionSet
    assert isinstance(sql_options, TableOptionSet)
    for next_atr in dir(sql_options):
        if callable(getattr(sql_options, next_atr)) == True:
            continue
        if next_atr[0] == "_":
            continue
        if next_atr in ["type"]:
            continue
        assert getattr(sql_options, next_atr) is None
    tbl = stmt.table
    assert isinstance(tbl, TableName)
    assert tbl.schema is None
    assert isinstance(tbl.table, Identifier)
    assert tbl.table.name.lower() == "tt"
    assert len(stmt.columns) == 3
    col = stmt.columns[0]
    assert isinstance(col, ColumnDefClause)
    assert col.comment is None
    assert col.storage is None
    assert col.columnFormat is None
    assert col.defaultValue is None
    assert col.isAutoIncrement is False
    assert col.isUnique is False
    assert col.isNotNull is True
    assert col.isPrimary is False
    assert col.refDef is None
    assert isinstance(col.name, Identifier)
    assert col.name.name.lower() == "c1"
    datatype = col.dataType
    assert isinstance(datatype, CharDataTypeClause)
    assert datatype.typeName.lower() == "varchar"
    assert datatype.length == "200"
    assert datatype.collationName is None
    assert datatype.isBinary is None
    assert datatype.charSetName is None
    col = stmt.columns[1]
    assert isinstance(col, ColumnDefClause)
    assert col.comment is None
    assert col.storage is None
    assert col.columnFormat is None
    assert col.defaultValue is None
    assert col.isAutoIncrement is False
    assert col.isUnique is True
    assert col.isNotNull is False
    assert col.isPrimary is False
    assert col.refDef is None
    assert isinstance(col.name, Identifier)
    assert col.name.name.lower() == "`1e2`"
    datatype = col.dataType
    assert isinstance(datatype, DimensionDataTypeClause)
    assert datatype.typeName.lower() == "decimal"
    assert datatype.length == "5"
    assert datatype.secondLength == "3"
    assert datatype.isUnsigned is False
    assert datatype.isZerofill is False
    col = stmt.columns[2]
    assert isinstance(col, ColumnDefClause)
    assert col.comment is None
    assert col.storage is None
    assert col.columnFormat is None
    assert col.defaultValue is None
    assert col.isAutoIncrement is False
    assert col.isUnique is False
    assert col.isNotNull is False
    assert col.isPrimary is False
    assert col.refDef is None
    assert isinstance(col.name, Identifier)
    assert col.name.name.lower() == "list"
    datatype = col.dataType
    assert isinstance(datatype, CollectionCharDataTypeClause)
    assert datatype.typeName.lower() == "set"
    assert datatype.collationName is None
    assert datatype.isBinary is None
    assert isinstance(datatype.charSetName, CharSet)
    assert datatype.charSetName.name.lower() == "cp866"
    assert len(datatype.values) == 5
    val = datatype.values[0]
    assert isinstance(val, StringLiteral)
    assert val.value.lower() == "one"
    val = datatype.values[1]
    assert isinstance(val, StringLiteral)
    assert val.value.lower() == "two"
    val = datatype.values[2]
    assert isinstance(val, StringLiteral)
    assert val.value.lower() == "five"
    val = datatype.values[3]
    assert isinstance(val, StringLiteral)
    assert val.value.lower() == "ten"
    val = datatype.values[4]
    assert isinstance(val, StringLiteral)
    assert val.value.lower() == "hundred"


def test_mysql_create_table_by_columns():
    query = """ create table ttt(
                    c1 int references t2(col_for_link asc),
                    c2 varchar(10), constraint constr1 foreign key (c2(10) asc,
                    c3(200)) references t3 (col1(10), col2(200) desc)
                    on delete cascade, primary key using btree (c1)
                )
    """
    script = ast_parser.parse(query)
    assert isinstance(script, Script)
    assert len(script.bodyStatements) == 1
    stmt = script.bodyStatements[0]
    assert isinstance(stmt, CreateTableColumnStatement)
    assert stmt.ifNotExist == False
    assert stmt.isTemporary == False
    sql_options = stmt.optionSet
    assert isinstance(sql_options, TableOptionSet)
    for next_atr in dir(sql_options):
        if callable(getattr(sql_options, next_atr)) == True:
            continue
        if next_atr[0] == "_":
            continue
        if next_atr in ["type"]:
            continue
        assert getattr(sql_options, next_atr) is None
    tbl = stmt.table
    assert isinstance(tbl, TableName)
    assert tbl.schema is None
    assert isinstance(tbl.table, Identifier)
    assert tbl.table.name.lower() == "ttt"
    assert len(stmt.columns) == 2
    col = stmt.columns[0]
    assert isinstance(col, ColumnDefClause)
    assert col.comment is None
    assert col.storage is None
    assert col.columnFormat is None
    assert col.defaultValue is None
    assert col.isAutoIncrement is False
    assert col.isUnique is False
    assert col.isNotNull is False
    assert col.isPrimary is False
    assert isinstance(col.name, Identifier)
    assert col.name.name.lower() == "c1"
    datatype = col.dataType
    assert isinstance(datatype, DimensionDataTypeClause)
    assert datatype.typeName.lower() == "int"
    assert datatype.length is None
    assert datatype.secondLength is None
    assert datatype.isUnsigned is False
    assert datatype.isZerofill is False
    refdef = col.refDef
    assert isinstance(refdef, ReferenceDefClause)
    assert refdef.onDelete is None
    assert refdef.onUpdate is None
    assert refdef.matchType is None
    tbl = refdef.table
    assert isinstance(tbl, TableName)
    assert tbl.schema is None
    assert isinstance(tbl.table, Identifier)
    assert tbl.table.name.lower() == "t2"
    assert len(refdef.indexColumns) == 1
    iCol = refdef.indexColumns[0]
    assert isinstance(iCol, IndexColNameClause)
    assert iCol.length is None
    assert iCol.sortType.lower() == "asc"
    assert isinstance(iCol.columnName, Identifier)
    assert iCol.columnName.name.lower() == "col_for_link"
    col = stmt.columns[1]
    assert isinstance(col, ColumnDefClause)
    assert col.comment is None
    assert col.storage is None
    assert col.columnFormat is None
    assert col.defaultValue is None
    assert col.isAutoIncrement is False
    assert col.isUnique is False
    assert col.isNotNull is False
    assert col.isPrimary is False
    assert isinstance(col.name, Identifier)
    assert col.name.name.lower() == "c2"
    datatype = col.dataType
    assert isinstance(datatype, CharDataTypeClause)
    assert datatype.typeName.lower() == "varchar"
    assert datatype.length == "10"
    assert datatype.collationName is None
    assert datatype.isBinary is None
    assert datatype.charSetName is None
    assert len(stmt.constraints) == 2
    ## start constraints
    constr = stmt.constraints[0]
    assert isinstance(constr, ConstraintKeyClause)
    assert constr.keyType.lower() == "foreign"
    assert constr.indexName is None
    assert constr.indexType is None
    assert isinstance(constr.name, Identifier)
    assert constr.name.name.lower() == "constr1"
    assert constr.indexOptionSet is None
    assert len(constr.indexColumns) == 2
    iCol = constr.indexColumns[0]
    assert isinstance(iCol, IndexColNameClause)
    assert iCol.length == 10
    assert iCol.sortType.lower() == "asc"
    assert isinstance(iCol.columnName, Identifier)
    assert iCol.columnName.name.lower() == "c2"
    iCol = constr.indexColumns[1]
    assert isinstance(iCol, IndexColNameClause)
    assert iCol.length == 200
    assert iCol.sortType is None
    assert isinstance(iCol.columnName, Identifier)
    assert iCol.columnName.name.lower() == "c3"
    refdef = constr.refDef
    assert isinstance(refdef, ReferenceDefClause)
    assert refdef.onDelete.lower() == "cascade"
    assert refdef.onUpdate is None
    assert refdef.matchType is None
    tbl = refdef.table
    assert isinstance(tbl, TableName)
    assert tbl.schema is None
    assert isinstance(tbl.table, Identifier)
    assert tbl.table.name.lower() == "t3"
    assert len(refdef.indexColumns) == 2
    iCol = refdef.indexColumns[0]
    assert isinstance(iCol, IndexColNameClause)
    assert iCol.length == 10
    assert iCol.sortType is None
    assert isinstance(iCol.columnName, Identifier)
    assert iCol.columnName.name.lower() == "col1"
    iCol = refdef.indexColumns[1]
    assert isinstance(iCol, IndexColNameClause)
    assert iCol.length == 200
    assert iCol.sortType.lower() == "desc"
    assert isinstance(iCol.columnName, Identifier)
    assert iCol.columnName.name.lower() == "col2"
    constr = stmt.constraints[1]
    assert isinstance(constr, ConstraintKeyClause)
    assert constr.keyType.lower() == "primary"
    assert constr.name is None
    assert constr.indexName is None
    assert constr.indexType.lower() == "btree"
    assert constr.refDef is None
    iOpt = constr.indexOptionSet
    assert isinstance(iOpt, IndexOptionSet)
    assert iOpt.comment is None
    assert iOpt.indexType is None
    assert iOpt.parser is None
    assert iOpt.keyBlockSize is None
    assert len(constr.indexColumns) == 1
    iCol = constr.indexColumns[0]
    assert isinstance(iCol, IndexColNameClause)
    assert iCol.length is None
    assert iCol.sortType is None
    assert isinstance(iCol.columnName, Identifier)
    assert iCol.columnName.name.lower() == "c1"
    ## end constraints


def test_mysql_create_based_on_query():
    query = """ create table tt (
                    col1 varchar(200) not null,
                    1d2 decimal(5,3) unique, 111ee enum('one', 'two', 'three')
                ) select * from t1
    """
    script = ast_parser.parse(query)
    assert isinstance(script, Script)
    assert len(script.bodyStatements) == 1
    stmt = script.bodyStatements[0]
    assert isinstance(stmt, CreateTableQueryStatement)
    assert stmt.ifNotExist is False
    assert stmt.isTemporary is False
    assert stmt.constraints == []
    sql_options = stmt.optionSet
    assert isinstance(sql_options, TableOptionSet)
    for next_atr in dir(sql_options):
        if callable(getattr(sql_options, next_atr)) == True:
            continue
        if next_atr[0] == "_":
            continue
        if next_atr in ["type"]:
            continue
        assert getattr(sql_options, next_atr) is None
    tbl = stmt.table
    assert isinstance(tbl, TableName)
    assert tbl.schema is None
    assert isinstance(tbl.table, Identifier)
    assert tbl.table.name.lower() == "tt"
    ## start ColumnDefinitions in create
    assert len(stmt.columns) == 3
    col = stmt.columns[0]
    assert isinstance(col, ColumnDefClause)
    assert col.comment is None
    assert col.storage is None
    assert col.columnFormat is None
    assert col.defaultValue is None
    assert col.isAutoIncrement is False
    assert col.isUnique is False
    assert col.isNotNull is True
    assert col.isPrimary is False
    assert col.refDef is None
    assert isinstance(col.name, Identifier)
    assert col.name.name.lower() == "col1"
    datatype = col.dataType
    assert isinstance(datatype, CharDataTypeClause)
    assert datatype.typeName.lower() == "varchar"
    assert datatype.length == "200"
    assert datatype.collationName is None
    assert datatype.isBinary is None
    assert datatype.charSetName is None
    col = stmt.columns[1]
    assert isinstance(col, ColumnDefClause)
    assert col.comment is None
    assert col.storage is None
    assert col.columnFormat is None
    assert col.defaultValue is None
    assert col.isAutoIncrement is False
    assert col.isUnique is True
    assert col.isNotNull is False
    assert col.isPrimary is False
    assert col.refDef is None
    assert isinstance(col.name, Identifier)
    assert col.name.name.lower() == "1d2"
    datatype = col.dataType
    assert isinstance(datatype, DimensionDataTypeClause)
    assert datatype.typeName.lower() == "decimal"
    assert datatype.length == "5"
    assert datatype.secondLength == "3"
    assert datatype.isUnsigned is False
    assert datatype.isZerofill is False
    col = stmt.columns[2]
    assert isinstance(col, ColumnDefClause)
    assert col.comment is None
    assert col.storage is None
    assert col.columnFormat is None
    assert col.defaultValue is None
    assert col.isAutoIncrement is False
    assert col.isUnique is False
    assert col.isNotNull is False
    assert col.isPrimary is False
    assert col.refDef is None
    assert isinstance(col.name, Identifier)
    assert col.name.name.lower() == "111ee"
    datatype = col.dataType
    assert isinstance(datatype, CollectionCharDataTypeClause)
    assert datatype.typeName.lower() == "enum"
    assert datatype.collationName is None
    assert datatype.isBinary is None
    assert datatype.charSetName is None
    assert len(datatype.values) == 3
    val = datatype.values[0]
    assert isinstance(val, StringLiteral)
    assert val.value.lower() == "one"
    val = datatype.values[1]
    assert isinstance(val, StringLiteral)
    assert val.value.lower() == "two"
    val = datatype.values[2]
    assert isinstance(val, StringLiteral)
    assert val.value.lower() == "three"
    ## end ColumnDefinitions in create
    stmt_l2 = stmt.query
    assert isinstance(stmt_l2, SelectStatement)
    assert stmt_l2.where is None
    assert stmt_l2.having is None
    assert stmt_l2.export is None
    assert stmt_l2.groupBy is None
    assert stmt_l2.orderByElems is None
    assert stmt_l2.limitLines is None
    assert stmt_l2.limitOffset is None
    assert len(stmt_l2.columns) == 1
    col = stmt_l2.columns[0]
    assert isinstance(col, ColumnClause)
    assert col.alias is None
    colValue = col.value
    assert isinstance(colValue, ColumnName)
    assert colValue.schema is None
    assert colValue.table is None
    assert isinstance(colValue.column, Star)

    fromCl = stmt_l2.fromClause
    assert isinstance(fromCl, FromClause)
    assert len(fromCl.tableRefs) == 1
    tblRef = fromCl.tableRefs[0]
    assert isinstance(tblRef, TableSource)
    assert tblRef.alias is None
    assert tblRef.indexHints is None
    assert tblRef.partitions is None
    tbl = tblRef.name
    assert isinstance(tbl, TableName)
    assert tbl.schema is None
    assert isinstance(tbl.table, Identifier)
    assert tbl.table.name.lower() == "t1"


def test_mysql_insert():
    script = ast_parser.parse("insert into t (col1, col2, col3) values (1, 2, 3), (3, sqrt(2), 3 + 3);")
    assert isinstance(script, Script)
    assert len(script.bodyStatements) == 1
    stmt = script.bodyStatements[0]
    assert isinstance(stmt, InsertRowStatement)
    assert stmt.priority is None
    assert stmt.onDuplicateKey is None
    assert stmt.isIgnore is False
    tbl = stmt.table
    assert isinstance(tbl, TableName)
    assert tbl.schema is None
    assert isinstance(tbl.table, Identifier)
    assert tbl.table.name.lower() == "t"
    assert len(stmt.columns) == 3
    col = stmt.columns[0]
    assert isinstance(col, ColumnName)
    assert col.schema is None
    assert col.table is None
    assert isinstance(col.column, Identifier)
    assert col.column.name.lower() == "col1"
    col = stmt.columns[1]
    assert isinstance(col, ColumnName)
    assert col.schema is None
    assert col.table is None
    assert isinstance(col.column, Identifier)
    assert col.column.name.lower() == "col2"
    col = stmt.columns[2]
    assert isinstance(col, ColumnName)
    assert col.schema is None
    assert col.table is None
    assert isinstance(col.column, Identifier)
    assert col.column.name.lower() == "col3"
    assert len(stmt.rows) == 2
    row = stmt.rows[0]
    assert isinstance(row, InsertRowClause)
    assert len(row.values) == 3
    rowVal = row.values[0]
    assert isinstance(rowVal, NumberLiteral)
    assert rowVal.value == "1"
    rowVal = row.values[1]
    assert isinstance(rowVal, NumberLiteral)
    assert rowVal.value == "2"
    rowVal = row.values[2]
    assert isinstance(rowVal, NumberLiteral)
    assert rowVal.value == "3"
    row = stmt.rows[1]
    assert isinstance(row, InsertRowClause)
    assert len(row.values) == 3
    rowVal = row.values[0]
    assert isinstance(rowVal, NumberLiteral)
    assert rowVal.value == "3"
    rowVal = row.values[1]
    assert isinstance(rowVal, SimpleFunctionCall)
    assert rowVal.name.lower() == "sqrt"
    assert len(rowVal.arguments) == 1
    arg = rowVal.arguments[0]
    assert isinstance(arg, NumberLiteral)
    assert arg.value == "2"
    rowVal = row.values[2]
    assert isinstance(rowVal, BinaryExpression)
    assert rowVal.operation == "+"
    expr = rowVal.leftArg
    assert isinstance(expr, NumberLiteral)
    assert expr.value == "3"
    expr = rowVal.rightArg
    assert isinstance(expr, NumberLiteral)
    assert expr.value == "3"


def test_mysql_insert_set():
    script = ast_parser.parse("insert ignore t set col1=default, col2=1+1, col3 = abs(3*3-5+(sqrt(4*8)+pi()));")
    assert isinstance(script, Script)
    assert len(script.bodyStatements) == 1
    stmt = script.bodyStatements[0]
    assert isinstance(stmt, InsertSetStatement)
    assert stmt.priority is None
    assert stmt.onDuplicateKey is None
    assert stmt.isIgnore is True
    tbl = stmt.table
    assert isinstance(tbl, TableName)
    assert tbl.schema is None
    assert isinstance(tbl.table, Identifier)
    assert tbl.table.name.lower() == "t"
    assert len(stmt.columns) == 3
    col = stmt.columns[0]
    assert isinstance(col, ColumnName)
    assert col.schema is None
    assert col.table is None
    assert isinstance(col.column, Identifier)
    assert col.column.name.lower() == "col1"
    col = stmt.columns[1]
    assert isinstance(col, ColumnName)
    assert col.schema is None
    assert col.table is None
    assert isinstance(col.column, Identifier)
    assert col.column.name.lower() == "col2"
    col = stmt.columns[2]
    assert isinstance(col, ColumnName)
    assert col.schema is None
    assert col.table is None
    assert isinstance(col.column, Identifier)
    assert col.column.name.lower() == "col3"
    assert len(stmt.expressions) == 3
    expr = stmt.expressions[0]
    assert isinstance(expr, KeywordPrimitive)
    assert expr.keyword.lower() == "default"
    expr = stmt.expressions[1]
    assert isinstance(expr, BinaryExpression)
    assert expr.operation == "+"
    expr_l2 = expr.leftArg
    assert isinstance(expr_l2, NumberLiteral)
    assert expr_l2.value == "1"
    expr_l2 = expr.rightArg
    assert isinstance(expr_l2, NumberLiteral)
    assert expr_l2.value == "1"
    expr = stmt.expressions[2]
    assert isinstance(expr, SimpleFunctionCall)
    assert expr.name.lower() == "abs"
    assert len(expr.arguments) == 1
    arg = expr.arguments[0]
    assert isinstance(arg, BinaryExpression)
    assert arg.operation == "+"
    expr_l2 = arg.leftArg
    assert isinstance(expr_l2, BinaryExpression)
    assert expr_l2.operation == "-"
    expr_l3 = expr_l2.leftArg
    assert isinstance(expr_l3, BinaryExpression)
    assert expr_l3.operation == "*"
    expr_l4 = expr_l3.leftArg
    assert isinstance(expr_l4, NumberLiteral)
    assert expr_l4.value == "3"
    expr_l4 = expr_l3.rightArg
    assert isinstance(expr_l4, NumberLiteral)
    assert expr_l4.value == "3"
    expr_l3 = expr_l2.rightArg
    assert isinstance(expr_l3, NumberLiteral)
    assert expr_l3.value == "5"
    expr_l2 = arg.rightArg
    assert isinstance(expr_l2, ParenthesisExpression)
    expr_l3 = expr_l2.value
    assert isinstance(expr_l3, BinaryExpression)
    assert expr_l3.operation == "+"
    expr_l4 = expr_l3.leftArg
    assert isinstance(expr_l4, SimpleFunctionCall)
    assert expr_l4.name.lower() == "sqrt"
    assert len(expr_l4.arguments) == 1
    arg_l2 = expr_l4.arguments[0]
    assert isinstance(arg_l2, BinaryExpression)
    assert arg_l2.operation == "*"
    expr_l5 = arg_l2.leftArg
    assert isinstance(expr_l5, NumberLiteral)
    assert expr_l5.value == "4"
    expr_l5 = arg_l2.rightArg
    assert isinstance(expr_l5, NumberLiteral)
    assert expr_l5.value == "8"
    expr_l4 = expr_l3.rightArg
    assert isinstance(expr_l4, SimpleFunctionCall)
    assert expr_l4.name.lower() == "pi"
    assert expr_l4.arguments is None


def test_mysql_insert_based_on_query():
    script = ast_parser.parse("insert delayed ignore into t select *, 1+b*2 from tt where b is not null;")
    assert isinstance(script, Script)
    body = script.bodyStatements
    assert len(body) == 1
    stmt = body[0]
    assert isinstance(stmt, InsertQueryStatement)
    assert stmt.isIgnore is True
    assert stmt.priority.lower() == "delayed"
    assert stmt.onDuplicateKey is None
    assert stmt.columns == []
    tbl = stmt.table
    assert isinstance(tbl, TableName)
    assert tbl.schema is None
    assert isinstance(tbl.table, Identifier)
    assert tbl.table.name.lower() == "t"
    stmt_l2 = stmt.query
    assert isinstance(stmt_l2, SelectStatement)
    assert stmt_l2.having is None
    assert stmt_l2.groupBy is None
    assert stmt_l2.orderByElems is None
    assert stmt_l2.limitLines is None
    assert stmt_l2.limitOffset is None
    assert stmt_l2.export is None
    assert len(stmt_l2.columns) == 2
    ## start columns in internal SELECT
    col = stmt_l2.columns[0]
    assert isinstance(col, ColumnClause)
    assert col.alias is None
    colValue = col.value
    assert isinstance(colValue, ColumnName)
    assert colValue.schema is None
    assert colValue.table is None
    assert isinstance(colValue.column, Star)

    col = stmt_l2.columns[1]
    assert isinstance(col, ColumnClause)
    assert col.alias is None
    colValue = col.value
    assert isinstance(colValue, BinaryExpression)
    assert colValue.operation == "*"
    expr = colValue.leftArg
    assert isinstance(expr, BinaryExpression)
    assert expr.operation == "+"
    expr_l2 = expr.leftArg
    assert isinstance(expr_l2, NumberLiteral)
    assert expr_l2.value == "1"
    expr_l2 = expr.rightArg
    assert isinstance(expr_l2, ColumnName)
    assert expr_l2.schema is None
    assert expr_l2.table is None
    assert isinstance(expr_l2.column, Identifier)
    assert expr_l2.column.name.lower() == "b"
    expr = colValue.rightArg
    assert isinstance(expr, NumberLiteral)
    assert expr.value == "2"
    ## end columns in internal SELECT
    fromCl = stmt_l2.fromClause
    assert isinstance(fromCl, FromClause)
    assert len(fromCl.tableRefs) == 1
    tblref = fromCl.tableRefs[0]
    assert isinstance(tblref, TableSource)
    assert tblref.indexHints is None
    assert tblref.partitions is None
    assert tblref.alias is None
    tbl = tblref.name
    assert isinstance(tbl, TableName)
    assert tbl.schema is None
    assert isinstance(tbl.table, Identifier)
    assert tbl.table.name.lower() == "tt"
    whereDef = stmt_l2.where
    assert isinstance(whereDef, WhereClause)
    whereVal = whereDef.value
    assert isinstance(whereVal, IsNullPredicate)
    assert whereVal.isNot is True
    expr = whereVal.value
    assert isinstance(expr, ColumnName)
    assert expr.schema is None
    assert expr.table is None
    assert isinstance(expr.column, Identifier)
    assert expr.column.name.lower() == "b"


def test_mysql_insert_with_duplicate_keys():
    query = """ insert delayed ignore t values (1, 2, 3),
                (3, sqrt(2), 3 + 3) on duplicate key
                update col1 = 1 + 1, col2 = col5 + VALUES(col3);
            """
    script = ast_parser.parse(query)
    assert isinstance(script, Script)
    body = script.bodyStatements
    assert len(body) == 1
    stmt = body[0]
    assert isinstance(stmt, InsertRowStatement)
    assert stmt.isIgnore is True
    assert stmt.priority.lower() == "delayed"
    assert stmt.columns == []
    tbl = stmt.table
    assert isinstance(tbl, TableName)
    assert tbl.schema is None
    assert isinstance(tbl.table, Identifier)
    assert tbl.table.name.lower() == "t"
    assert len(stmt.rows) == 2
    row = stmt.rows[0]
    assert isinstance(row, InsertRowClause)
    assert len(row.values) == 3
    rowVal = row.values[0]
    assert isinstance(rowVal, NumberLiteral)
    assert rowVal.value == "1"
    rowVal = row.values[1]
    assert isinstance(rowVal, NumberLiteral)
    assert rowVal.value == "2"
    rowVal = row.values[2]
    assert isinstance(rowVal, NumberLiteral)
    assert rowVal.value == "3"
    row = stmt.rows[1]
    assert isinstance(row, InsertRowClause)
    assert len(row.values) == 3
    rowVal = row.values[0]
    assert isinstance(rowVal, NumberLiteral)
    assert rowVal.value == "3"
    rowVal = row.values[1]
    assert isinstance(rowVal, SimpleFunctionCall)
    assert rowVal.name.lower() == "sqrt"
    assert len(rowVal.arguments) == 1
    arg = rowVal.arguments[0]
    assert isinstance(arg, NumberLiteral)
    assert arg.value == "2"
    rowVal = row.values[2]
    assert isinstance(rowVal, BinaryExpression)
    assert rowVal.operation == "+"
    expr = rowVal.leftArg
    assert isinstance(expr, NumberLiteral)
    assert expr.value == "3"
    expr = rowVal.rightArg
    assert isinstance(expr, NumberLiteral)
    assert expr.value == "3"
    onduplkey = stmt.onDuplicateKey
    assert isinstance(onduplkey, OnDuplicateKeyClause)
    assert len(onduplkey.values) == 2
    assert len(onduplkey.columns) == 2
    expr = onduplkey.values[0]
    assert isinstance(expr, BinaryExpression)
    assert expr.operation == "+"
    expr_l2 = expr.leftArg
    assert isinstance(expr_l2, NumberLiteral)
    assert expr_l2.value == "1"
    expr_l2 = expr.rightArg
    assert isinstance(expr_l2, NumberLiteral)
    assert expr_l2.value == "1"
    expr = onduplkey.values[1]
    assert isinstance(expr, BinaryExpression)
    assert expr.operation == "+"
    expr_l2 = expr.leftArg
    assert isinstance(expr_l2, ColumnName)
    assert expr_l2.schema is None
    assert expr_l2.table is None
    assert isinstance(expr_l2.column, Identifier)
    assert expr_l2.column.name.lower() == "col5"
    expr_l2 = expr.rightArg
    assert isinstance(expr_l2, SimpleFunctionCall)
    assert expr_l2.name.lower() == "values"
    assert len(expr_l2.arguments) == 1
    arg = expr_l2.arguments[0]
    assert isinstance(arg, ColumnName)
    assert arg.schema is None
    assert arg.table is None
    assert isinstance(arg.column, Identifier)
    assert arg.column.name.lower() == "col3"
    col = onduplkey.columns[0]
    assert isinstance(col, ColumnName)
    assert col.schema is None
    assert col.table is None
    assert isinstance(col.column, Identifier)
    assert col.column.name.lower() == "col1"
    col = onduplkey.columns[1]
    assert isinstance(col, ColumnName)
    assert col.schema is None
    assert col.table is None
    assert isinstance(col.column, Identifier)
    assert col.column.name.lower() == "col2"


def test_mysql_update_single_table():
    query = """ update ignore ttt set somecol = DEFAULT,
                cccc = c1 - c2,
                cc = ifnull(asdfds,100)
                where col1 is not null and col1 + col2 > somecol
                order by sort_col1 asc, substring(colsorttext, 2, length(colsorttext)/2) desc limit 5;"""
    script = ast_parser.parse(query)
    assert isinstance(script, Script)
    body = script.bodyStatements
    assert len(body) == 1
    stmt = body[0]
    assert isinstance(stmt, UpdateSingleStatement)
    assert stmt.isIgnore is True
    assert stmt.priority is None
    assert stmt.limit == "5"
    assert len(stmt.orderByElems) == 2
    assert len(stmt.values) == 3
    assert len(stmt.columns) == 3
    col = stmt.columns[0]
    assert isinstance(col, ColumnName)
    assert col.schema is None
    assert col.table is None
    assert isinstance(col.column, Identifier)
    assert col.column.name.lower() == "somecol"
    col = stmt.columns[1]
    assert isinstance(col, ColumnName)
    assert col.schema is None
    assert col.table is None
    assert isinstance(col.column, Identifier)
    assert col.column.name.lower() == "cccc"
    col = stmt.columns[2]
    assert isinstance(col, ColumnName)
    assert col.schema is None
    assert col.table is None
    assert isinstance(col.column, Identifier)
    assert col.column.name.lower() == "cc"
    expr = stmt.values[0]
    assert isinstance(expr, KeywordPrimitive)
    assert expr.keyword.lower() == "default"
    expr = stmt.values[1]
    assert isinstance(expr, BinaryExpression)
    assert expr.operation == "-"
    expr_l2 = expr.leftArg
    assert isinstance(expr_l2, ColumnName)
    assert expr_l2.schema is None
    assert expr_l2.table is None
    assert isinstance(expr_l2.column, Identifier)
    assert expr_l2.column.name.lower() == "c1"
    expr_l2 = expr.rightArg
    assert isinstance(expr_l2, ColumnName)
    assert expr_l2.schema is None
    assert expr_l2.table is None
    assert isinstance(expr_l2.column, Identifier)
    assert expr_l2.column.name.lower() == "c2"
    expr = stmt.values[2]
    assert isinstance(expr, SimpleFunctionCall)
    assert expr.name.lower() == "ifnull"
    assert len(expr.arguments) == 2
    arg = expr.arguments[0]
    assert isinstance(arg, ColumnName)
    assert arg.schema is None
    assert arg.table is None
    assert isinstance(arg.column, Identifier)
    assert arg.column.name.lower() == "asdfds"
    arg = expr.arguments[1]
    assert isinstance(arg, NumberLiteral)
    assert arg.value == "100"
    tblsrc = stmt.source
    assert isinstance(tblsrc, TableSource)
    assert tblsrc.alias is None
    assert tblsrc.indexHints is None
    assert tblsrc.partitions is None
    tbl = tblsrc.name
    assert isinstance(tbl, TableName)
    assert tbl.schema is None
    assert isinstance(tbl.table, Identifier)
    assert tbl.table.name.lower() == "ttt"
    whereDef = stmt.where
    assert isinstance(whereDef, WhereClause)
    whereVal = whereDef.value
    assert isinstance(whereVal, LogicalExpression)
    assert whereVal.operator.lower() == "and"
    assert whereVal.isUnary is False
    expr = whereVal.leftArg
    assert isinstance(expr, IsNullPredicate)
    assert expr.isNot is True
    expr_l2 = expr.value
    assert isinstance(expr_l2, ColumnName)
    assert expr_l2.schema is None
    assert expr_l2.table is None
    assert isinstance(expr_l2.column, Identifier)
    assert expr_l2.column.name.lower() == "col1"
    expr = whereVal.rightArg
    assert isinstance(expr, ComparisonPredicate)
    assert expr.comparisonOperator == ">"
    expr_l2 = expr.leftArg
    assert isinstance(expr_l2, BinaryExpression)
    assert expr_l2.operation == "+"
    expr_l3 = expr_l2.leftArg
    assert isinstance(expr_l3, ColumnName)
    assert expr_l3.schema is None
    assert expr_l3.table is None
    assert isinstance(expr_l3.column, Identifier)
    assert expr_l3.column.name.lower() == "col1"
    expr_l3 = expr_l2.rightArg
    assert isinstance(expr_l3, ColumnName)
    assert expr_l3.schema is None
    assert expr_l3.table is None
    assert isinstance(expr_l3.column, Identifier)
    assert expr_l3.column.name.lower() == "col2"
    expr_l2 = expr.rightArg
    assert isinstance(expr_l2, ColumnName)
    assert expr_l2.schema is None
    assert expr_l2.table is None
    assert isinstance(expr_l2.column, Identifier)
    assert expr_l2.column.name.lower() == "somecol"
    orderby = stmt.orderByElems[0]
    assert isinstance(orderby, SortItem)
    assert orderby.sortType.lower() == "asc"
    expr = orderby.expression
    assert isinstance(expr, ColumnName)
    assert expr.schema is None
    assert expr.table is None
    assert isinstance(expr.column, Identifier)
    assert expr.column.name.lower() == "sort_col1"
    orderby = stmt.orderByElems[1]
    assert isinstance(orderby, SortItem)
    assert orderby.sortType.lower() == "desc"
    expr = orderby.expression
    assert isinstance(expr, SimpleFunctionCall)
    assert expr.name.lower() == "substring"
    assert len(expr.arguments) == 3
    arg = expr.arguments[0]
    assert isinstance(arg, ColumnName)
    assert arg.schema is None
    assert arg.table is None
    assert isinstance(arg.column, Identifier)
    assert arg.column.name.lower() == "colsorttext"
    arg = expr.arguments[1]
    assert isinstance(arg, NumberLiteral)
    assert arg.value == "2"
    arg = expr.arguments[2]
    assert isinstance(arg, BinaryExpression)
    assert arg.operation == "/"
    expr_l2 = arg.leftArg
    assert isinstance(expr_l2, SimpleFunctionCall)
    assert expr_l2.name.lower() == "length"
    assert len(expr_l2.arguments) == 1
    arg_l2 = expr_l2.arguments[0]
    assert isinstance(arg_l2, ColumnName)
    assert arg_l2.schema is None
    assert arg_l2.table is None
    assert isinstance(arg_l2.column, Identifier)
    assert arg_l2.column.name.lower() == "colsorttext"
    expr_l2 = arg.rightArg
    assert isinstance(expr_l2, NumberLiteral)
    assert expr_l2.value == "2"


def test_mysql_delete_single_table():
    query = """ delete quick ignore from tbl_name
                where somecol is null and substring(left('this is test mysql string', 5)
                from sqrt(3) for 10-5*1.5 * (11*11 - 21)) in ('one', 'two', concat_ws(' ', 'one', 'two', 'three'))
                order by sortcol desc limit 10; """
    script = ast_parser.parse(query)
    assert isinstance(script, Script)
    body = script.bodyStatements
    assert len(body) == 1
    stmt = body[0]
    assert isinstance(stmt, DeleteSingleStatement)
    assert stmt.isIgnore is True
    assert stmt.priority is None
    assert stmt.isQuick == True
    assert stmt.limit == 10
    tbl = stmt.table
    assert isinstance(tbl, TableName)
    assert tbl.schema is None
    assert isinstance(tbl.table, Identifier)
    assert tbl.table.name.lower() == "tbl_name"
    whereDef = stmt.where
    assert isinstance(whereDef, WhereClause)
    whereVal = whereDef.value
    assert isinstance(whereVal, LogicalExpression)
    assert whereVal.isUnary is False
    assert whereVal.operator.lower() == "and"
    expr = whereVal.leftArg
    assert isinstance(expr, IsNullPredicate)
    assert expr.isNot is False
    assert isinstance(expr.value, ColumnName)
    assert expr.value.schema is None
    assert expr.value.table is None
    assert isinstance(expr.value.column, Identifier)
    assert expr.value.column.name.lower() == "somecol"
    expr = whereVal.rightArg
    assert isinstance(expr, InPredicate)
    assert expr.subquery is None
    assert expr.isNot is False
    assert expr.isSubquery is False
    ## start value in InPredicate
    expr_l2 = expr.comparableValue
    assert isinstance(expr_l2, ExtArgFunctionCall)
    assert expr_l2.name.lower() == "substring"
    assert len(expr_l2.arguments) == 3
    arg = expr_l2.arguments[0]
    assert isinstance(arg, FuncExtExprArgument)
    assert arg.keyword is None
    assert arg.keywordPosition is None
    assert arg.separator is None
    assert isinstance(arg.value, SimpleFunctionCall)
    assert arg.value.name.lower() == "left"
    assert len(arg.value.arguments) == 2
    subarg = arg.value.arguments[0]
    assert isinstance(subarg, StringLiteral)
    assert subarg.value.lower() == "this is test mysql string"
    subarg = arg.value.arguments[1]
    assert isinstance(subarg, NumberLiteral)
    assert subarg.value == "5"
    arg = expr_l2.arguments[1]
    assert isinstance(arg, FuncExtExprArgument)
    assert arg.keyword.lower() == "from"
    assert arg.keywordPosition.lower() == "before"
    assert arg.separator is None
    assert isinstance(arg.value, SimpleFunctionCall)
    assert arg.value.name.lower() == "sqrt"
    assert len(arg.value.arguments) == 1
    subarg = arg.value.arguments[0]
    assert isinstance(subarg, NumberLiteral)
    assert subarg.value == "3"
    arg = expr_l2.arguments[2]
    assert isinstance(arg, FuncExtExprArgument)
    assert arg.keyword.lower() == "for"
    assert arg.keywordPosition.lower() == "before"
    assert arg.separator is None
    assert isinstance(arg.value, BinaryExpression)
    assert arg.value.operation == "*"
    expr_l3 = arg.value.leftArg
    assert isinstance(expr_l3, BinaryExpression)
    assert expr_l3.operation == "*"
    expr_l4 = expr_l3.leftArg
    assert isinstance(expr_l4, BinaryExpression)
    assert expr_l4.operation == "-"
    expr_l5 = expr_l4.leftArg
    assert isinstance(expr_l5, NumberLiteral)
    assert expr_l5.value == "10"
    expr_l5 = expr_l4.rightArg
    assert isinstance(expr_l5, NumberLiteral)
    assert expr_l5.value == "5"
    expr_l4 = expr_l3.rightArg
    assert isinstance(expr_l4, RealLiteral)
    assert expr_l4.value == "1.5"
    expr_l3 = arg.value.rightArg
    assert isinstance(expr_l3, ParenthesisExpression)
    assert isinstance(expr_l3.value, BinaryExpression)
    assert expr_l3.value.operation == "-"
    expr_l4 = expr_l3.value.leftArg
    assert isinstance(expr_l4, BinaryExpression)
    assert expr_l4.operation == "*"
    expr_l5 = expr_l4.leftArg
    assert isinstance(expr_l5, NumberLiteral)
    assert expr_l5.value == "11"
    expr_l5 = expr_l4.rightArg
    assert isinstance(expr_l5, NumberLiteral)
    assert expr_l5.value == "11"
    expr_l4 = expr_l3.value.rightArg
    assert isinstance(expr_l4, NumberLiteral)
    assert expr_l4.value == "21"
    ## end value in InPredicate
    ## start values in InPredicate
    assert len(expr.comparedValues) == 3
    expr_l2 = expr.comparedValues[0]
    assert isinstance(expr_l2, StringLiteral)
    assert expr_l2.value.lower() == "one"
    expr_l2 = expr.comparedValues[1]
    assert isinstance(expr_l2, StringLiteral)
    assert expr_l2.value.lower() == "two"
    expr_l2 = expr.comparedValues[2]
    assert isinstance(expr_l2, SimpleFunctionCall)
    assert expr_l2.name.lower() == "concat_ws"
    assert len(expr_l2.arguments) == 4
    arg = expr_l2.arguments[0]
    assert isinstance(arg, StringLiteral)
    assert arg.value.lower() == " "
    arg = expr_l2.arguments[1]
    assert isinstance(arg, StringLiteral)
    assert arg.value.lower() == "one"
    arg = expr_l2.arguments[2]
    assert isinstance(arg, StringLiteral)
    assert arg.value.lower() == "two"
    arg = expr_l2.arguments[3]
    assert isinstance(arg, StringLiteral)
    assert arg.value.lower() == "three"
    ## end values in InPredicate
    assert len(stmt.orderByElems) == 1
    orderby = stmt.orderByElems[0]
    assert isinstance(orderby, SortItem)
    assert orderby.sortType.lower() == "desc"
    expr = orderby.expression
    assert isinstance(expr, ColumnName)
    assert expr.schema is None
    assert expr.table is None
    assert isinstance(expr.column, Identifier)
    assert expr.column.name.lower() == "sortcol"


def test_mysql_spec_comment():
    query = "select 1 /*!, ' hello' */, 2 /*! union select 5, ' world', 10 */"
    script = ast_parser.parse(query)
    assert isinstance(script, Script)
    body = script.bodyStatements
    assert len(body) == 1
    stmt = body[0]
    assert isinstance(stmt, UnionStatement)
    # First union clause start
    union_clause = stmt.clauses[0]
    assert isinstance(union_clause, UnionClause)
    assert union_clause.unionType is None
    stmt_l2 = union_clause.statement
    assert isinstance(stmt_l2, SelectStatement)
    assert len(stmt_l2.columns) == 3
    assert stmt_l2.limitLines is None
    assert stmt_l2.limitOffset is None
    assert stmt_l2.where is None
    assert stmt_l2.having is None
    assert stmt_l2.fromClause is None
    assert stmt_l2.groupBy is None
    assert stmt_l2.orderByElems is None
    assert stmt_l2.export is None
    ## FirstColumn start
    col = stmt_l2.columns[0]
    assert isinstance(col, ColumnClause)
    assert col.alias is None
    assert isinstance(col.value, NumberLiteral)
    assert col.value.value == "1"
    ## FirstColumn end
    ## SecondColumn start
    col = stmt_l2.columns[1]
    assert isinstance(col, ColumnClause)
    assert col.alias is None
    assert isinstance(col.value, StringLiteral)
    assert col.value.value == " hello"
    ## SecondColumn end
    ## ThirdColumn start
    col = stmt_l2.columns[2]
    assert isinstance(col, ColumnClause)
    assert col.alias is None
    assert isinstance(col.value, NumberLiteral)
    assert col.value.value == "2"
    ## ThirdColumn end
    # First union clause end
    # Second union clause start
    union_clause = stmt.clauses[1]
    assert isinstance(union_clause, UnionClause)
    assert union_clause.unionType is None
    stmt_l2 = union_clause.statement
    assert isinstance(stmt_l2, SelectStatement)
    assert len(stmt_l2.columns) == 3
    assert stmt_l2.limitLines is None
    assert stmt_l2.limitOffset is None
    assert stmt_l2.where is None
    assert stmt_l2.having is None
    assert stmt_l2.fromClause is None
    assert stmt_l2.groupBy is None
    assert stmt_l2.orderByElems is None
    assert stmt_l2.export is None
    ## FirstColumn start
    col = stmt_l2.columns[0]
    assert isinstance(col, ColumnClause)
    assert col.alias is None
    assert isinstance(col.value, NumberLiteral)
    assert col.value.value == "5"
    ## FirstColumn end
    ## SecondColumn start
    col = stmt_l2.columns[1]
    assert isinstance(col, ColumnClause)
    assert col.alias is None
    assert isinstance(col.value, StringLiteral)
    assert col.value.value == " world"
    ## SecondColumn end
    ## ThirdColumn start
    col = stmt_l2.columns[2]
    assert isinstance(col, ColumnClause)
    assert col.alias is None
    assert isinstance(col.value, NumberLiteral)
    assert col.value.value == "10"
    ## ThirdColumn end
    # Second union clause end

    query = """
    select * from t 
    /*! where col = somefunc(col2) order by sortcol */; 
    insert into mytable /*!(col2, col3, col1) */ 
    values (load_file('sompath'), 'str1', 2);
"""
    script = ast_parser.parse(query)
    assert isinstance(script, Script)
    body = script.bodyStatements
    assert len(body) == 2
    # First statement start
    stmt = body[0]
    assert isinstance(stmt, SelectStatement)
    assert len(stmt.columns) == 1
    assert stmt.limitLines is None
    assert stmt.limitOffset is None
    assert stmt.having is None
    assert stmt.groupBy is None
    assert len(stmt.orderByElems) == 1
    sortcol = stmt.orderByElems[0]
    assert isinstance(sortcol, SortItem)
    assert sortcol.sortType is None
    expr = sortcol.expression
    assert isinstance(expr, ColumnName)
    assert expr.schema is None
    assert expr.table is None
    assert isinstance(expr.column, Identifier)
    assert expr.column.name.lower() == "sortcol"
    assert stmt.export is None
    ## FirstColumn start
    col = stmt.columns[0]
    assert isinstance(col, ColumnClause)
    assert col.alias is None
    colValue = col.value
    assert isinstance(colValue, ColumnName)
    assert colValue.table is None
    assert colValue.schema is None
    assert isinstance(colValue.column, Star)

    ## FirstColumn end
    ## From_clause start
    fromCl = stmt.fromClause
    assert isinstance(fromCl, FromClause)
    assert len(fromCl.tableRefs) == 1
    tblRef = fromCl.tableRefs[0]
    assert isinstance(tblRef, TableSource)
    assert tblRef.alias is None
    assert tblRef.indexHints is None
    assert tblRef.partitions is None
    assert isinstance(tblRef.name, TableName)
    assert tblRef.name.schema is None
    assert isinstance(tblRef.name.table, Identifier)
    assert tblRef.name.table.name.lower() == "t"
    ## From_clause end
    ## where_definition start
    whereDef = stmt.where
    assert isinstance(whereDef, WhereClause)
    whereVal = whereDef.value
    assert isinstance(whereVal, ComparisonPredicate)
    assert whereVal.comparisonOperator == "="
    left = whereVal.leftArg
    assert isinstance(left, ColumnName)
    assert left.schema is None
    assert left.table is None
    assert isinstance(left.column, Identifier)
    assert left.column.name.lower() == "col"
    right = whereVal.rightArg
    assert isinstance(right, UDFFunctionCall)
    assert len(right.arguments) == 1
    arg = right.arguments[0]
    assert isinstance(arg, ColumnName)
    assert arg.schema is None
    assert arg.table is None
    assert isinstance(arg.column, Identifier)
    assert arg.column.name.lower() == "col2"
    udf = right.name
    assert isinstance(udf, UDFuncName)
    assert udf.schema is None
    assert isinstance(udf.routine, Identifier)
    assert udf.routine.name.lower() == "somefunc"
    ## where_definition end
    # First statement end
    # Second statement start
    stmt = body[1]
    assert isinstance(stmt, InsertRowStatement)
    assert stmt.onDuplicateKey is None
    assert stmt.isIgnore is False
    assert stmt.priority is None
    tbl = stmt.table
    assert isinstance(tbl, TableName)
    assert tbl.schema is None
    assert isinstance(tbl.table, Identifier)
    assert tbl.table.name.lower() == "mytable"
    assert len(stmt.columns) == 3
    col = stmt.columns[0]
    assert isinstance(col, ColumnName)
    assert col.schema is None
    assert col.table is None
    assert isinstance(col.column, Identifier)
    assert col.column.name.lower() == "col2"
    col = stmt.columns[1]
    assert isinstance(col, ColumnName)
    assert col.schema is None
    assert col.table is None
    assert isinstance(col.column, Identifier)
    assert col.column.name.lower() == "col3"
    col = stmt.columns[2]
    assert isinstance(col, ColumnName)
    assert col.schema is None
    assert col.table is None
    assert isinstance(col.column, Identifier)
    assert col.column.name.lower() == "col1"
    ## rows into insert start
    assert len(stmt.rows) == 1
    row = stmt.rows[0]
    assert isinstance(row, InsertRowClause)
    assert len(row.values) == 3
    rowVal = row.values[0]
    assert isinstance(rowVal, SimpleFunctionCall)
    assert rowVal.over is None
    assert rowVal.name.lower() == "load_file"
    assert len(rowVal.arguments) == 1
    arg = rowVal.arguments[0]
    assert isinstance(arg, StringLiteral)
    assert arg.value.lower() == "sompath"
    rowVal = row.values[1]
    assert isinstance(rowVal, StringLiteral)
    assert rowVal.value.lower() == "str1"
    rowVal = row.values[2]
    assert isinstance(rowVal, NumberLiteral)
    assert rowVal.value.lower() == "2"
    ## rows into insert end
    # Second statement end


def main():
    sql = """
 SELECT * FROM topics WHERE id_author<<\!2;
"""
    script = ast_parser.parse(sql)
    print(jsonpickle.encode(script))


if __name__ == "__main__":
    main()