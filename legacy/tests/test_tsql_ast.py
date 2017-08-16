import os
import tests.utils as utils
from .context import ASTParserFactory
from aule.generated.sqlAST import *
import jsonpickle

ast_parser = ASTParserFactory.create("tsql")


def test_tsql_ast():
    """ T-SQL AST smoke tests. """
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


def test_tsql_special_functions_and_expressions_1():
    query = """SELECT CONVERT(NVARCHAR(32), HashBytes('MD5', 'email@dot.com'),2) AS cc,
               CAST(p.Name AS char(10)) AS c, CHARINDEX('bike', document) AS ccc,
               CAST(ROUND(SalesYTD/CommissionPCT, 0) AS int) AS cccc
            """
    script = ast_parser.parse(query)
    assert isinstance(script, Script)
    body = script.bodyStatements
    assert len(body) == 1
    stmt = body[0]
    assert isinstance(stmt, SelectStatement)
    assert len(stmt.columns) == 4
    assert stmt.limitLines is None
    assert stmt.fromClause is None
    assert stmt.limitOffset is None
    assert stmt.where is None
    assert stmt.having is None
    assert stmt.groupBy is None
    assert stmt.orderByElems is None
    assert stmt.export is None
    #  FirstColumn start
    col = stmt.columns[0]
    assert isinstance(col, ColumnClause)
    assert isinstance(col.alias, Identifier)
    assert col.alias.name.lower() == "cc"
    col_value = col.value
    assert isinstance(col_value, ExtArgFunctionCall)
    assert col_value.name.lower() == "convert"
    assert len(col_value.arguments) == 3
    arg = col_value.arguments[0]
    assert isinstance(arg, FuncExtDataTypeArgument)
    assert arg.keyword is None
    assert arg.keywordPosition is None
    assert arg.separator is None
    arg_val = arg.value
    assert arg_val.firstDim == "32"
    assert arg_val.secondDim is None
    assert arg_val.dataType.lower() == "nvarchar"
    assert arg_val.charSet is None
    arg = col_value.arguments[1]
    assert isinstance(arg, FuncExtExprArgument)
    assert arg.keyword is None
    assert arg.keywordPosition is None
    assert arg.separator == ","
    arg_val = arg.value
    assert isinstance(arg_val, SimpleFunctionCall)
    assert arg_val.over is None
    assert arg_val.name.lower() == "hashbytes"
    arg12 = arg_val.arguments[0]
    assert isinstance(arg12, StringLiteral)
    assert arg12.value == "'MD5'"
    arg12 = arg.value.arguments[1]
    assert isinstance(arg12, StringLiteral)
    assert arg12.value == "'email@dot.com'"
    arg = col_value.arguments[2]
    assert isinstance(arg, FuncExtExprArgument)
    assert arg.separator == ","
    assert arg.keywordPosition is None
    assert arg.keyword is None
    arg_val = arg.value
    assert isinstance(arg_val, NumberLiteral)
    assert arg_val.value == "2"
    #  FirstColumn end
    #  SecondColumn start
    col = stmt.columns[1]
    assert isinstance(col, ColumnClause)
    assert isinstance(col.alias, Identifier)
    assert col.alias.name.lower() == "c"
    col_value = col.value
    assert isinstance(col_value, ExtArgFunctionCall)
    assert col_value.name == "CAST"
    assert len(col_value.arguments) == 2
    arg = col_value.arguments[0]
    assert arg.keyword == "AS"
    assert arg.keywordPosition == "BEFORE"
    assert arg.separator is None
    arg_val = arg.value
    assert arg_val.firstDim == "10"
    assert arg_val.secondDim is None
    assert arg_val.dataType == "char"
    assert arg_val.charSet is None
    assert isinstance(arg_val, ConvertedDataType)
    arg = col_value.arguments[1]
    assert isinstance(arg, FuncExtExprArgument)
    assert arg.separator is None
    assert arg.keyword is None
    assert arg.keywordPosition is None
    arg_val = arg.value
    assert isinstance(arg_val, ColumnName)
    assert arg_val.schema is None
    assert arg_val.column.name == "Name"
    assert isinstance(arg_val.column, Identifier)
    assert arg_val.table.name == "p"
    assert isinstance(arg_val.table, Identifier)
    #  SecondColumn end
    #  ThirdColumn start
    col = stmt.columns[2]
    assert isinstance(col, ColumnClause)
    assert isinstance(col.alias, Identifier)
    assert col.alias.name.lower() == "ccc"
    col_value = col.value
    assert isinstance(col_value, SimpleFunctionCall)
    assert col_value.over is None
    assert col_value.name == "CHARINDEX"
    arg = col_value.arguments[0]
    assert isinstance(arg, StringLiteral)
    assert arg.value == "'bike'"
    arg = col_value.arguments[1]
    assert isinstance(arg, ColumnName)
    assert arg.table is None
    assert arg.schema is None
    assert isinstance(arg.column, Identifier)
    assert arg.column.name == "document"
    #  ThirdColumn end
    #  FourthColumn start
    col = stmt.columns[3]
    assert isinstance(col, ColumnClause)
    assert isinstance(col.alias, Identifier)
    assert col.alias.name == "cccc"
    col_value = col.value
    assert isinstance(col_value, ExtArgFunctionCall)
    assert col_value.name.lower() == "cast"
    assert len(col_value.arguments) == 2
    arg = col_value.arguments[0]
    assert isinstance(arg, FuncExtDataTypeArgument)
    assert arg.keyword == "AS"
    assert arg.keywordPosition == "BEFORE"
    assert arg.separator is None
    arg_val = arg.value
    assert arg_val.firstDim is None
    assert arg_val.secondDim is None
    assert arg_val.dataType == "int"
    assert arg_val.charSet is None
    assert isinstance(arg_val, ConvertedDataType)
    arg = col_value.arguments[1]
    assert isinstance(arg, FuncExtExprArgument)
    assert arg.separator is None
    assert arg.keywordPosition is None
    assert arg.keyword is None
    arg_val = arg.value
    assert isinstance(arg_val, SimpleFunctionCall)
    assert arg_val.name.lower() == "round"
    assert arg_val.over is None
    arg23 = arg_val.arguments[0]
    assert arg23.operation == "/"
    assert isinstance(arg23, BinaryExpression)
    assert isinstance(arg23.rightArg, ColumnName)
    assert arg23.rightArg.table is None
    assert arg23.rightArg.schema is None
    assert arg23.rightArg.column.name == "CommissionPCT"
    assert isinstance(arg23.rightArg.column, Identifier)
    assert isinstance(arg23.leftArg, ColumnName)
    assert arg23.leftArg.table is None
    assert arg23.leftArg.schema is None
    assert arg23.leftArg.column.name == "SalesYTD"
    assert isinstance(arg23.leftArg.column, Identifier)
    arg23 = arg_val.arguments[1]
    assert isinstance(arg23, NumberLiteral)
    assert arg23.value == "0"
    #  FourthColumn end


