import sys
from antlr4.tree.Tree import TerminalNode
from aule.generated.sqlAST import *
from aule.generated.tsqlVisitor import tsqlVisitor


class tsqlASTVisitor(tsqlVisitor):

    def visitRoot(self, ctx):
        nodes = []
        if len(ctx.batch()) > 0:
            nodes = self.visit(ctx.batch(0))
        iscommented = False
        # Define if SQL has comments.
        common_tokens = ctx.parser._input.tokens
        line_comment = ctx.parser.LINE_COMMENT
        comment_input = ctx.parser.COMMENT
        for token in common_tokens:
            if token.type == line_comment or token.type == comment_input:
                iscommented = True
        return Script(bodyStatements=nodes, iscommented=iscommented)

    def visitBatch(self, ctx):
        sqlSentences = []
        sqlSentences_tree = ctx.sql_clauses().sql_clause()
        cntSent = len(sqlSentences_tree)
        index = 0
        while index < cntSent:
            sqlCurSentence = self.visit(sqlSentences_tree[index])
            sqlSentences.append(sqlCurSentence)
            index += 1
        return sqlSentences

    def visitSql_clauses(self, ctx):
        body = []
        for stmt in ctx.sql_clause():
            body.append(self.visit(stmt))
        return BlockQueryStatement(bodyStatements=body)

    def visitSql_clause(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitDml_clause(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitDdl_clause(self, ctx):
        return self.visit(ctx.getChild(0))

    # cfl_statement start

    def visitIf_statement(self, ctx):
        condition = self.visit(ctx.search_condition())
        statements = []
        statements.append(self.visit(ctx.sql_clause(0)))
        else_alternative = self.visit(ctx.sql_clause(1)) if ctx.ELSE() else None
        return IfStatement(
            condition=condition, statements=statements,
            elseAlternativeStatements=else_alternative
        )

    def visitReturn_statement(self, ctx):
        value = self.visit(ctx.expression()) if ctx.expression() else None
        return ReturnStatement(value=value)

    def visitWhile_statement(self, ctx):
        search_condition = self.visit(ctx.search_condition())
        statements = self.visit(ctx.sql_clause()) if ctx.sql_clause() else None
        statements = ctx.BREAK().getText() if ctx.BREAK() else statements
        statements = ctx.CONTINUE().getText() if ctx.CONTINUE() else statements
        return WhileStatement(searchCondition=search_condition,  statements=statements)

    # cfl_statement end
    def visitAnother_statement(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitDeclare_statement(self, ctx):
        # need describe!
        columns, constraints = None, None
        declare_local = []
        if ctx.table_type_definition():
            columns, constraints = self.visit(ctx.table_type_definition())
            expr = ctx.LOCAL_ID().getText()
        if ctx.declare_local():
            for index in range(len(ctx.declare_local())):
                declare_local.append(self.visit(ctx.declare_local(index)))

    def visitCursor_statement(self, ctx):
        # need describe global
        global_ = True if ctx.GLOBAL() else False
        name = self.visit(ctx.cursor_name()) if ctx.cursor_name() else None
        control_type = "close" if ctx.CLOSE() else None
        control_type = "open" if ctx.OPEN() else control_type
        control_type = "deallocate" if ctx.DEALLOCATE() else control_type
        result = HandleCursorStatement(handletype=control_type, name=name)
        if ctx.fetch_cursor():
            result = self.visit(ctx.fetch_cursor())
        if ctx.declare_cursor():
            result = self.visit(ctx.declare_cursor())
        return result

    def visitFetch_cursor(self, ctx):
        # need describe global
        # need describe ((NEXT | PRIOR | FIRST | LAST | (ABSOLUTE | RELATIVE) expression)?
        variables = []
        global_ = True if ctx.GLOBAL() else False
        name = self.visit(ctx.cursor_name()) if ctx.cursor_name() else None
        expr = self.visit(ctx.expression()) if ctx.expression() else None
        for index in range(len(ctx.LOCAL_ID())):
            variables.append(Identifier(ctx.LOCAL_ID(index).getText()))
        return FetchCursorStatement(name=name, variables=variables)

    def visitDeclare_cursor(self, ctx):
        # need describe column_name_list
        # need describe declare_set_cursor_common!
        name = self.visit(ctx.cursor_name()) if ctx.cursor_name() else None
        if ctx.select_statement():
            select = self.visit(ctx.select_statement())
        else:
            select = self.visit(ctx.declare_set_cursor_common().select_statement())
        return DeclareCursor(name=name, select=select)

    #  Delete Statement start.
    def visitDelete_statement(self, ctx):
        where_clauses = None
        priority = None
        limit = None
        tables = TableSource(name=self.visit(ctx.delete_statement_from()))
        if ctx.with_expression():
            with_expression = self.visit(ctx.with_expression())
        if ctx.expression():
            expression = self.visit(ctx.expression())
        if ctx.insert_with_table_hints():
            insert_with_table_hints = self.visit(ctx.insert_with_table_hints())
        if ctx.output_clause():
            output_clause = self.visit(ctx.output_clause())
        if ctx.search_condition():
            where_clauses = WhereClause(value=self.visit(ctx.search_condition()))
        if ctx.for_clause():
            for_clause = self.visit(ctx.for_clause())
        if ctx.option_clause():
            option_clause = self.visit(ctx.option_clause())
        if ctx.table_sources():
            sources = self.visit(ctx.table_sources())
            result = DeleteMultipleStatement(priority=priority,
                                             tables=tables, tableRefs=sources, where=where_clauses)
        else:
            result = DeleteSingleStatement(priority=priority, table=tables, where=where_clauses,
                                           limit=limit)
        return result

    def visitDelete_statement_from(self, ctx):
        table_name = None
        if ctx.table_alias():
            table_name = TableName(table=self.visit(ctx.table_alias()))
        if ctx.ddl_object():
            table_name = self.visit(ctx.ddl_object())
        return table_name
    #  Delete Statement end

    #  Insert Statement start.
    def visitInsert_statement(self, ctx):
        #  need fix
        rows = []
        values = self.visit(ctx.insert_statement_value())
        table = None
        columns = []
        if ctx.with_expression():
            with_expression = self.visit(ctx.with_expression())
        if ctx.expression():
            expression = self.visit(ctx.expression())
        if ctx.ddl_object():
            table = self.visit(ctx.ddl_object())
        elif ctx.rowset_function_limited():
            table = self.visit(ctx.rowset_function_limited())
        if ctx.insert_with_table_hints():
            insert_with_table_hints = self.visit(ctx.insert_with_table_hints())
        if ctx.column_name_list():
            columns = self.visit(ctx.column_name_list())
        if ctx.output_clause():
            output_clause = self.visit(ctx.output_clause())
        if ctx.for_clause():
            for_clause = self.visit(ctx.for_clause())
        if ctx.option_clause():
            option_clause = self.visit(ctx.option_clause())
        if ctx.insert_statement_value().table_value_constructor():
            for index in range(len(values)):
                rows.append(InsertRowClause(values=values[index]))
            result = InsertRowStatement(table=table, columns=columns, rows=rows)
        elif ctx.insert_statement_value().derived_table():
            rows = values
            result = InsertQueryStatement(table=table, columns=columns, query=rows)
        elif ctx.insert_statement_value().execute_statement():
            pass
        else:
            pass
        return result

    def visitInsert_statement_value(self, ctx):
        insert_statement_value = []
        if ctx.table_value_constructor():
            insert_statement_value = self.visit(ctx.table_value_constructor())
        elif ctx.derived_table():
            insert_statement_value = self.visit(ctx.derived_table())
        elif ctx.execute_statement():
            insert_statement_value = self.visit(ctx.execute_statement())
        else:
            insert_statement_value.append(ctx.DEFAULT().getText() + ctx.VALUES().getText())
        return insert_statement_value

    def visitInsert_with_table_hints(self, ctx):
        insert_with_table_hints = []
        index = 0
        child_count = ctx.getChildCount()
        while index < child_count:
            insert_with_table_hints.append(ctx.table_hint(index))
            index += 1
        return insert_with_table_hints

    def visitRowset_function_limited(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitOpenquery(self, ctx):
        return ctx.OPENQUERY().getText(), self.visit(ctx.linked_server), ctx.query

    def visitOpendatasource(self, ctx):
        database = Identifier(ctx.database.getText()) if ctx.database else None
        schema = Identifier(ctx.schema.getText()) if ctx.schema else None
        open_data_source = ctx.OPENDATASOURCE().getText()
        provider = ctx.provider.getText()
        init = ctx.init.getText()
        table = ctx.table.getText()
        return open_data_source, provider, init, database, schema, table

    def visitOutput_clause(self, ctx):
        output_clauses = []
        index = 0
        child_count = ctx.getChildCount()
        while index < child_count:
            output_clauses.append(ctx.output_dml_list_elem(index))
            index += 1
        column_name_list = self.visit(ctx.column_name_list()) if ctx.column_name_list() else None
        return output_clauses

    def visitSelect_statement(self, ctx):
        order_clauses = None
        row_count, offset = None, None
        group_clauses = None
        where_clauses = None
        having_clauses = None
        columns = None
        if ctx.with_expression():
            with_expression = self.visit(ctx.with_expression())
        if ctx.query_expression():
            columns, from_clause, where_clauses, having_clauses, group_clauses, union = self.visit(ctx.query_expression())
        if ctx.order_by_clause():
            order_clauses = self.visit(ctx.order_by_clause())
        if ctx.for_clause():
            pass
        if ctx.option_clause():
            pass
        from_clause = FromClause(from_clause) if from_clause else None
        if len(union) > 0:
            statement = SelectStatement(
                columns=columns,
                fromClause=from_clause,
                where=where_clauses,
                groupby=group_clauses,
                having=having_clauses
            )
            union.insert(0, UnionClause(statement=statement, unionType=None))
            result = UnionStatement(clauses=union, orderByElems=order_clauses)
        else:
            result = SelectStatement(
                columns=columns,
                fromClause=from_clause,
                where=where_clauses,
                groupBy=group_clauses,
                orderByElems=order_clauses,
                having=having_clauses,
                limitLines=row_count,
                limitOffset=offset
            )
        return result

    def visitUpdate_statement(self, ctx):
        # need fix where_expr
        update_elem = []
        columns = []
        values = []
        where_expr = ["None"]
        table = None
        expression = None
        if ctx.with_expression():
            with_expression = self.visit(ctx.with_expression())
        if ctx.expression():
            expression = self.visit(ctx.expression())
        if ctx.ddl_object():
            # table = self.visit(ctx.ddl_object())
            table = TableSource(name=self.visit(ctx.ddl_object()))
        elif ctx.rowset_function_limited():
            rowset_function_limited = self.visit(ctx.rowset_function_limited())
        if ctx.with_table_hints():
            with_table_hints = self.visit(ctx.with_table_hints())
        if ctx.update_elem():
            for index in range(len(ctx.update_elem())):
                update_elem.append(self.visit(ctx.update_elem(index)))
                columns.append(update_elem[index][0])
                values.append(update_elem[index][2])
        if ctx.output_clause():
            output_clause = self.visit(ctx.output_clause())
        if ctx.table_sources():
            table_sources = self.visit(ctx.table_sources())
        if ctx.search_condition_list():
            where_expr = self.visit(ctx.search_condition_list())  # return list
        if ctx.for_clause():
            for_clause = self.visit(ctx.for_clause())
        if ctx.option_clause():
            option_clause = self.visit(ctx.option_clause)
        return UpdateSingleStatement(columns=columns, values=values, source=table, where=WhereClause(value=where_expr[0]), limit=expression)

    def visitUpdate_elem(self, ctx):
        full_column_name = None
        assignment_operator = None
        expression = None
        if ctx.expression():
            full_column_name = self.visit(ctx.full_column_name()) if ctx.full_column_name() else ctx.LOCAL_ID().getText()
            assignment_operator = self.visit(ctx.assignment_operator()) if ctx.assignment_operator() else "="
            expression = self.visit(ctx.expression())
        else:
            udt_column_name = ctx.udt_column_name
            method_name = ctx.method_name
            expression_list = self.visit(ctx.expression_list())
        return full_column_name, assignment_operator, expression

    def visitQuery_expression(self, ctx):
        columns, from_clause, where_clauses, having_clauses, group_clauses, union = self.visit(ctx.query_specification())\
            if ctx.query_specification() else self.visit(ctx.query_expression())
        if len(ctx.union()) > 0:
            for index in range(len(ctx.union())):
                union.append(self.visit(ctx.union(index)))
        return columns, from_clause, where_clauses, having_clauses, group_clauses, union

    def visitUnion(self, ctx):
        union_type = ctx.ALL().getText() if ctx.ALL() else None
        columns, from_clause, where_clauses, having_clauses, group_clauses, union = self.visit(ctx.query_specification()) \
            if ctx.query_specification() else self.visit(ctx.query_expression())
        from_clause = FromClause(from_clause) if from_clause else None
        statement = SelectStatement(
                columns=columns,
                fromClause=from_clause,
                where=where_clauses,
                groupBy=group_clauses,
                having=having_clauses
            )
        return UnionClause(statement=statement, unionType=union_type)

    def visitQuery_specification(self, ctx):
        top_clause = None
        from_clause = None
        where_clauses = None
        having_clauses = None
        columns = None
        group_clauses = None
        clauses = []
        for index in range(len(ctx.group_by_item())):
            item = self.visit(ctx.group_by_item(index))
            clauses.append(item)
        if len(clauses) > 0:
            group_clauses = GroupbyClause(values=clauses)
        if ctx.top_clause():
            top_clause = self.visit(ctx.top_clause())
        if ctx.select_list():
            columns = self.visit(ctx.select_list())
        if ctx.table_sources():
            from_clause = self.visit(ctx.table_sources())
        if ctx.WHERE():
            where_clauses = WhereClause(value=self.visit(ctx.search_condition(0)))
        if ctx.HAVING():
            having_clauses = self.visit(ctx.search_condition(1)) if ctx.WHERE() else self.visit(ctx.search_condition(0))
        return columns, from_clause, where_clauses, having_clauses, group_clauses, []

    def visitOrder_by_clause(self, ctx):
        clauses = []
        for index in range(len(ctx.order_by_expression())):
            clauses.append(self.visit(ctx.order_by_expression(index)))
        return clauses

    def visitOrder_by_expression(self, ctx):
        expr = self.visit(ctx.expression())
        sort_type = ctx.getChild(1).getText() if ctx.ASC() or ctx.DESC() else None
        return SortItem(expression=expr, sortType=sort_type)

    def visitFor_clause(self, ctx):
        # TODO: need  fix return statement
        if ctx.STRING():
            result = ctx.STRING().getText()
        if ctx.xml_common_directives():
            xml_common_directives = self.visit(ctx.xml_common_directives())
        return result

    def visitXml_common_directives(self, ctx):
        return ctx.getChild(3).getText()

    def visitGroup_by_item(self, ctx):
        return self.visit(ctx.expression())

    def visitOption_clause(self, ctx):
        options = []
        for index in range(ctx.getChildCount()):
            option = self.visit(ctx.option(index))
            options.append(option)
        return options

    def visitOption(self, ctx):
        name = ctx.getChild(0).getText()
        optimize_for_arg = []
        if len(ctx.optimize_for_arg()) > 0:
            for index in range(len(ctx.optimize_for_arg())):
                optimize_for_arg.append(self.visit(ctx.optimize_for_arg(index)))
        if ctx.number_rows:
            number_rows = ctx.number_rows
        if ctx.number_of_processors:
            umber_of_processors = ctx.number_of_processors
        if ctx.number_recursion:
            number_recursion = ctx.number_recursion
        return name

    def visitOptimize_for_arg(self, ctx):
        arg = self.visit(ctx.constant()) if ctx.constant() else ctx.UNKNOWN().getText()
        return arg

    def visitSelect_list(self, ctx):
        columns = []
        for index in range(len(ctx.select_list_elem())):
            node = ColumnClause(value=self.visit(ctx.select_list_elem(index))[0],
                                alias=self.visit(ctx.select_list_elem(index))[1])
            columns.append(node)
        return columns

    def visitSelect_list_elem(self, ctx):
        # need add $
        alias = None
        column_alias = None
        if ctx.expression():
            result = self.visit(ctx.expression())
            if ctx.column_alias():
                column_alias = self.visit(ctx.column_alias())
        else:
            elem = ctx.getText()
            if ctx.table_name():
                alias = ctx.table_name().getText()
            if elem == '*':
                elem = Star("*")
            result = ColumnName(column=elem,  table=alias)
        return [result, column_alias]

    def visitTable_sources(self, ctx):
        tables = []
        for index in range(len(ctx.table_source())):
            tables.append(self.visit(ctx.table_source(index)))
        return tables

    def visitTable_source(self, ctx):
        table = self.visit(ctx.table_source_item_joined())
        return table

    def visitTable_source_item_joined(self, ctx):
        tbl_source = None
        join_part_tree = ctx.join_part()
        if ctx.table_source_item():
            tbl_source = self.visit(ctx.table_source_item())
        # Here we have at least ONE JOIN
        if join_part_tree:
            # 0. Init step
            len_join_part_tree = len(join_part_tree)
            index = 0
            # for first iteration of while
            if isinstance(tbl_source, list):
                new_tbl_source = tbl_source
            else:
                new_tbl_source = [tbl_source]
            # Iterate all JOINs
            while index < len_join_part_tree:
                left = new_tbl_source
                right, join_type, search_condition = self.visit(join_part_tree[index])
                new_tbl_source = JoinClause(
                    joinType=join_type, leftClauses=left, rightClauses=right, joinCondition=search_condition
                )
                index += 1
            tbl_source = new_tbl_source
            #  If we have no join_part hence we have ONLY tbl_source
            #  and it is already defined
        return tbl_source

    def visitTable_source_item(self, ctx):
        # need add different alias for SubqueryClause
        # need describe rowset_function
        # need describe change_table
        # need describe function_call
        # need describe LOCAL_ID
        # need describe LOCAL_ID '.' function_call
        table_alias = None
        column_alias_list = None
        function_call = None
        local_id = None
        result = None
        if ctx.as_table_alias():
            table_alias = self.visit(ctx.as_table_alias())
            if ctx.column_alias_list():
                column_alias_list = self.visit(ctx.column_alias_list())
        if ctx.LOCAL_ID():
            local_id = Identifier(ctx.LOCAL_ID().getText())
            if ctx.function_call():
                function_call = self.visit(ctx.function_call())
        if ctx.table_name_with_hint():
            table, index_hint = self.visit(ctx.table_name_with_hint())
            result = TableSource(name=table, alias=table_alias, indexHints=index_hint)
        if ctx.derived_table():
            select = self.visit(ctx.derived_table())
            result = SubqueryClause(select=select)
        return result

    def visitJoin_part(self, ctx):
        # need add join_hint
        # describe APPLY ?
        join_hint = None
        join_type = ctx.getChild(0).getText().lower()
        search_condition = None
        tbl_item = self.visit(ctx.table_source())
        if isinstance(tbl_item, list) is False:
            right = [tbl_item]
        else:
            right = tbl_item
        if ctx.join_type:
            join_type = ctx.LEFT().getText() if ctx.LEFT() else None
            join_type = ctx.RIGHT().getText() if ctx.RIGHT() else join_type
            join_type = ctx.FULL().getText() if ctx.FULL() else join_type
        if ctx.join_hint:
            join_hint = ctx.join_hint.getText()
        if ctx.search_condition():
            search_condition = self.visit(ctx.search_condition())
        return right, join_type, search_condition

    def visitTable_name_with_hint(self, ctx):
        index_hint = None
        if ctx.with_table_hints():
            index_hint = self.visit(ctx.with_table_hints())
        table = self.visit(ctx.table_name())
        return table, index_hint

    def visitFunction_call(self, ctx):
        separator = None
        if ctx.ranking_windowed_function():
            result = self.visit(ctx.ranking_windowed_function())
        elif ctx.aggregate_windowed_function():
            result = self.visit(ctx.aggregate_windowed_function())
        elif ctx.scalar_function_name():
            name = ctx.scalar_function_name().getText()
            arguments = None
            if ctx.expression_list():
                arguments = self.visit(ctx.expression_list())
            result = SimpleFunctionCall(name=name, arguments=arguments)
        else:
            name = ctx.getChild(0).getText()
            ext_args = []
            if ctx.expression_list():
                ext_args.append(self.visit(ctx.expression_list()))
            if ctx.data_type():
                data_type, first_dim, second_dim, charset = self.visit(ctx.data_type())
                cur_arg = ConvertedDataType(dataType=data_type, firstDim=first_dim, secondDim=second_dim, charSet=charset)
                if name == 'CAST':
                    ext_args.append(FuncExtDataTypeArgument(value=cur_arg, keyword="AS", keywordPosition="BEFORE"))
                else:
                    ext_args.append(FuncExtDataTypeArgument(value=cur_arg))
            if ctx.DECIMAL():
                ext_args.append(FuncExtExprArgument(value=ctx.DECIMAL(0).getText(), separator=","))
                if len(ctx.DECIMAL()) > 1:
                    ext_args.append(FuncExtExprArgument(value=ctx.DECIMAL(1).getText(), separator=","))
            if ctx.ID():
                ext_args.append(FuncExtExprArgument(value=Identifier(ctx.ID().getText())))
            if ctx.expression():
                if name != "CAST" and name != "NULLIF":
                    separator = ","
                ext_args.append(FuncExtExprArgument(value=self.visit(ctx.expression(0)), separator=separator))
                if len(ctx.expression()) > 1:
                    separator = ","
                    ext_args.append(FuncExtExprArgument(value=self.visit(ctx.expression(1)), separator=separator))
            result = ExtArgFunctionCall(name=name, arguments=ext_args)
        return result

    def visitAggregate_windowed_function(self, ctx):

        name = ctx.getChild(0).getText()
        aggregator = None
        arguments = None
        order_by = None
        concat_separator = None
        over_clause = None
        if ctx.all_distinct_expression():
            arguments = self.visit(ctx.all_distinct_expression())
        if ctx.over_clause():
            over_clause = self.visit(ctx.over_clause())
        if ctx.expression():
            expression = self.visit(ctx.expression())
        if ctx.expression_list():
            expression_list = self.visit(ctx.expression_list())
        return AggregateFunctionCall(name=name, aggregator=aggregator, arguments=arguments, orderByElems=order_by,
                                     concatSeparator=concat_separator, over=over_clause)

    def visitRanking_windowed_function(self, ctx):
        name = ctx.getChild(0).getText()
        arguments = None
        over_clause = None
        if ctx.expression():
            arguments = self.visit(ctx.expression())
        if ctx.over_clause():
            over_clause = self.visit(ctx.over_clause())
        return AggregateFunctionCall(name=name, arguments=arguments, over=over_clause)

    def visitData_type(self, ctx):
        data_type = ctx.getChild(0).getText()
        first_dim = None
        second_dim = None
        charset = None
        if ctx.DECIMAL():
            first_dim = ctx.DECIMAL(0).getText()
            if len(ctx.DECIMAL()) > 1:
                second_dim = ctx.DECIMAL(1).getText()
        if ctx.MAX():   # max indicates that the maximum storage size is 2^31-1 bytes (2 GB). example varchar(MAX)
            first_dim = ctx.MAX().getText()
            if ctx.DECIMAL():
                second_dim = ctx.DECIMAL().getText()
        return data_type, first_dim, second_dim, charset

    def visitAs_table_alias(self, ctx):
        return self.visit(ctx.table_alias())

    def visitTable_alias(self, ctx):
        return self.visit(ctx.id_())

    def visitWith_table_hints(self, ctx):
        with_table_hints = []
        for index in range(len(ctx.table_hint())):
            with_table_hints.append(self.visit(ctx.table_hint(index)))
        return with_table_hints

    def visitTable_hint(self, ctx):
        # need describe hint
        return ctx.getCild(0).getText()

    def visitIndex_value(self, ctx):
        result = ctx.id_().getText() if ctx.id_() else ctx.DECIMAL().getText()
        return result

    def visitTable_value_constructor(self, ctx):
        table_value_constructor = []
        for index in range(len(ctx.expression_list())):
            table_value_constructor.append(self.visit(ctx.expression_list(index)))
        return table_value_constructor

    def visitExpression_list(self, ctx):
        expression_list = []
        for index in range(len(ctx.expression())):
            expression_list.append(self.visit(ctx.expression(index)))
        return expression_list

    def visitFull_table_name(self, ctx):
        # need add database, server
        server = Identifier(ctx.server.getText()) if ctx.server else None
        database = Identifier(ctx.database.getText()) if ctx.database else None
        schema = Identifier(ctx.schema.getText()) if ctx.schema else None
        table = Identifier(ctx.table.getText()) if ctx.table else None
        return TableName(schema=schema, table=table)

    def visitTable_name(self, ctx):
        database = Identifier(ctx.database.getText()) if ctx.database else None
        schema = Identifier(ctx.schema.getText()) if ctx.schema else None
        table = Identifier(ctx.table.getText()) if ctx.table else None
        return TableName(schema=schema, table=table)

    def visitSimple_name(self, ctx):
        schema = Identifier(ctx.schema.getText()) if ctx.schema else None
        name = Identifier(ctx.name.getText())
        return schema, name

    def visitDdl_object(self, ctx):
        result = self.visit(ctx.full_table_name()) if ctx.full_table_name() else TableName(table=ctx.LOCAL_ID().getText())
        return result

    # Search_condition start
    def visitSearch_condition_list(self, ctx):
        conditions = []
        index = 0
        tbl_count = len(ctx.search_condition())
        while index < tbl_count:
            conditions.append(self.visit(ctx.search_condition(index)))
            index += 1
        return conditions

    def visitSearch_condition(self, ctx):
        result = self.visit(ctx.search_condition_and(0))
        if len(ctx.search_condition_and()) > 1:
            len_ = len(ctx.search_condition_and())
            left = self.visit(ctx.search_condition_and(0))
            index = 1
            for i in range(1, len_-1, 1):
                op = ctx.getChild(index).getText()
                right = self.visit(ctx.search_condition_and(i))
                left = LogicalExpression(operator=op, leftArg=left, rightArg=right, isUnary=False)
                index += 2
            right = self.visit(ctx.search_condition_and(len_-1))
            op = ctx.getChild(index).getText()
            result = LogicalExpression(operator=op, leftArg=left, rightArg=right, isUnary=False)
        return result

    def visitSearch_condition_and(self, ctx):
        result = self.visit(ctx.search_condition_not(0))
        if len(ctx.search_condition_not()) > 1:
            len_ = len(ctx.search_condition_not())
            left = self.visit(ctx.search_condition_not(0))
            index = 1
            for i in range(1, len_-1, 1):
                op = ctx.getChild(index).getText()
                right = self.visit(ctx.search_condition_not(i))
                left = LogicalExpression(operator=op, leftArg=left, rightArg=right, isUnary=False)
                index += 2
            right = self.visit(ctx.search_condition_not(len_-1))
            op = ctx.getChild(index).getText()
            result = LogicalExpression(operator=op, leftArg=left, rightArg=right, isUnary=False)
        return result

    def visitSearch_condition_not(self, ctx):
        expr = self.visit(ctx.predicate())
        result = LogicalExpression(operator=ctx.NOT().getText().upper(), leftArg=expr, isUnary=True) if ctx.NOT() else expr
        return result

    # Predicate start.
    def visitPredicate(self, ctx):
        if ctx.EXISTS():
            subquery = self.visit(ctx.subquery())
            return ExistsExpression(subquery=subquery)
        elif ctx.search_condition():
            return self.visit(ctx.search_condition())
        elif ctx.comparison_operator():
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1)) if len(ctx.expression()) == 2 else self.visit(ctx.subquery())
            comparison_operator = self.visit(ctx.comparison_operator())
            return ComparisonPredicate(comparison_operator, left, right)
        else:
            value = self.visit(ctx.expression(0))
            is_not = True if ctx.NOT() else False
            if ctx.BETWEEN():
                left = self.visit(ctx.expression(1))
                right = self.visit(ctx.expression(2))
                result = BetweenPredicate(isNot=is_not, value=value, leftArg=left, rightArg=right)
            elif ctx.IN():
                subquery = None
                is_subquery = False
                value_list = None
                subquery_tree = ctx.subquery()
                if subquery_tree:
                    is_subquery = True
                    subquery = self.visit(subquery_tree)
                expression_list_tree = ctx.expression_list()
                if expression_list_tree:
                    value_list = self.visit(expression_list_tree)
                result = InPredicate(isSubquery=is_subquery, isNot=is_not, subquery=subquery, comparableValue=value,
                                     comparedValues=value_list)
            elif ctx.LIKE():
                pattern = self.visit(ctx.expression(1))
                escape = self.visit(ctx.expression(2)) if ctx.ESCAPE() else None
                result = LikePredicate(isNot=is_not, typeLike="LIKE", value=value,
                                       pattern=pattern, escapeString=escape)
            else:
                is_not = self.visit(ctx.null_notnull()) if ctx.null_notnull() else None
                result = IsNullPredicate(isNot=is_not, value=value)
        return result

    # Predicate end.

    def visitNull_notnull(self, ctx):
        return True if ctx.NOT() else False

    def visitComparison_operator(self, ctx):
        return ctx.getText()

    # Expression start.

    def visitPrimitive_expression(self, ctx):
        # need fix
        if ctx.DEFAULT():
            result = KeywordPrimitive("DEFAULT")
        elif ctx.NULL():
            result = NullLiteral("null")
        elif ctx.LOCAL_ID():
            result = Identifier(ctx.LOCAL_ID().getText())
        else:
            result = self.visit(ctx.constant())
        return result

    def visitFunction_call_expression(self, ctx):
        # need fix return statement
        if ctx.function_call():
            result = self.visit(ctx.function_call())
        else:
            result = self.visit(ctx.expression())
            id_ = self.visit(ctx.id_())
        return result

    def visitCase_expression(self, ctx):
        cases = []
        expression = self.visit(ctx.caseExpr) if ctx.caseExpr else None
        else_case = self.visit(ctx.elseExpr) if ctx.elseExpr else None
        cntCases = len(ctx.switch_section())
        for index in range(cntCases):
            when_ = self.visit(ctx.switch_section(index).expression(0))
            then_ = self.visit(ctx.switch_section(index).expression(1))
            cases.append(CaseClause(when_=when_, then_=then_))
        cntCases = len(ctx.switch_search_condition_section())
        for index in range(cntCases):
            when_ = self.visit(ctx.switch_search_condition_section(index).search_condition())
            then_ = self.visit(ctx.switch_search_condition_section(index).expression())
            cases.append(CaseClause(when_=when_, then_=then_))
        return CaseFunctionCall(expression=expression, cases=cases, elseCase=else_case)

    def visitColumn_ref_expression(self, ctx):
        return self.visit(ctx.full_column_name())

    def visitBracket_expression(self, ctx):
        return self.visit(ctx.expression())

    def visitSubquery_expression(self, ctx):
        return self.visit(ctx.subquery())

    def visitUnary_operator_expression(self, ctx):
        expr = self.visit(ctx.expression())
        op = ctx.getChild(0).getText()
        return UnaryExpression(op, expr)

    def visitBinary_operator_expression(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.op:
            op = ctx.getChild(1).getText()
            if op == '=':
                op = '=='
            result = BinaryExpression(op, left, right)
        elif ctx.comparison_operator():
            comparison_operator = self.visit(ctx.comparison_operator())
            result = ComparisonPredicate(comparison_operator, left, right)
        return result

    def visitOver_clause_expression(self, ctx):
        return self.visit(ctx.over_clause)

    def visitConstant_expression(self, ctx):
        if ctx.NULL():
            result = NullLiteral("null")
        elif ctx.constant():
            result = self.visit(ctx.constant())
        elif ctx.function_call():
            result = self.visit(ctx.function_call())
        elif ctx.constant_expression():
            result = self.visit(ctx.constant_expression())
        else:
            result = Identifier(ctx.LOCAL_ID().getText())
        return result

    def visitSubquery(self, ctx):
        return self.visit(ctx.select_statement())

    def visitWith_expression(self, ctx):
        with_expressions = []
        for index in range(len(ctx.common_table_expression())):
            with_expressions.append(self.visit(ctx.common_table_expression(index)))
        return with_expressions

    #  Expression end.

    def visitFull_column_name(self, ctx):
        schema = None
        table = None
        column = self.visit(ctx.id_())
        if ctx.table_name():
            if ctx.table_name().database:
                database = Identifier(ctx.table_name().database.getText())
            if ctx.table_name().schema:
                schema = Identifier(ctx.table_name().schema.getText())
            if ctx.table_name().table:
                table = Identifier(ctx.table_name().table.getText())
        result = ColumnName(schema=schema, table=table, column=column)
        if ctx.id_().getText()[0] == "\"" and ctx.id_().getText()[-1] == "\"":
            result = StringLiteral(ctx.id_().getText()[1:-1])
        return result

    def visitColumn_name_list_with_order(self, ctx):
        column_name_list_with_orders = []
        const = 1
        child_count = ctx.getChildCount()
        i = 0
        while i < child_count:
            node = ctx.getChild(i)
            if not isinstance(node, TerminalNode):
                column_name = self.visit(node)
                sort_type = None
                i += 1
                if i < child_count:
                    next_node = ctx.getChild(i)
                    if next_node.getText() != ",":
                        sort_type = next_node.getText()
                column_name_list_with_orders.append(IndexColNameClause(columnName=column_name, sortType=sort_type))
            i +=1
        return column_name_list_with_orders

    def visitColumn_name_list(self, ctx):
        column_name_lists = []
        for index in range(len(ctx.id_())):
            column_name_lists.append(ColumnName(column=self.visit(ctx.id_(index))))
        return column_name_lists

    def visitCursor_name(self, ctx):
        return Identifier(ctx.getChild(0).getText())

    def visitConstant(self, ctx):
        #  need add dollar
        if ctx.STRING():   # string, datetime or uniqueidentifier
            result = StringLiteral(ctx.getText())
        elif ctx.BINARY():
            result = HexadecimalLiteral(ctx.getText())
        elif ctx.dollar:
            result = StringLiteral(ctx.getText())
        elif ctx.DECIMAL():
            result = NumberLiteral(ctx.getText())
            if ctx.sign():
                result = UnaryExpression(ctx.sign().getChild(0).getText(), NumberLiteral(ctx.getChild(1).getText()))
        else:
            result = RealLiteral(ctx.getText())
            if ctx.sign():
                result = UnaryExpression(ctx.sign().getChild(0).getText(), RealLiteral(ctx.getChild(1).getText()))
        return result

    def visitId_(self, ctx):
        id_ = ctx.simple_id().getText() if ctx.simple_id() else ctx.getText()
        return Identifier(id_)

    def visitOver_clause(self, ctx):
        partition_by = None
        order_by = None
        range_ = None
        if ctx.expression_list():
            partition_by = self.visit(ctx.expression_list())
        if ctx.order_by_clause():
            order_by = self.visit(ctx.order_by_clause())
        if ctx.row_or_range_clause():
            range_ = self.visit(ctx.row_or_range_clause())
        return OverClause(partitionByElems=partition_by, orderByElems=order_by, rangeElems=range_)

    def visitRow_or_range_clause(self, ctx):
        result = self.visit(ctx.window_frame_extent())
        return result

    def visitWindow_frame_extent(self, ctx):
        arg = []
        if ctx.window_frame_preceding():
            arg_1, arg_2 = self.visit(ctx.window_frame_preceding())
            arg.append(FuncExtExprArgument(value=arg_1))
            arg.append(FuncExtExprArgument(value=arg_2))
        if ctx.window_frame_bound():
            arg_1, arg_2 = self.visit(ctx.window_frame_bound(0))
            arg.append(FuncExtExprArgument(value=arg_1, keyword='BETWEEN', keywordPosition='BEFORE'))
            arg.append(FuncExtExprArgument(value=arg_2, keyword='AND', keywordPosition='AFTER'))
            arg_1, arg_2 = self.visit(ctx.window_frame_bound(1))
            arg.append(FuncExtExprArgument(value=arg_1, keyword='AND', keywordPosition='BEFORE'))
            arg.append(FuncExtExprArgument(value=arg_2))
        return arg

    def visitWindow_frame_bound(self, ctx):
        arg_1, arg_2 = None, None
        if ctx.window_frame_preceding():
            arg_1, arg_2 = self.visit(ctx.window_frame_preceding())
        elif ctx.window_frame_following():
            arg_1, arg_2 = self.visit(ctx.window_frame_following())
        return arg_1, arg_2

    def visitWindow_frame_preceding(self, ctx):
        return ctx.getChild(0).getText(), ctx.getChild(1).getText()

    def visitWindow_frame_following(self, ctx):
        return ctx.getChild(0).getText(), ctx.getChild(1).getText()

        #  DDL start
        #  # Create block start
        #  ## Create table start

    def visitCreate_table(self, ctx):
        id_1 = None
        id_2 = None
        table = self.visit(ctx.table_name())
        columns, constraints = self.visit(ctx.column_def_table_constraints())
        options = self.visit(ctx.table_options()) if ctx.table_options() else []
        if ctx.id_():
            id_1 = self.visit(ctx.id_(0))
            if len(ctx.id_()) > 1:
                id_2 = self.visit(ctx.id_(1))
        return CreateTableColumnStatement(columns=columns, constraints=constraints, table=table, optionSet=options)

    def visitTable_options(self, ctx):
        options = []
        for index in range(len(ctx.index_option())):
            options.append(self.hlp_index_option_tree(ctx.index_option(index)))
        return options

    def visitColumn_def_table_constraints(self, ctx):
        columns = []
        constraints = []
        column_definitions_tree = ctx.column_def_table_constraint()
        for index in range(len(column_definitions_tree)):
            column_def, constraint_def = self.visit(column_definitions_tree[index])
            if column_def is not None:
                columns.append(column_def)
            if constraint_def is not None:
                constraints.append(constraint_def)
        return columns, constraints

    def visitColumn_definition(self, ctx):
        # need fix column_constraint
        name = Identifier(ctx.getChild(0).getText())
        constraint = None
        is_unique = None
        is_primary = None
        ref_def = None
        data_type = self.help_for_data_type(ctx.data_type()) if ctx.data_type() else self.visit(ctx.expression())
        is_not = self.visit(ctx.null_notnull()) if ctx.null_notnull() else None
        with_value = True if ctx.VALUES() else False
        if len(ctx.id_()) > 1 and ctx.COLLATE() is not None:
            id_collete = self.visit(ctx.id_(1))
        if ctx.constraint:
            constraint = ctx.constraint
        if ctx.constant_expression():
            constant_expression = self.visit(ctx.constant_expression())
        if ctx.IDENTITY():
            seed = ctx.seed if ctx.seed else None
            increment = ctx.increment if ctx.increment else None
            not_for_replication = True if ctx.REPLICATION() else False  # need add to ast
        rowguidcol = True if ctx.ROWGUIDCOL() else False  # need add to ast
        if len(ctx.column_constraint()):
            for index in range(len(ctx.column_constraint())):
                if ctx.column_constraint(index).CHECK():
                    return self.visit(ctx.column_constraint(index))
                id_constraint, is_not, is_unique, is_primary, clustered, index_options, ref_def = self.visit(ctx.column_constraint(index))
        return ColumnDefClause(name=name, dataType=data_type, isNotNull=is_not, isUnique=is_unique, isPrimary=is_primary, refDef=ref_def), None

    def help_for_data_type(self, data):
        data_type, first_dim, second_dim, charset = self.visit(data)
        result = None
        # Exact Numerics
        if data_type == "bigint" or data_type == "bit" or data_type == "decimal" or data_type == "int"\
                or data_type == "money" or data_type == "numeric" or data_type == "smallint"\
                or data_type == "smallmoney" or data_type == "tinyint":  # need add data_type money
            result = DimensionDataTypeClause(typeName=data_type, length=first_dim, secondLength=second_dim)

        # Approximate Numerics
        elif data_type == "float" or data_type == "real":
            result = DimensionDataTypeClause(typeName=data_type, length=first_dim, secondLength=second_dim)

        # Date and Time
        elif data_type == "date" or data_type == "datetime2" or data_type == "datetime"\
                or data_type == "datetimeoffset" or data_type == "smalldatetime" or data_type == "time":
            result = SimpleDataTypeClause(typeName=data_type)
            if data_type == "time" or data_type == "datetimeoffset" or data_type == "datetime2":
                result = DimensionDataTypeClause(typeName=data_type, length=first_dim, secondLength=second_dim)

        #  Character Strings
        elif data_type == "varchar" or data_type == "char" or data_type == "text":
            result = CharDataTypeClause(typeName=data_type, length=first_dim)

        # Unicode Character Strings
        elif data_type == "nchar" or data_type == "nvarchar" or data_type == "ntext":
            result = CharDataTypeClause(typeName=data_type, length=first_dim)

        # Binary Strings
        elif data_type == "binary" or data_type == "varbinary" or data_type == "image":
            result = DimensionDataTypeClause(typeName=data_type, length=first_dim, secondLength=second_dim)
        return result

    def foreignkey_build(self, ctx):
        refdef = None
        if ctx.REFERENCES():
            table_name = None
            indexcolumns = None
            ondelete = ctx.on_delete().getText().lower() if ctx.on_delete() else None
            onupdate = ctx.on_update().getText().lower() if ctx.on_update() else None
            icolumns = []
            column_name_list = self.visit(ctx.pk)
            table_name = self.visit(ctx.table_name())
            for index in range(len(column_name_list)):
                icolumns.append(IndexColNameClause(columnName=column_name_list[index].column))
            if not(ondelete is None):
                ondelete = ondelete.replace("ondelete", "").lstrip()
            if not(onupdate is None):
                onupdate = onupdate.replace("onupdate", "").lstrip()
            refdef = ReferenceDefClause(table=table_name, indexColumns=icolumns, onDelete=ondelete, onUpdate=onupdate)
        return refdef

    def visitColumn_constraint(self, ctx):
        id_constraint = None
        clustered = None
        index_options = None
        if ctx.CHECK():
            expr = self.visit(ctx.search_condition())
            return ConstraintCheckClause(expression=expr), None
        if ctx.CONSTRAINT():
            id_constraint = self.visit(ctx.id_())
        is_not = self.visit(ctx.null_notnull()) if ctx.null_notnull() else None
        is_unique = True if ctx.UNIQUE() else False
        is_primary = True if ctx.PRIMARY() else False
        ref_def = self.foreignkey_build(ctx) if ctx.REFERENCES() else None
        if ctx.clustered():
            clustered = self.visit(ctx.clustered())  # def if UNIQUE - NONCLUSTERED if PRIMARY KEY - CLUSTERED
        if ctx.index_options():
            index_options = self.visit(ctx.index_options())

        return id_constraint, is_not, is_unique, is_primary, clustered, index_options, ref_def

    def visitTable_constraint(self, ctx):
        if ctx.CHECK():
            expr = self.visit(ctx.search_condition())
            return None, ConstraintCheckClause(expression=expr)
        name = None
        on = None  # ?
        iopt = None
        if ctx.id_():
            if len(ctx.id_()) == 1 and ctx.CONSTRAINT() is not None:
                name = Identifier(ctx.id_(0).getText())
            elif len(ctx.id_()) > 1 and ctx.CONSTRAINT() is not None:
                name = Identifier(ctx.id_(0).getText())
                on = Identifier(ctx.id_(1).getText())
            else:
                on = Identifier(ctx.id_().getText())
        key_type_index = 2 if ctx.getChild(0).getText().lower() == 'constraint' else 0  # ?
        key_type = ctx.getChild(key_type_index).getText()
        icolumns = []
        column_name_list = []
        if ctx.clustered():    # need add to AST
            clustered = self.visit(ctx.clustered())
        # different object name for FOREIGN KEY and other key
        if ctx.FOREIGN():
            column_name_list = self.visit(ctx.fk)
        else:
            # TODO: make static choise
            if isinstance(ctx.column_name_list(), list):
                column_name_list = self.visit(ctx.column_name_list(0))
            else:
                column_name_list = self.visit(ctx.column_name_list())
        sort_type = "asc" if ctx.ASC() else None
        sort_type = "desc" if ctx.DESC() else sort_type
        for index in range(len(column_name_list)):
            icolumns.append(IndexColNameClause(columnName=column_name_list[index].column, sortType=sort_type))
        if ctx.index_options():
            iopt = self.visit(ctx.index_options())
        refdef = self.foreignkey_build(ctx) if ctx.REFERENCES() else None
        return None, ConstraintKeyClause(name=name, keyType=key_type, indexColumns=icolumns, indexOptionSet=iopt, refDef=refdef)

    #  ## Other create start

    def visitCreate_database(self, ctx):
        # need describe primary
        # need describe containment
        # need describe database_option
        # need fix database_file_spec
        collate = None
        primary = False
        containment = None
        database_file_specs = []
        handle_type = "create"
        db_name = DbName(schema=Identifier(ctx.database.getText()))
        containment = ctx.NONE().getText() if ctx.NONE() else None
        containment = ctx.PARTIAL().getText() if ctx.PARTIAL() else containment
        if ctx.database_file_spec():
            if ctx.PRIMARY():
                primary = True
            for index in range(len(ctx.database_file_spec())):
                database_file_spec = self.visit(ctx.database_file_spec(index))
                database_file_specs.append(database_file_spec)
            if ctx.LOG():
                pass
        if ctx.collation_name:
            collate = ctx.collation_name.getText()
        if ctx.create_database_option():
            default_lang, default_fulltext_lang, nested_triggers, transform_noise_words, two_digit_year_cutoff, db_chaining, trustworthy = self.hlp_database_option(ctx.create_database_option())
        return HandleDatabaseStatement(handleType=handle_type, dbName=db_name, collate=collate)

    def hlp_database_option(self, options):
        # need fix filestream_option
        default_lang = None
        default_fulltext_lang = None
        nested_triggers = None
        transform_noise_words = None
        two_digit_year_cutoff = None
        db_chaining = None
        trustworthy = None
        for index in range(len(options)):
            cur_char = options[index]
            if len(options.database_filestream_option()):
                for next_database_filestream_option in options.database_filestream_option():
                    if next_database_filestream_option.NON_TRANSACTED_ACCESS():
                        non_transacted_accsess = next_database_filestream_option.getChild(2).getText()
                    if next_database_filestream_option.DIRECTORY_NAME():
                        directory_name = next_database_filestream_option.getChild(2).getText()
            if cur_char.DEFAULT_LANGUAGE():
                default_lang = self.visit(options.id_()) if options.id_() else None
                default_lang = options.STRING().getText() if options.STRING() else default_lang
            if cur_char.DEFAULT_FULLTEXT_LANGUAGE():
                default_fulltext_lang = self.visit(options.id_()) if options.id_() else None
                default_fulltext_lang = options.STRING().getText() if options.STRING() else default_fulltext_lang
            if cur_char.NESTED_TRIGGERS():
                nested_triggers = options.OFF().getText() if options.OFF() else None
                nested_triggers = options.ON().getText() if options.ON() else nested_triggers
            if cur_char.TRANSFORM_NOISE_WORDS():
                transform_noise_words = options.OFF().getText() if options.OFF() else None
                transform_noise_words = options.ON().getText() if options.ON() else transform_noise_words
            if cur_char.TWO_DIGIT_YEAR_CUTOFF():
                two_digit_year_cutoff = options.DECIMAL().getText() if options.DECIMAL() else None
                two_digit_year_cutoff = options.ON().getText() if options.ON() else two_digit_year_cutoff
            if cur_char.DB_CHAINING():
                db_chaining = options.OFF().getText() if options.OFF() else None
                db_chaining = options.ON().getText() if options.ON() else db_chaining
            if cur_char.TRUSTWORTHY():
                trustworthy = options.OFF().getText() if options.OFF() else None
                trustworthy = options.ON().getText() if options.ON() else trustworthy
        return default_lang, default_fulltext_lang, nested_triggers, transform_noise_words, two_digit_year_cutoff, db_chaining, trustworthy

    def visitCreate_index(self, ctx):
        # need describe clustered
        # need describe where_clauses
        # need describe include
        # need describe partition
        partition = None
        clustered = None
        column_name_list = None
        where_clauses = None
        iopts = None
        category = "unique" if ctx.UNIQUE() else None
        index_name = self.visit(ctx.id_(0))
        table_name, table_hint = self.visit(ctx.table_name_with_hint())
        icols = self.visit(ctx.column_name_list_with_order())
        if ctx.INCLUDE():
            column_name_list = self.visit(ctx.column_name_list())
        if ctx.clustered():
            clustered = self.visit(ctx.clustered())
        if ctx.search_condition():
            where_clauses = WhereClause(value=self.visit(ctx.search_condition()))
        if ctx.index_options():
            iopts = self.visit(ctx.index_options())
        if len(ctx.id_()) > 1:
            partition = self.visit(ctx.id_(1))
        return CreateIndexStatement(
            category=category, name=index_name, table=table_name, indexColumns=icols,
            indexOptionSet=iopts,
        )

    def visitIndex_options(self, ctx):
        return self.hlp_index_option_tree(ctx.index_option())

    def hlp_index_option_tree(self, options_tree):
        # need add relational_index_option! - https://docs.microsoft.com/en-us/sql/t-sql/statements/create-index-transact-sql
        ioptions = IndexOptionSet()
        length_options_tree = len(options_tree)
        for index in range(length_options_tree):
            pass
        return ioptions

    def visitCreate_or_alter_function(self, ctx):
        # need describe type_(create_or_alter)
        # need describe return stmt
        params = []
        body = None
        return_type = None
        returns_param = None
        type_ = ctx.getChild(0).getText()
        schema_name, routine_name = self.visit(ctx.func_proc_name())  # don't forget about database
        routine = UDFuncName(schema=schema_name, routine=routine_name)
        for index in range(len(ctx.procedure_param())):
            params.append(self.visit(ctx.procedure_param(index)))
        index = ctx.getChildCount() - 1
        if ctx.func_body_returns_select():
            body, data_type, returns_null_on_null_input, called_on_null_input, execute_clause = self.hlp_routine_returns(ctx.getChild(index), 'select')
        elif ctx.func_body_returns_table():
            body, data_type, returns_null_on_null_input, called_on_null_input, execute_clause = self.hlp_routine_returns(ctx.getChild(index), 'table')
        else:
            body, data_type, returns_null_on_null_input, called_on_null_input, execute_clause = self.hlp_routine_returns(ctx.getChild(index), 'scalar')
        return CreateFuncStatement(
            function=routine, params=params, body=body, returnType=data_type
            )

    def visitFunc_proc_name(self, ctx):
        # need describe database
        database = Identifier(ctx.database.getText()) if ctx.database else None
        schema = Identifier(ctx.schema.getText()) if ctx.schema else None
        procedure = Identifier(ctx.procedure.getText()) if ctx.procedure else None
        return schema, procedure

    def visitProcedure_param(self, ctx):
        # need describe AS
        # need describe VARYING
        # need describe id_
        # need describe default_val
        # direction=type_ ?
        id_ = None
        default_val = None
        as_ = False
        varying = False
        type_ = None
        name = Identifier(ctx.LOCAL_ID().getText())
        if ctx.id_():
            id_ = self.visit(ctx.id_())
        data_type = self.help_for_data_type(ctx.data_type())
        if ctx.default_val:
            default_val = ctx.default_val.getText()
        if ctx.AS():
            as_ = True
        if ctx.VARYING():
            varying = True
        type_ = "out" if ctx.OUT() else None
        type_ = "output" if ctx.OUTPUT() else type_
        type_ = "readonly" if ctx.READONLY() else type_
        return RoutineParameter(direction=type_, name=name, dataType=data_type)

    def hlp_routine_returns(self, returns, return_type):
        #  need describe as
        #  need describe LOCAL_ID
        #  need describe table_type_definition
        #  need describe ret
        #  need add more type return stm for ast?
        data_type = None
        as_ = False
        ret = None
        table_type_definition = None
        local_id = None
        columns = None
        constraints = None
        body = []
        returns_null_on_null_input, called_on_null_input, execute_clause = self.hlp_function_options(returns.function_option())
        if returns.AS():
            as_ = True
        if return_type == 'select':
            body.append(self.visit(returns.select_statement()))
        else:
            for index in range(len(returns.sql_clause())):
                body.append(self.visit(returns.sql_clause(index)))
            if return_type == 'table':
                local_id = Identifier(returns.LOCAL_ID().getText())
                columns, constraints = self.visit(returns.table_type_definition())
            else:
                data_type = self.help_for_data_type(returns.data_type())
                if returns.ret:
                    ret = returns.ret.getText()
        body = BlockQueryStatement(bodyStatements=body)
        return body, data_type, returns_null_on_null_input, called_on_null_input, execute_clause

    def visitTable_type_definition(self, ctx):
        columns, constraints = self.visit(ctx.column_def_table_constraints())
        return columns, constraints

    def visitCreate_or_alter_procedure(self, ctx):
        # need describe for_replication
        # need describe decimal
        # need describe type_(create_or_alter)
        # need describe proc ?
        # need describe  encryption, recompile, execute_clause
        params = []
        decimal = None
        for_replication = False
        type_ = ctx.getChild(0).getText()
        proc = "proc" if ctx.PROC() else None
        proc = "procedure" if ctx.PROCEDURE() else proc
        schema_name, routine_name = self.visit(ctx.func_proc_name())  # don't forget about database
        routine = ProcedureName(schema=schema_name, routine=routine_name)
        if ctx.DECIMAL():
            decimal = ctx.DECIMAL().getText()
        for index in range(len(ctx.procedure_param())):
            params.append(self.visit(ctx.procedure_param(index)))
        if ctx.REPLICATION():
            for_replication = True
        body = self.visit(ctx.sql_clauses())
        encryption, recompile, execute_clause = self.hlp_procedure_options(ctx.procedure_option())
        return CreateProcStatement(procedure=routine, params=params, body=body)

    def visitProcedure_option(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitExecute_clause(self, ctx):
        # need describe
        return ctx.clause.getText()

    def visitDeclare_local(self, ctx):
        # need describe!
        expr_1 = Identifier(ctx.LOCAL_ID().getText())
        data_type = self.help_for_data_type(ctx.data_type())
        expr_2 = self.visit(ctx.expression()) if ctx.expression() else None

    @staticmethod
    def hlp_procedure_options(options):
        encryption = None
        recompile = None
        execute_clause = None
        for index in range(len(options)):
            cur_char = options[index]
            if cur_char.ENCRYPTION():
                encryption = cur_char.ENCRYPTION().getText()
            if cur_char.RECOMPILE():
                recompile = cur_char.RECOMPILE().getText()
            if cur_char.execute_clause():
                execute_clause = cur_char.execute_clause.clause.getText()
        return encryption, recompile, execute_clause

    @staticmethod
    def hlp_function_options(options):
        # need describe returns/called
        returns_null_on_null_input = None
        called_on_null_input = None
        execute_clause = None
        for index in range(len(options)):
            cur_char = options[index]
            if cur_char.RETURNS():
                returns_null_on_null_input = "returns_null_on_null_input"
            if cur_char.CALLED():
                called_on_null_input = "called_on_null_input"
            if cur_char.execute_clause():
                execute_clause = cur_char.execute_clause.clause.getText()
        return returns_null_on_null_input, called_on_null_input, execute_clause

    def visitCreate_or_alter_trigger(self, ctx):
        # 2 type trigger
        return self.visit(ctx.getChild(0))

    def visitDml_trigger(self, ctx):
        # event - list, mb more than 1
        # need describe not_for_replication
        # need describe with_append
        # need describe type_
        # need fix time
        # need  describe option
        with_append = False
        not_for_replication = False
        type_ = ctx.getChild(0).getText()
        schema_name, trigger_name = self.visit(ctx.simple_name())
        trigger = TriggerName(schema=schema_name, trigger=trigger_name)
        table_name = self.visit(ctx.table_name())
        event = self.hlp_trigger_event(ctx.dml_trigger_operation())
        body = self.visit(ctx.sql_clauses())
        time = ctx.FOR().getText() if ctx.FOR() else None
        time = ctx.AFTER().getText() if ctx.AFTER() else time
        time = ctx.INSTEAD().getText() if ctx.INSTEAD() else time
        encryption, execute_clause = self.hlp_trigger_option(ctx.dml_trigger_option())
        if ctx.REPLICATION():
            not_for_replication = True
        if ctx.APPEND():
            with_append = True
        return CreateTriggerStatement(
            name=trigger, table=table_name, time=time, event=event, body=body,
        )

    def visitDdl_trigger(self, ctx):
        # need  describe option
        # event - list, mb more than 1
        # need describe type_
        type_ = ctx.getChild(0).getText()
        schema_name, trigger_name = self.visit(ctx.simple_name())
        trigger = TriggerName(schema=schema_name, trigger=trigger_name)
        body = self.visit(ctx.sql_clauses())
        encryption, execute_clause = self.hlp_trigger_option(ctx.dml_trigger_option())
        table_name = ctx.SERVER().getText() if ctx.SERVER() else None
        table_name = ctx.DATABASE().getText() if ctx.DATABASE() else table_name
        time = ctx.FOR().getText() if ctx.FOR() else None
        time = ctx.AFTER().getText() if ctx.AFTER() else time
        event = self.hlp_trigger_event(ctx.dml_trigger_operation())
        return CreateTriggerStatement(
            name=trigger, table=table_name, time=time, event=event, body=body,
        )

    @staticmethod
    def hlp_trigger_event(events):
        event = []
        for index in range(len(events)):
            cur_char = events[index]
            event.append(cur_char.getChild(0).getText())
        return event

    @staticmethod
    def hlp_trigger_option(options):
        encryption = None
        execute_clause = None
        for index in range(len(options)):
            cur_char = options[index]
            if cur_char.ENCRYPTION():
                encryption = cur_char.ENCRYPTION().getText()
            if cur_char.execute_clause():
                execute_clause = cur_char.execute_clause.clause.getText()
        return encryption, execute_clause

    def visitCreate_view(self, ctx):
        # need describe attribute
        handle_type = "create"
        schema_name, view_name = self.visit(ctx.simple_name())
        view = ViewName(schema=schema_name, view=view_name)
        cols = self.visit(ctx.column_name_list()) if ctx.column_name_list() else []
        select_stmt = self.visit(ctx.select_statement())
        encryption, schema_binding, view_metadata = self.hlp_view_attribute(ctx.view_attribute())
        opt = "with_check_option" if ctx.OPTION() else ""
        return HandleViewStatement(
            handleType=handle_type, name=view, columns=cols, select=select_stmt, checkOption=opt
        )

    @staticmethod
    def hlp_view_attribute(attributes):
        encryption = None
        schema_binding = None
        view_metadata = None
        for index in range(len(attributes)):
            cur_char = attributes[index]
            if cur_char.ENCRYPTION():
                encryption = cur_char.ENCRYPTION().getText()
            if cur_char.SCHEMABINDING():
                schema_binding = cur_char.SCHEMABINDING().getText()
            if cur_char.VIEW_METADATA():
                view_metadata = cur_char.VIEW_METADATA().getText()
        return encryption, schema_binding, view_metadata