def test_tsql_special_functions_and_expressions_2():
    query = """SELECT *, SQRT(a) AS col1, CONCAT('abc', 'def', 'ghij') AS col2,
               LOWER(UPPER(SUBSTRING(Name, 1, 20))) AS col3
               FROM tab1 WHERE a IS NOT NULL
            """
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
    #  FirstColumn start
    col = stmt.columns[0]
    assert isinstance(col, ColumnClause)
    assert col.alias is None
    col_value = col.value
    assert isinstance(col_value, ColumnName)
    assert col_value.table is None
    assert col_value.schema is None
    assert isinstance(col_value.column, Star)

    #  FirstColumn end
    #  SecondColumn start
    col = stmt.columns[1]
    assert isinstance(col, ColumnClause)
    assert isinstance(col.alias, Identifier)
    assert col.alias.name.lower() == "col1"
    col_value = col.value
    assert isinstance(col_value, SimpleFunctionCall)
    assert col_value.name.lower() == "sqrt"
    assert len(col_value.arguments) == 1
    arg = col_value.arguments[0]
    assert isinstance(arg, ColumnName)
    assert arg.table is None
    assert arg.schema is None
    assert isinstance(arg.column, Identifier)
    assert arg.column.name.lower() == "a"
    #  SecondColumn end
    #  ThirdColumn start
    col = stmt.columns[2]
    assert isinstance(col, ColumnClause)
    assert isinstance(col.alias, Identifier)
    assert col.alias.name.lower() == "col2"
    col_value = col.value
    assert isinstance(col_value, SimpleFunctionCall)
    assert col_value.name.lower() == "concat"
    assert len(col_value.arguments) == 3
    arg = col_value.arguments[0]
    assert isinstance(arg, StringLiteral)
    assert arg.value.lower() == "'abc'"
    arg = col_value.arguments[1]
    assert isinstance(arg, StringLiteral)
    assert arg.value.lower() == "'def'"
    arg = col_value.arguments[2]
    assert isinstance(arg, StringLiteral)
    assert arg.value.lower() == "'ghij'"
    #  ThirdColumn end
    #  FourthColumn start
    col = stmt.columns[3]
    assert isinstance(col, ColumnClause)
    assert isinstance(col.alias, Identifier)
    assert col.alias.name.lower() == "col3"
    col_value = col.value
    assert isinstance(col_value, SimpleFunctionCall)
    assert col_value.name.lower() == "lower"
    assert len(col_value.arguments) == 1
    assert col_value.over is None
    arg = col_value.arguments[0]
    assert isinstance(arg, SimpleFunctionCall)
    assert arg.name.lower() == "upper"
    assert len(arg.arguments) == 1
    assert arg.over is None
    arg_2 = arg.arguments[0]
    assert isinstance(arg_2, SimpleFunctionCall)
    assert arg_2.name.lower() == "substring"
    assert len(arg_2.arguments) == 3
    assert arg_2.over is None
    arg_3 = arg_2.arguments[0]
    assert isinstance(arg_3, ColumnName)
    assert isinstance(arg_3.column, Identifier)
    assert arg_3.column.name == "Name"
    assert arg_3.table is None
    assert arg_3.schema is None
    arg_3 = arg_2.arguments[1]
    assert isinstance(arg_3, NumberLiteral)
    assert arg_3.value == "1"
    arg_3 = arg_2.arguments[2]
    assert isinstance(arg_3, NumberLiteral)
    assert arg_3.value == "20"
    #  FourthColumn end
    #  From_clause start
    from_clause = stmt.fromClause
    assert isinstance(from_clause, FromClause)
    assert len(from_clause.tableRefs) == 1
    tbl_ref = from_clause.tableRefs[0]
    assert isinstance(tbl_ref, TableSource)
    assert tbl_ref.alias is None
    assert tbl_ref.indexHints is None
    assert tbl_ref.partitions is None
    assert isinstance(tbl_ref.name, TableName)
    assert tbl_ref.name.schema is None
    assert isinstance(tbl_ref.name.table, Identifier)
    assert tbl_ref.name.table.name.lower() == "tab1"
    #  From_clause end
    #  where_definition start
    where_def = stmt.where
    assert isinstance(where_def, WhereClause)
    where_val = where_def.value
    assert isinstance(where_val, IsNullPredicate)
    assert where_val.isNot is True
    val = where_val.value
    assert isinstance(val, ColumnName)
    assert val.schema is None
    assert val.table is None
    assert isinstance(val.column, Identifier)
    assert val.column.name.lower() == "a"
    #  where_definition end
    # test query 2 end


def test_tsql_special_functions_and_expressions_3():
    query = """SELECT id_1, id_2, CONVERT(varchar(20),
               SUM(sale) OVER(PARTITION BY id_2 ORDER BY DATEPART(yy, modifiedDate)
               ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING ), 1) AS ccc
            """
    script = ast_parser.parse(query)
    assert isinstance(script, Script)
    body = script.bodyStatements
    assert len(body) == 1
    stmt = body[0]
    assert isinstance(stmt, SelectStatement)
    assert len(stmt.columns) == 3
    assert stmt.limitLines is None
    assert stmt.limitOffset is None
    assert stmt.having is None
    assert stmt.groupBy is None
    assert stmt.orderByElems is None
    assert stmt.export is None
    assert stmt.fromClause is None
    col = stmt.columns[0]
    assert col.alias is None
    assert isinstance(col, ColumnClause)
    col_val = col.value
    assert isinstance(col_val, ColumnName)
    assert isinstance(col_val.column, Identifier)
    assert col_val.column.name == "id_1"
    assert col_val.schema is None
    assert col_val.table is None
    col = stmt.columns[1]
    assert col.alias is None
    assert isinstance(col, ColumnClause)
    col_val = col.value
    assert isinstance(col_val, ColumnName)
    assert isinstance(col_val.column, Identifier)
    assert col_val.column.name == "id_2"
    assert col_val.schema is None
    assert col_val.table is None
    col = stmt.columns[2]
    assert isinstance(col, ColumnClause)
    assert isinstance(col.alias, Identifier)
    assert col.alias.name == "ccc"
    col_val = col.value
    assert isinstance(col_val, ExtArgFunctionCall)
    assert col_val.name.lower() == "convert"
    arg = col_val.arguments[0]
    assert arg.keyword is None
    assert arg.separator is None
    assert isinstance(arg, FuncExtDataTypeArgument)
    assert arg.keywordPosition is None
    arg_val = arg.value
    assert arg_val.firstDim == "20"
    assert arg_val.secondDim is None
    assert arg_val.dataType == "varchar"
    assert arg_val.charSet is None
    assert isinstance(arg_val, ConvertedDataType)
    arg = col_val.arguments[1]
    assert isinstance(arg, FuncExtExprArgument)
    assert arg.keyword is None
    assert arg.keywordPosition is None
    assert arg.separator == ","
    arg_val = arg.value
    assert arg_val.orderByElems is None
    assert arg_val.aggregator is None
    assert arg_val.name.lower() == "sum"
    assert arg_val.concatSeparator is None
    assert isinstance(arg_val, AggregateFunctionCall)
    arg12 = arg_val.arguments
    assert isinstance(arg12, ColumnName)
    assert arg12.column.name == "sale"
    assert isinstance(arg12.column, Identifier)
    assert arg12.table is None
    assert arg12.schema is None
    arg = col_val.arguments[2]
    assert arg.keyword is None
    assert isinstance(arg, FuncExtExprArgument)
    assert arg.separator == ","
    assert arg.keywordPosition is None
    assert isinstance(arg.value, NumberLiteral)
    assert arg.value.value == "1"
    over = arg_val.over
    assert isinstance(over, OverClause)
    order_by = over.orderByElems[0]
    assert order_by.sortType is None
    assert isinstance(order_by, SortItem)
    exp = order_by.expression
    assert isinstance(exp, ExtArgFunctionCall)
    assert exp.name.lower() == "datepart"
    arg = exp.arguments[0]
    assert isinstance(arg, FuncExtExprArgument)
    assert arg.separator is None
    assert arg.keywordPosition is None
    assert arg.keyword is None
    assert isinstance(arg.value, Identifier)
    assert arg.value.name.lower() == "yy"
    arg = exp.arguments[1]
    assert isinstance(arg, FuncExtExprArgument)
    assert arg.separator == ","
    assert arg.keywordPosition is None
    assert arg.keyword is None
    arg_val = arg.value
    assert isinstance(arg_val, ColumnName)
    assert arg_val.table is None
    assert arg_val.schema is None
    assert isinstance(arg_val.column, Identifier)
    assert arg_val.column.name == "modifiedDate"
    range_ = over.rangeElems[0]
    assert range_.keyword == "BETWEEN"
    assert range_.value == "CURRENT"
    assert range_.keywordPosition == "BEFORE"
    assert range_.separator is None
    assert isinstance(range_, FuncExtExprArgument)
    range_ = over.rangeElems[1]
    assert range_.keyword == "AND"
    assert range_.value == "ROW"
    assert range_.keywordPosition == "AFTER"
    assert range_.separator is None
    assert isinstance(range_, FuncExtExprArgument)
    range_ = over.rangeElems[2]
    assert range_.keyword == "AND"
    assert range_.value == "1"
    assert range_.keywordPosition == "BEFORE"
    assert range_.separator is None
    assert isinstance(range_, FuncExtExprArgument)
    range_ = over.rangeElems[3]
    assert range_.keyword is None
    assert range_.value == "FOLLOWING"
    assert range_.keywordPosition is None
    assert range_.separator is None
    assert isinstance(range_, FuncExtExprArgument)
    partition_by = over.partitionByElems[0]
    assert isinstance(partition_by, ColumnName)
    assert partition_by.table is None
    assert partition_by.schema is None
    assert isinstance(partition_by.column, Identifier)
    assert partition_by.column.name == "id_2"


def test_tsql_special_expressions_1():
    query = """SELECT * FROM t.c
               WHERE cost BETWEEN 12.00 AND 14.00 AND date IS NULL
            """
    script = ast_parser.parse(query)
    assert isinstance(script, Script)
    body = script.bodyStatements
    assert len(body) == 1
    stmt = body[0]
    assert isinstance(stmt, SelectStatement)
    assert len(stmt.columns) == 1
    assert stmt.limitLines is None
    assert stmt.limitOffset is None
    assert stmt.having is None
    assert stmt.groupBy is None
    assert stmt.orderByElems is None
    assert stmt.export is None
    col = stmt.columns[0]
    assert isinstance(col, ColumnClause)
    assert col.alias is None
    assert col.value.table is None
    assert col.value.schema is None
    assert isinstance(col.value.column, Star)

    #  From_clause start
    from_clause = stmt.fromClause
    assert isinstance(from_clause, FromClause)
    assert len(from_clause.tableRefs) == 1
    tbl_ref = from_clause.tableRefs[0]
    assert isinstance(tbl_ref, TableSource)
    assert tbl_ref.alias is None
    assert tbl_ref.indexHints is None
    assert tbl_ref.partitions is None
    assert isinstance(tbl_ref.name, TableName)
    assert isinstance(tbl_ref.name.schema, Identifier)
    assert tbl_ref.name.schema.name == "t"
    assert isinstance(tbl_ref.name.table, Identifier)
    assert tbl_ref.name.table.name.lower() == "c"
    #  From_clause end
    #  where_definition start
    where_def = stmt.where
    assert isinstance(where_def, WhereClause)
    where_val = where_def.value
    assert isinstance(where_val, LogicalExpression)
    assert where_val.operator == "AND"
    assert where_val.isUnary is False
    right = where_val.rightArg
    assert isinstance(right, IsNullPredicate)
    assert right.isNot is False
    assert isinstance(right.value, ColumnName)
    assert right.value.table is None
    assert right.value.schema is None
    assert isinstance(right.value.column, Identifier)
    assert right.value.column.name == "date"
    left = where_val.leftArg
    assert isinstance(left, BetweenPredicate)
    assert left.isNot is False
    right = left.rightArg
    assert isinstance(right, RealLiteral)
    assert right.value == "14.00"
    left12 = left.leftArg
    assert isinstance(left12, RealLiteral)
    assert left12.value == "12.00"
    left_val = left.value
    assert isinstance(left_val, ColumnName)
    assert left_val.table is None
    assert left_val.schema is None
    assert isinstance(left_val.column, Identifier)
    assert left_val.column.name == "cost"
    #  where_definition end


def test_tsql_special_expressions_2():
    query = "SELECT * FROM e  WHERE a < 12 AND a > 13 AND a <14 or b>15 and not b<16 or c<17 and c>18"
    script = ast_parser.parse(query)
    assert isinstance(script, Script)
    body = script.bodyStatements
    assert len(body) == 1
    stmt = body[0]
    assert isinstance(stmt, SelectStatement)
    assert len(stmt.columns) == 1
    assert stmt.limitLines is None
    assert stmt.limitOffset is None
    assert stmt.having is None
    assert stmt.groupBy is None
    assert stmt.orderByElems is None
    assert stmt.export is None
    col = stmt.columns[0]
    assert isinstance(col, ColumnClause)
    assert col.alias is None
    assert col.value.table is None
    assert col.value.schema is None
    assert isinstance(col.value.column, Star)

    #  From_clause start
    from_clause = stmt.fromClause
    assert isinstance(from_clause, FromClause)
    assert len(from_clause.tableRefs) == 1
    tbl_ref = from_clause.tableRefs[0]
    assert isinstance(tbl_ref, TableSource)
    assert tbl_ref.alias is None
    assert tbl_ref.indexHints is None
    assert tbl_ref.partitions is None
    assert isinstance(tbl_ref.name, TableName)
    assert tbl_ref.name.schema is None
    assert isinstance(tbl_ref.name.table, Identifier)
    assert tbl_ref.name.table.name.lower() == "e"
    #  From_clause end
    #  where_definition start
    where_def = stmt.where
    assert isinstance(where_def, WhereClause)
    where_val = where_def.value
    assert isinstance(where_val, LogicalExpression)
    assert where_val.isUnary is False
    assert where_val.operator == "or"
    right = where_val.rightArg
    assert isinstance(right, LogicalExpression)
    assert right.isUnary is False
    assert right.operator == "and"
    right12 = right.rightArg
    assert isinstance(right12, ComparisonPredicate)
    assert right12.comparisonOperator == ">"
    right23 = right12.rightArg
    assert isinstance(right23, NumberLiteral)
    assert right23.value == "18"
    left23 = right12.leftArg
    assert isinstance(left23, ColumnName)
    assert left23.schema is None
    assert left23.table is None
    assert isinstance(left23.column, Identifier)
    assert left23.column.name.lower() == "c"
    left12 = right.leftArg
    assert isinstance(left12, ComparisonPredicate)
    assert left12.comparisonOperator == "<"
    right23 = left12.rightArg
    assert isinstance(right23, NumberLiteral)
    assert right23.value == "17"
    left23 = left12.leftArg
    assert isinstance(left23, ColumnName)
    assert left23.schema is None
    assert left23.table is None
    assert isinstance(left23.column, Identifier)
    assert left23.column.name.lower() == "c"
    left = where_val.leftArg
    assert isinstance(left, LogicalExpression)
    assert left.operator == "or"
    assert left.isUnary is False
    right12 = left.rightArg
    assert isinstance(right12, LogicalExpression)
    assert right12.operator == "and"
    assert right12.isUnary is False
    right23 = right12.rightArg
    assert isinstance(right23, LogicalExpression)
    assert right23.operator == "NOT"
    assert right23.isUnary is True
    assert right23.rightArg is None
    left34 = right23.leftArg
    assert isinstance(left34, ComparisonPredicate)
    right45 = left34.rightArg
    assert isinstance(right45, NumberLiteral)
    assert right45.value == "16"
    left45 = left34.leftArg
    assert isinstance(left45, ColumnName)
    assert left45.table is None
    assert left45.schema is None
    assert isinstance(left45.column, Identifier)
    assert left45.column.name == "b"
    left23 = right12.leftArg
    assert isinstance(left23, ComparisonPredicate)
    assert left23.comparisonOperator == ">"
    right34 = left23.rightArg
    assert isinstance(right34, NumberLiteral)
    assert right34.value == "15"
    left34 = left23.leftArg
    assert isinstance(left34, ColumnName)
    assert left34.table is None
    assert left34.schema is None
    assert isinstance(left34.column, Identifier)
    assert left34.column.name == "b"
    left12 = left.leftArg
    assert isinstance(left12, LogicalExpression)
    assert left12.operator == "AND"
    assert left12.isUnary is False
    right23 = left12.rightArg
    assert isinstance(right23, ComparisonPredicate)
    assert right23.comparisonOperator == "<"
    right34 = right23.rightArg
    assert isinstance(right34, NumberLiteral)
    assert right34.value == "14"
    left34 = right23.leftArg
    assert isinstance(left34, ColumnName)
    assert left34.table is None
    assert left34.schema is None
    assert isinstance(left34.column, Identifier)
    assert left34.column.name == "a"
    left23 = left12.leftArg
    assert isinstance(left23, LogicalExpression)
    assert left23.operator == "AND"
    assert left23.isUnary is False
    right34 = left23.rightArg
    assert isinstance(right34, ComparisonPredicate)
    assert right34.comparisonOperator == ">"
    right45 = right34.rightArg
    assert isinstance(right45, NumberLiteral)
    assert right45.value == "13"
    left45 = right34.leftArg
    assert isinstance(left45, ColumnName)
    assert left45.table is None
    assert left45.schema is None
    assert isinstance(left45.column, Identifier)
    assert left45.column.name == "a"
    left34 = left23.leftArg
    assert isinstance(left34, ComparisonPredicate)
    assert left34.comparisonOperator == "<"
    right45 = left34.rightArg
    assert isinstance(right45, NumberLiteral)
    assert right45.value == "12"
    left45 = left34.leftArg
    assert isinstance(left45, ColumnName)
    assert left45.table is None
    assert left45.schema is None
    assert isinstance(left45.column, Identifier)
    assert left45.column.name == "a"
    #  where_definition end


def test_tsql_insert():
    query = "insert into t (col1, col2, col3) values (1, 2, 3), (3, sqrt(2), 3 + 3)"
    script = ast_parser.parse(query)
    assert isinstance(script, Script)
    assert len(script.bodyStatements) == 1
    stmt = script.bodyStatements[0]
    assert isinstance(stmt, InsertRowStatement)
    assert stmt.priority is None
    assert stmt.onDuplicateKey is None
    assert stmt.isIgnore is None
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
    row_val = row.values[0]
    assert isinstance(row_val, NumberLiteral)
    assert row_val.value == "1"
    row_val = row.values[1]
    assert isinstance(row_val, NumberLiteral)
    assert row_val.value == "2"
    row_val = row.values[2]
    assert isinstance(row_val, NumberLiteral)
    assert row_val.value == "3"
    row = stmt.rows[1]
    assert isinstance(row, InsertRowClause)
    assert len(row.values) == 3
    row_val = row.values[0]
    assert isinstance(row_val, NumberLiteral)
    assert row_val.value == "3"
    row_val = row.values[1]
    assert isinstance(row_val, SimpleFunctionCall)
    assert row_val.name.lower() == "sqrt"
    assert len(row_val.arguments) == 1
    arg = row_val.arguments[0]
    assert isinstance(arg, NumberLiteral)
    assert arg.value == "2"
    row_val = row.values[2]
    assert isinstance(row_val, BinaryExpression)
    assert row_val.operation == "+"
    expr = row_val.leftArg
    assert isinstance(expr, NumberLiteral)
    assert expr.value == "3"
    expr = row_val.rightArg
    assert isinstance(expr, NumberLiteral)
    assert expr.value == "3"


def test_tsql_insert_based_on_query():
    query = "insert into t select *, 1*b+2 from tt where b is NOT NULL"
    script = ast_parser.parse(query)
    assert isinstance(script, Script)
    assert len(script.bodyStatements) == 1
    stmt = script.bodyStatements[0]
    assert isinstance(stmt, InsertQueryStatement)
    assert stmt.isIgnore is None
    assert stmt.priority is None
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
    #  start columns in internal SELECT
    col = stmt_l2.columns[0]
    assert isinstance(col, ColumnClause)
    assert col.alias is None
    col_value = col.value
    assert isinstance(col_value, ColumnName)
    assert col_value.schema is None
    assert col_value.table is None
    assert isinstance(col_value.column, Star)

    col = stmt_l2.columns[1]
    assert isinstance(col, ColumnClause)
    assert col.alias is None
    col_value = col.value
    assert isinstance(col_value, BinaryExpression)
    assert col_value.operation == "+"
    expr = col_value.leftArg
    assert isinstance(expr, BinaryExpression)
    assert expr.operation == "*"
    expr_l2 = expr.leftArg
    assert isinstance(expr_l2, NumberLiteral)
    assert expr_l2.value == "1"
    expr_l2 = expr.rightArg
    assert isinstance(expr_l2, ColumnName)
    assert expr_l2.schema is None
    assert expr_l2.table is None
    assert isinstance(expr_l2.column, Identifier)
    assert expr_l2.column.name.lower() == "b"
    expr = col_value.rightArg
    assert isinstance(expr, NumberLiteral)
    assert expr.value == "2"
    #  end columns in internal SELECT
    #  From_clause start
    from_clause = stmt_l2.fromClause
    assert isinstance(from_clause, FromClause)
    assert len(from_clause.tableRefs) == 1
    tbl_ref = from_clause.tableRefs[0]
    assert isinstance(tbl_ref, TableSource)
    assert tbl_ref.indexHints is None
    assert tbl_ref.partitions is None
    assert tbl_ref.alias is None
    tbl = tbl_ref.name
    assert isinstance(tbl, TableName)
    assert tbl.schema is None
    assert isinstance(tbl.table, Identifier)
    assert tbl.table.name.lower() == "tt"
    #  From_clause end
    #  where_definition start
    where_def = stmt_l2.where
    assert isinstance(where_def, WhereClause)
    where_val = where_def.value
    assert isinstance(where_val, IsNullPredicate)
    assert where_val.isNot is True
    expr = where_val.value
    assert isinstance(expr, ColumnName)
    assert expr.schema is None
    assert expr.table is None
    assert isinstance(expr.column, Identifier)
    assert expr.column.name.lower() == "b"


def test_tsql_update_single_table():
    query = """UPDATE ttt SET somecol = DEFAULT,
               cccc = c1 - c2, cc = ifnull(asdfds,100)
               WHERE col1 IS NOT NULL and col1 + col2 > somecol
            """

    script = ast_parser.parse(query)
    assert isinstance(script, Script)

    body = script.bodyStatements
    assert len(body) == 1

    stmt = body[0]
    assert isinstance(stmt, UpdateSingleStatement)
    assert stmt.isIgnore is None
    assert stmt.priority is None
    assert stmt.limit is None
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

    tbl_src = stmt.source
    assert isinstance(tbl_src, TableSource)
    assert tbl_src.alias is None
    assert tbl_src.indexHints is None
    assert tbl_src.partitions is None

    tbl = tbl_src.name
    assert isinstance(tbl, TableName)
    assert tbl.schema is None
    assert isinstance(tbl.table, Identifier)
    assert tbl.table.name.lower() == "ttt"

    where_def = stmt.where
    assert isinstance(where_def, WhereClause)

    where_val = where_def.value
    assert isinstance(where_val, LogicalExpression)
    assert where_val.operator.lower() == "and"
    assert where_val.isUnary is False

    expr = where_val.leftArg
    assert isinstance(expr, IsNullPredicate)
    assert expr.isNot is True

    expr_l2 = expr.value
    assert isinstance(expr_l2, ColumnName)
    assert expr_l2.schema is None
    assert expr_l2.table is None
    assert isinstance(expr_l2.column, Identifier)
    assert expr_l2.column.name.lower() == "col1"

    expr = where_val.rightArg
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


def test_tsql_delete_single_table():
    query = "DELETE FROM s.t WHERE id IN (SELECT id2 FROM s2.t2 ORDER BY date ASC);"

    script = ast_parser.parse(query)
    assert isinstance(script, Script)

    body = script.bodyStatements
    assert len(body) == 1

    stmt = body[0]
    assert isinstance(stmt, DeleteSingleStatement)
    assert stmt.isIgnore is None
    assert stmt.priority is None
    assert stmt.isQuick is None
    assert stmt.limit is None

    tbl = stmt.table
    assert isinstance(tbl, TableSource)
    assert tbl.alias is None
    assert tbl.indexHints is None
    assert tbl.partitions is None
    assert isinstance(tbl.name, TableName)
    assert isinstance(tbl.name.table, Identifier)
    assert tbl.name.table.name.lower() == "t"
    assert isinstance(tbl.name.schema, Identifier)
    assert tbl.name.schema.name.lower() == "s"

    where_def = stmt.where
    assert isinstance(where_def, WhereClause)

    where_val = where_def.value
    assert isinstance(where_val, InPredicate)
    assert where_val.isSubquery is True
    assert where_val.isNot is False
    assert isinstance(where_val.comparableValue, ColumnName)
    assert where_val.comparableValue.table is None
    assert where_val.comparableValue.schema is None
    assert where_val.comparableValue.column.name.lower() == "id"
    assert isinstance(where_val.comparableValue.column, Identifier)
    assert where_val.comparedValues is None

    subquery = where_val.subquery
    assert subquery.limitLines is None
    assert subquery.where is None
    assert subquery.having is None
    assert subquery.export is None
    assert subquery.limitOffset is None
    assert subquery.groupBy is None
    assert isinstance(subquery, SelectStatement)
    assert len(subquery.columns) == 1

    col = subquery.columns[0]
    assert isinstance(col, ColumnClause)
    assert col.alias is None
    assert isinstance(col.value, ColumnName)
    assert col.value.table is None
    assert col.value.schema is None
    assert isinstance(col.value.column, Identifier)
    assert col.value.column.name == "id2"

    from_cl = subquery.fromClause
    assert isinstance(from_cl, FromClause)
    assert len(from_cl.tableRefs) == 1

    tbl = from_cl.tableRefs[0]
    assert isinstance(tbl, TableSource)
    assert tbl.indexHints is None
    assert tbl.partitions is None
    assert tbl.alias is None
    assert isinstance(tbl.name, TableName)
    assert isinstance(tbl.name.table, Identifier)
    assert tbl.name.table.name == "t2"
    assert isinstance(tbl.name.schema, Identifier)
    assert tbl.name.schema.name == "s2"
    assert len(subquery.orderByElems) == 1

    order_by = subquery.orderByElems[0]
    assert order_by.sortType == "ASC"
    assert isinstance(order_by, SortItem)

    expr = order_by.expression
    assert isinstance(expr, ColumnName)
    assert expr.table is None
    assert expr.schema is None
    assert isinstance(expr.column, Identifier)
    assert expr.column.name.lower() == "date"


def test_tsql_create_table_by_column():
    query = "create table ttt(a int NOT NULL, aa smallint PRIMARY KEY, aaa decimal(5,3) unique)"

    script = ast_parser.parse(query)
    assert isinstance(script, Script)
    assert len(script.bodyStatements) == 1

    stmt = script.bodyStatements[0]
    assert isinstance(stmt, CreateTableColumnStatement)

    tbl = stmt.table
    assert isinstance(tbl, TableName)
    assert tbl.schema is None
    assert isinstance(tbl.table, Identifier)
    assert tbl.table.name.lower() == "ttt"
    assert len(stmt.columns) == 3

    col = stmt.columns[0]
    assert isinstance(col, ColumnDefClause)
    assert col.comment is None
    assert col.storage is None
    assert col.columnFormat is None
    assert col.defaultValue is None
    assert col.isAutoIncrement is None
    assert col.isUnique is None
    assert col.isNotNull is True
    assert col.isPrimary is None
    assert isinstance(col.name, Identifier)
    assert col.name.name.lower() == "a"

    data_type = col.dataType
    assert isinstance(data_type, DimensionDataTypeClause)
    assert data_type.typeName.lower() == "int"
    assert data_type.length is None
    assert data_type.secondLength is None
    assert data_type.isUnsigned is None
    assert data_type.isZerofill is None

    col = stmt.columns[1]
    assert isinstance(col, ColumnDefClause)
    assert col.comment is None
    assert col.storage is None
    assert col.columnFormat is None
    assert col.defaultValue is None
    assert col.isAutoIncrement is None
    assert col.isUnique is False
    assert col.isNotNull is None
    assert col.isPrimary is True
    assert isinstance(col.name, Identifier)
    assert col.name.name.lower() == "aa"

    data_type = col.dataType
    assert isinstance(data_type, DimensionDataTypeClause)
    assert data_type.typeName.lower() == "smallint"
    assert data_type.length is None
    assert data_type.secondLength is None
    assert data_type.isUnsigned is None
    assert data_type.isZerofill is None

    col = stmt.columns[2]
    assert isinstance(col, ColumnDefClause)
    assert col.comment is None
    assert col.storage is None
    assert col.columnFormat is None
    assert col.defaultValue is None
    assert col.isAutoIncrement is None
    assert col.isUnique is True
    assert col.isNotNull is None
    assert col.isPrimary is False
    assert isinstance(col.name, Identifier)
    assert col.name.name.lower() == "aaa"
    data_type = col.dataType
    assert isinstance(data_type, DimensionDataTypeClause)
    assert data_type.typeName.lower() == "decimal"
    assert data_type.length == "5"
    assert data_type.secondLength == "3"
    assert data_type.isUnsigned is None
    assert data_type.isZerofill is None


def test_tsql_create_table_by_column_with_foreign():
    query = """create table ttt(colpk smallint PRIMARY KEY, 
        colfk1 smallint references t2(colid) on delete cascade, colfk2_1 smallint, colfk2_2 smallint, 
        constraint fk2 foreign key (colfk2_1, colfk2_2) references t3(col1_id, col2_id) on update set null);
        """

    script = ast_parser.parse(query)
    assert isinstance(script, Script)
    assert len(script.bodyStatements) == 1

    stmt = script.bodyStatements[0]
    assert isinstance(stmt, CreateTableColumnStatement)

    tbl = stmt.table
    assert isinstance(tbl, TableName)
    assert tbl.schema is None
    assert isinstance(tbl.table, Identifier)
    assert tbl.table.name.lower() == "ttt"
    assert len(stmt.columns) == 4

    col = stmt.columns[0]
    assert isinstance(col, ColumnDefClause)
    assert col.comment is None
    assert col.storage is None
    assert col.columnFormat is None
    assert col.defaultValue is None
    assert col.isAutoIncrement is None
    assert col.isUnique is False
    assert col.isNotNull is None
    assert col.isPrimary is True
    assert isinstance(col.name, Identifier)
    assert col.name.name.lower() == "colpk"

    data_type = col.dataType
    assert isinstance(data_type, DimensionDataTypeClause)
    assert data_type.typeName.lower() == "smallint"
    assert data_type.length is None
    assert data_type.secondLength is None
    assert data_type.isUnsigned is None
    assert data_type.isZerofill is None

    col = stmt.columns[1]
    assert isinstance(col, ColumnDefClause)
    assert col.comment is None
    assert col.storage is None
    assert col.columnFormat is None
    assert col.defaultValue is None
    assert col.isAutoIncrement is None
    assert col.isUnique is False
    assert col.isNotNull is None
    assert col.isPrimary is False
    assert isinstance(col.name, Identifier)
    assert col.name.name.lower() == "colfk1"

    data_type = col.dataType
    assert isinstance(data_type, DimensionDataTypeClause)
    assert data_type.typeName.lower() == "smallint"
    assert data_type.length is None
    assert data_type.secondLength is None
    assert data_type.isUnsigned is None
    assert data_type.isZerofill is None

    ref_def = col.refDef
    assert isinstance(ref_def, ReferenceDefClause)

    tbl = ref_def.table
    assert isinstance(tbl, TableName)
    assert tbl.schema is None
    assert isinstance(tbl.table, Identifier)
    assert tbl.table.name.lower() == "t2"
    assert len(ref_def.indexColumns) == 1
    ref_def_col = ref_def.indexColumns[0]
    assert isinstance(ref_def_col, IndexColNameClause)
    assert isinstance(ref_def_col.columnName, Identifier)
    assert ref_def_col.columnName.name.lower() == "colid"
    assert ref_def_col.length is None
    assert ref_def_col.sortType is None
    assert ref_def.onDelete == "cascade"
    assert ref_def.onUpdate is None

    col = stmt.columns[2]
    assert isinstance(col, ColumnDefClause)
    assert col.comment is None
    assert col.storage is None
    assert col.columnFormat is None
    assert col.defaultValue is None
    assert col.isAutoIncrement is None
    assert col.isUnique is None
    assert col.isNotNull is None
    assert col.isPrimary is None
    assert isinstance(col.name, Identifier)
    assert col.name.name.lower() == "colfk2_1"

    data_type = col.dataType
    assert isinstance(data_type, DimensionDataTypeClause)
    assert data_type.typeName.lower() == "smallint"
    assert data_type.length is None
    assert data_type.secondLength is None
    assert data_type.isUnsigned is None
    assert data_type.isZerofill is None

    col = stmt.columns[3]
    assert isinstance(col, ColumnDefClause)
    assert col.comment is None
    assert col.storage is None
    assert col.columnFormat is None
    assert col.defaultValue is None
    assert col.isAutoIncrement is None
    assert col.isUnique is None
    assert col.isNotNull is None
    assert col.isPrimary is None
    assert isinstance(col.name, Identifier)
    assert col.name.name.lower() == "colfk2_2"
    data_type = col.dataType
    assert isinstance(data_type, DimensionDataTypeClause)
    assert data_type.typeName.lower() == "smallint"
    assert data_type.length is None
    assert data_type.secondLength is None
    assert data_type.isUnsigned is None
    assert data_type.isZerofill is None
    assert len(stmt.constraints) == 1

    constr = stmt.constraints[0]
    assert isinstance(constr, ConstraintKeyClause)
    assert isinstance(constr.name, Identifier)
    assert constr.name.name.lower() == "fk2"
    assert constr.keyType.lower() == "foreign"
    assert len(constr.indexColumns) == 2

    icol = constr.indexColumns[0]
    assert isinstance(icol, IndexColNameClause)
    assert isinstance(icol.columnName, Identifier)
    assert icol.columnName.name.lower() == "colfk2_1"
    assert icol.length is None
    assert icol.sortType is None

    icol = constr.indexColumns[1]
    assert isinstance(icol, IndexColNameClause)
    assert isinstance(icol.columnName, Identifier)
    assert icol.columnName.name.lower() == "colfk2_2"
    assert icol.length is None
    assert icol.sortType is None
    assert constr.indexName is None
    assert constr.indexType is None
    assert constr.indexOptionSet is None

    ref_def = constr.refDef
    assert isinstance(ref_def, ReferenceDefClause)

    tbl = ref_def.table
    assert isinstance(tbl, TableName)
    assert tbl.schema is None
    assert isinstance(tbl.table, Identifier)
    assert tbl.table.name.lower() == "t3"
    assert len(ref_def.indexColumns) == 2

    ref_def_col = ref_def.indexColumns[0]
    assert isinstance(ref_def_col, IndexColNameClause)
    assert isinstance(ref_def_col.columnName, Identifier)
    assert ref_def_col.columnName.name.lower() == "col1_id"
    assert ref_def_col.length is None
    assert ref_def_col.sortType is None

    ref_def_col = ref_def.indexColumns[1]
    assert isinstance(ref_def_col, IndexColNameClause)
    assert isinstance(ref_def_col.columnName, Identifier)
    assert ref_def_col.columnName.name.lower() == "col2_id"
    assert ref_def_col.length is None
    assert ref_def_col.sortType is None
    assert ref_def.onDelete is None
    assert ref_def.onUpdate == "setnull"


def test_tsql_union():
    query = """SELECT a, aa FROM s.t
               WHERE id NOT IN (3, 4)
               UNION SELECT b, bb FROM ss.tt ORDER BY v
            """

    script = ast_parser.parse(query)
    assert isinstance(script, Script)
    assert len(script.bodyStatements) == 1

    stmt = script.bodyStatements[0]
    assert isinstance(stmt, UnionStatement)
    assert len(stmt.clauses) == 2

    #  FirstUnionClause start
    clause = stmt.clauses[0]
    assert clause.unionType is None
    assert isinstance(clause, UnionClause)

    stmt12 = clause.statement
    assert isinstance(stmt12, SelectStatement)
    assert stmt12.limitLines is None
    assert stmt12.having is None
    assert stmt12.orderByElems is None
    assert stmt12.export is None
    assert stmt12.limitOffset is None
    assert stmt12.groupBy is None

    #  FirstColumn start
    col = stmt12.columns[0]
    assert isinstance(col, ColumnClause)
    assert col.alias is None

    col_value = col.value
    assert isinstance(col_value, ColumnName)
    assert col_value.table is None
    assert col_value.schema is None
    assert isinstance(col_value.column, Identifier)
    assert col_value.column.name == "a"

    #  FirstColumn end
    #  SecondColumn start
    col = stmt12.columns[1]
    assert isinstance(col, ColumnClause)
    assert col.alias is None

    col_value = col.value
    assert isinstance(col_value, ColumnName)
    assert col_value.table is None
    assert col_value.schema is None
    assert isinstance(col_value.column, Identifier)
    assert col_value.column.name == "aa"

    #  SecondColumn end
    #  From_clause start
    from_cl = stmt12.fromClause
    assert isinstance(from_cl, FromClause)
    assert len(from_cl.tableRefs) == 1

    tbl = from_cl.tableRefs[0]
    assert isinstance(tbl, TableSource)
    assert tbl.indexHints is None
    assert tbl.partitions is None
    assert tbl.alias is None
    assert isinstance(tbl.name, TableName)
    assert isinstance(tbl.name.table, Identifier)
    assert tbl.name.table.name == "t"
    assert isinstance(tbl.name.schema, Identifier)
    assert tbl.name.schema.name == "s"

    #  From_clause end
    #  where_definition start
    where_def = stmt12.where
    assert isinstance(where_def, WhereClause)
    expr = where_def.value
    assert isinstance(expr, InPredicate)
    assert expr.isNot is True
    assert expr.isSubquery is False
    val = expr.comparableValue
    assert isinstance(val, ColumnName)
    assert val.schema is None
    assert val.table is None
    assert isinstance(val.column, Identifier)
    assert val.column.name.lower() == "id"
    val_list = expr.comparedValues
    assert val_list[0].value == "3"
    assert isinstance(val_list[0], NumberLiteral)
    assert val_list[1].value == "4"
    assert isinstance(val_list[1], NumberLiteral)
    #  where_definition end
    #  FirstUnionClause end

    #  SecondUnionClause start
    clause = stmt.clauses[1]
    assert clause.unionType is None
    assert isinstance(clause, UnionClause)
    stmt12 = clause.statement
    assert isinstance(stmt12, SelectStatement)
    assert stmt12.limitLines is None
    assert stmt12.having is None
    assert stmt12.orderByElems is None
    assert stmt12.export is None
    assert stmt12.limitOffset is None
    assert stmt12.groupBy is None

    #  FirstColumn start
    col = stmt12.columns[0]
    assert isinstance(col, ColumnClause)
    assert col.alias is None

    col_value = col.value
    assert isinstance(col_value, ColumnName)
    assert col_value.table is None
    assert col_value.schema is None
    assert isinstance(col_value.column, Identifier)
    assert col_value.column.name == "b"

    #  FirstColumn end
    #  SecondColumn start
    col = stmt12.columns[1]
    assert isinstance(col, ColumnClause)
    assert col.alias is None

    col_value = col.value
    assert isinstance(col_value, ColumnName)
    assert col_value.table is None
    assert col_value.schema is None
    assert isinstance(col_value.column, Identifier)
    assert col_value.column.name == "bb"

    #  SecondColumn end
    #  From_clause start
    from_cl = stmt12.fromClause
    assert isinstance(from_cl, FromClause)
    assert len(from_cl.tableRefs) == 1

    tbl = from_cl.tableRefs[0]
    assert isinstance(tbl, TableSource)
    assert tbl.indexHints is None
    assert tbl.partitions is None
    assert tbl.alias is None
    assert isinstance(tbl.name, TableName)
    assert isinstance(tbl.name.table, Identifier)
    assert tbl.name.table.name == "tt"
    assert isinstance(tbl.name.schema, Identifier)
    assert tbl.name.schema.name == "ss"

    #  From_clause end
    #  SecondUnionClause end
    order_by = stmt.orderByElems[0]
    assert order_by.sortType is None
    assert isinstance(order_by, SortItem)
    expr = order_by.expression
    assert isinstance(expr, ColumnName)
    assert expr.table is None
    assert expr.schema is None
    assert isinstance(expr.column, Identifier)
    assert expr.column.name.lower() == "v"


def test_tsql_join():
    query = """ SELECT DaysToManufacture
                FROM Sales.SalesOrderDetail
                JOIN Production.Product
                ON Sales.SalesOrderDetail.ProductID = Production.Product.ProductID
                WHERE SalesOrderID = OrderID
            """
    script = ast_parser.parse(query)
    assert isinstance(script, Script)

    body = script.bodyStatements
    assert len(body) == 1

    stmt = body[0]
    assert isinstance(stmt, SelectStatement)
    assert len(stmt.columns) == 1
    assert stmt.limitLines is None
    assert stmt.limitOffset is None
    assert stmt.having is None
    assert stmt.groupBy is None
    assert stmt.orderByElems is None
    assert stmt.export is None

    #  FirstColumn start
    col = stmt.columns[0]
    assert isinstance(col, ColumnClause)
    assert col.alias is None

    col_value = col.value
    assert isinstance(col_value, ColumnName)
    assert col_value.table is None
    assert col_value.schema is None
    assert isinstance(col_value.column, Identifier)
    assert col_value.column.name == "DaysToManufacture"

    #  FirstColumn end
    #  From_clause start
    from_clause = stmt.fromClause
    assert isinstance(from_clause, FromClause)
    assert len(from_clause.tableRefs) == 1

    tbl_ref = from_clause.tableRefs[0]
    assert isinstance(tbl_ref, JoinClause)
    assert tbl_ref.joinType == "join"
    assert tbl_ref.joinColumns is None
    assert tbl_ref.isNatural is None
    assert len(tbl_ref.leftClauses) == 1

    left = tbl_ref.leftClauses[0]
    assert isinstance(left, TableSource)
    assert left.alias is None
    assert left.indexHints is None
    assert left.partitions is None
    assert isinstance(left.name, TableName)
    assert isinstance(left.name.schema, Identifier)
    assert left.name.schema.name == "Sales"
    assert isinstance(left.name.table, Identifier)
    assert left.name.table.name == "SalesOrderDetail"

    join_condition = tbl_ref.joinCondition
    assert isinstance(join_condition, ComparisonPredicate)
    assert join_condition.comparisonOperator == "="

    right = join_condition.rightArg
    assert isinstance(right, ColumnName)
    assert isinstance(right.table, Identifier)
    assert right.table.name == "Product"
    assert isinstance(right.schema, Identifier)
    assert right.schema.name == "Production"
    assert isinstance(right.column, Identifier)
    assert right.column.name == "ProductID"

    left = join_condition.leftArg
    assert isinstance(left, ColumnName)
    assert isinstance(left.table, Identifier)
    assert left.table.name == "SalesOrderDetail"
    assert isinstance(left.schema, Identifier)
    assert left.schema.name == "Sales"
    assert isinstance(left.column, Identifier)
    assert left.column.name == "ProductID"
    assert len(tbl_ref.rightClauses) == 1

    right = tbl_ref.rightClauses[0]
    assert isinstance(right, TableSource)
    assert right.alias is None
    assert right.indexHints is None
    assert right.partitions is None
    assert isinstance(right.name, TableName)
    assert isinstance(right.name.schema, Identifier)
    assert right.name.schema.name == "Production"
    assert isinstance(right.name.table, Identifier)
    assert right.name.table.name == "Product"

    #  From_clause end
    #  where_definition start
    where_def = stmt.where
    assert isinstance(where_def, WhereClause)

    where_val = where_def.value
    assert isinstance(where_val, ComparisonPredicate)
    assert where_val.comparisonOperator == "="

    right = where_val.rightArg
    assert isinstance(right, ColumnName)
    assert right.table is None
    assert right.schema is None
    assert isinstance(right.column, Identifier)
    assert right.column.name == "OrderID"

    left = where_val.leftArg
    assert isinstance(left, ColumnName)
    assert left.table is None
    assert left.schema is None
    assert isinstance(left.column, Identifier)
    assert left.column.name == "SalesOrderID"
    #  where_definition end
