from aule.generated.sqlASTListener import ASTListener
from aule.generated.sqlAST import Identifier

# Types
from typing import List, Dict


class SQLProfileListener(ASTListener):
    """ This class retrieves profile data from SQL query.
    """

    def __init__(self) -> None:
        self.flow_control_functions_names = ["if", "ifnull", "nullif"]
        self.service_schemas = ["mysql", "information_schema"]
        self.current_query_level = 0
        self.stack_query_level: List[int] = []
        self.is_union_context = False
        self.stack_union_context: List[bool] = []
        self.generator_query_id = 1
        self.current_query_context_id = 0
        self.stack_query_context: List[int] = []
        self.column_clause_context: bool = None
        self.start_subquery_insert_depth: int = None
        self.start_subquery_update_depth: int = None
        self.start_subquery_select_depth: int = None
        self.start_subquery_delete_depth: int = None

        # Target attributes
        self.is_start_insert = False
        self.is_start_update = False
        self.is_start_select = False
        self.is_start_delete = False
        self.is_insert_context = False
        self.is_update_context = False
        self.is_select_context = False
        self.is_delete_context = False
        self.is_valid = False
        self.is_subquery: bool = None
        self.is_union: bool = None
        self.is_insert_subquery: bool = None
        self.is_update_subquery: bool = None
        self.is_delete_subquery: bool = None
        self.is_hex: bool = None
        self.is_constant: bool = None
        self.is_rw_file: bool = None
        self.is_exec_os_command: bool = None
        self.is_stacked_queries: bool = None
        self.is_comment: bool = None
        self.is_sys_entity: bool = None
        self.is_variable: bool = None
        self.is_routine_proc: bool = None
        self.is_logical_operator: bool = None
        self.max_subquery_depth: int = None
        self.max_insert_depth: int = None
        self.max_update_depth: int = None
        self.max_select_depth: int = None
        self.max_delete_depth: int = None
        self.max_union_len: int = None
        self.max_db_len: int = None
        self.max_entity_len: int = None
        self.max_schema_len: int = None
        self.max_table_len: int = None
        self.max_column_len: int = None
        self.max_routine_len: int = None
        self.max_variable_len: int = None
        self.max_columns: int = None
        self.function_names: Dict = None
        self.is_flow_control_func: bool = None

    def get_results(self) -> Dict:
        functions = list(self.function_names.keys()) if self.function_names else None
        return {
            "is_valid": self.is_valid,
            "is_subquery": self.is_subquery,
            "is_union": self.is_union,
            "is_insert_subquery": self.is_insert_subquery,
            "is_update_subquery": self.is_update_subquery,
            "is_delete_subquery": self.is_delete_subquery,
            "max_subquery_depth": self.max_subquery_depth,
            "max_insert_depth": self.max_insert_depth,
            "max_update_depth": self.max_update_depth,
            "max_select_depth": self.max_select_depth,
            "max_delete_depth": self.max_delete_depth,
            "max_union_len": self.max_union_len,
            "max_entity_len": self.max_entity_len,
            "max_db_len": self.max_db_len,
            "max_schema_len": self.max_schema_len,
            "max_table_len": self.max_table_len,
            "max_column_len": self.max_column_len,
            "max_routine_len": self.max_routine_len,
            "max_variable_len": self.max_variable_len,
            "max_columns": self.max_columns,
            "functions": functions,
            "is_flow_control_func": self.is_flow_control_func,
            "is_hex": self.is_hex,
            "is_constant": self.is_constant,
            "is_rw_file": self.is_rw_file,
            "is_exec_os_command": self.is_exec_os_command,
            "is_stacked_queries": self.is_stacked_queries,
            "is_comment": self.is_comment,
            "is_sys_entity": self.is_sys_entity,
            "is_variable": self.is_variable,
            "is_routine_proc": self.is_routine_proc,
            "is_logical_operator": self.is_logical_operator
        }

    # Tree walker start
    # Root methods start
    def enterScript(self, ctx) -> None:
        self.function_names = {}
        self.is_comment = ctx.isCommented
        self.max_subquery_depth = 0
        self.max_insert_depth = 0
        self.max_update_depth = 0
        self.max_select_depth = 0
        self.max_delete_depth = 0
        self.max_union_len = 0
        self.max_db_len = 0
        self.max_entity_len = 0
        self.max_schema_len = 0
        self.max_table_len = 0
        self.max_column_len = 0
        self.max_routine_len = 0
        self.max_variable_len = 0
        self.max_columns = 0
        self.is_subquery = False
        self.is_insert_subquery = False
        self.is_select_subquery = False
        self.is_update_subquery = False
        self.is_delete_subquery = False
        self.is_union = False
        self.is_stacked_queries = False
        self.is_sys_entity = False
        self.is_hex = False
        self.is_exec_os_command = False
        self.is_routine_proc = False
        self.is_flow_control_func = False
        self.is_rw_file = False
        self.is_logical_operator = False
        self.is_variable = False
        self.is_constant = False
        self.is_stacked_queries = True if len(ctx.bodyStatements) > 1 else False


    def exitScript(self, ctx) -> None:
        # if we here hence SQL correct
        self.is_valid = True

        if self.max_insert_depth > 0:
            self.is_insert_subquery = True
        if self.max_update_depth > 0:
            self.is_update_subquery = True
        if self.max_delete_depth > 0:
            self.is_delete_subquery = True

    def statementCommonFirstActions(self, ctx) -> None:
        is_union = False
        is_next_query_level = False
        is_next_script_stmt = False

        # Check where we are? which context is used now? Union? Script? or next-level statement?
        if self.is_union_context:
            # Our context is "Next statement from UNION"
            is_union = True
        else:
            # we are NOT in union context!
            # check if we still in some existence context => that mean we deep into
            if self.current_query_context_id != 0:
                # Our context is "Deep into next subquery level"
                is_next_query_level = True
            else:
                # Our context is "next statement from Script"
                is_next_script_stmt = True

        # Save stack-values in stack
        # save query_level
        self.stack_query_level.append(self.current_query_level)
        # save union_context
        self.stack_union_context.append(self.is_union_context)
        # save id of previous level query
        self.stack_query_context.append(self.current_query_context_id)

        # Define current statement parameters
        # level_up if necessary
        if is_next_query_level:
            self.current_query_level += 1
        # Generate next id from generator
        self.current_query_context_id = self.generator_query_id
        # increment generator
        self.generator_query_id += 1
        # Clear union_context
        self.is_union_context = False

        # Define profiler's value "is_subquery"
        if self.current_query_level > 0:
            self.is_subquery = True

        # Save max level of subquery
        if self.max_subquery_depth < self.current_query_level:
            self.max_subquery_depth = self.current_query_level

        # Save max level for all subtypes
        # SELECT
        if self.is_select_context:
            if self.max_select_depth < (self.current_query_level - self.start_subquery_select_depth):
                self.max_select_depth = self.current_query_level - self.start_subquery_select_depth
        # INSERT
        if self.is_insert_context:
            if self.max_insert_depth < (self.current_query_level - self.start_subquery_insert_depth):
                self.max_insert_depth = self.current_query_level - self.start_subquery_insert_depth
        # UPDATE
        if self.is_update_context:
            if self.max_update_depth < (self.current_query_level - self.start_subquery_update_depth):
                self.max_update_depth = self.current_query_level - self.start_subquery_update_depth

        # DELETE
        if self.is_delete_context:
            if self.max_delete_depth < (self.current_query_level - self.start_subquery_delete_depth):
                self.max_delete_depth = self.current_query_level - self.start_subquery_delete_depth

    def statementAferwordActions(self, ctx) -> None:
        prev_is_union_context = self.stack_union_context.pop()
        prev_query_level = self.stack_query_level.pop()
        prev_query_id = self.stack_query_context.pop()

        # restore stack-values
        self.is_union_context = prev_is_union_context
        self.current_query_context_id = prev_query_id
        self.current_query_level = prev_query_level

        # if we back to root-level we must clear min-flags
        if self.current_query_context_id == 0:
            self.start_subquery_insert_depth = 0
            self.start_subquery_update_depth = 0
            self.start_subquery_select_depth = 0
            self.start_subquery_delete_depth = 0
            self.is_start_insert = False
            self.is_start_update = False
            self.is_start_select = False
            self.is_start_delete = False

    # Root-stack methods end

    # Root-stack dependent methods start
    def enterSelectStatement(self, ctx) -> None:
        # <Base class actions>
        self.statementCommonFirstActions(ctx)
        # </Base class actions>
        self.is_select_context = True
        # define start level for query
        if not self.is_start_select:
            self.is_start_select = True
            self.start_subquery_select_depth = self.current_query_level
        # max_columns
        if self.max_columns < len(ctx.columns):
            self.max_columns = len(ctx.columns)

    def exitSelectStatement(self, ctx) -> None:
        self.is_select_context = False
        # <Base class actions>
        self.statementAferwordActions(ctx)
        # </Base class actions>

    def enterUnionStatement(self, ctx) -> None:
        # <Base class actions>
        self.statementCommonFirstActions(ctx)
        # </Base class actions>

        self.is_select_context = True
        self.is_union_context = True
        # define start level for query
        if not self.is_start_select:
            self.is_start_select = True
            self.start_subquery_select_depth = self.current_query_level
        self.is_union = True
        if self.max_union_len < len(ctx.clauses):
            self.max_union_len = len(ctx.clauses)

    def exitUnionStatement(self, ctx) -> None:
        self.is_select_context = False
        # <Base class actions>
        self.statementAferwordActions(ctx)
        # </Base class actions>
    # Root-stack dependent methods end

    # Subquery determination methods start
    def enterInsertSetStatement(self, ctx) -> None:
        # <Base class actions>
        self.statementCommonFirstActions(ctx)
        # </Base class actions>
        self.is_insert_context = True
        # define start level for query
        if not self.is_start_insert:
            self.is_start_insert = True
            self.start_subquery_insert_depth = self.current_query_level

    def exitInsertSetStatement(self, ctx) -> None:
        self.is_insert_context = False
        # <Base class actions>
        self.statementAferwordActions(ctx)
        # </Base class actions>

    def enterInsertQueryStatement(self, ctx) -> None:
        # <Base class actions>
        self.statementCommonFirstActions(ctx)
        # </Base class actions>
        self.is_insert_context = True
        # define start level for query
        if not self.is_start_insert:
            self.is_start_insert = True
            self.start_subquery_insert_depth = self.current_query_level

    def exitInsertQueryStatement(self, ctx) -> None:
        self.is_insert_context = False
        # <Base class actions>
        self.statementAferwordActions(ctx)
        # </Base class actions>

    def enterInsertRowStatement(self, ctx) -> None:
        # <Base class actions>
        self.statementCommonFirstActions(ctx)
        # </Base class actions>
        self.is_insert_context = True
        # define start level for query
        if not self.is_start_insert:
            self.is_start_insert = True
            self.start_subquery_insert_depth = self.current_query_level

    def exitInsertRowStatement(self, ctx) -> None:
        self.is_insert_context = False
        # <Base class actions>
        self.statementAferwordActions(ctx)
        # </Base class actions>

    def enterUpdateSingleStatement(self, ctx) -> None:
        # <Base class actions>
        self.statementCommonFirstActions(ctx)
        # </Base class actions>
        self.is_update_context = True
        # define start level for query
        if not self.is_start_update:
            self.is_start_update = True
            self.start_subquery_update_depth = self.current_query_level

    def exitUpdateSingleStatement(self, ctx) -> None:
        self.is_update_context = False
        # <Base class actions>
        self.statementAferwordActions(ctx)
        # </Base class actions>

    def enterUpdateMultipleStatement(self, ctx) -> None:
        # <Base class actions>
        self.statementCommonFirstActions(ctx)
        # </Base class actions>
        self.is_update_context = True
        # define start level for query
        if not self.is_start_update:
            self.is_start_update = True
            self.start_subquery_update_depth = self.current_query_level

    def exitUpdateMultipleStatement(self, ctx) -> None:
        self.is_update_context = False
        # <Base class actions>
        self.statementAferwordActions(ctx)
        # </Base class actions>

    def enterDeleteSingleStatement(self, ctx) -> None:
        # <Base class actions>
        self.statementCommonFirstActions(ctx)
        # </Base class actions>
        self.is_delete_context = True
        # define start level for query
        if not self.is_start_delete:
            self.is_start_delete = True
            self.start_subquery_delete_depth = self.current_query_level

    def exitDeleteSingleStatement(self, ctx) -> None:
        self.is_delete_context = False
        
        # <Base class actions>
        self.statementAferwordActions(ctx)
        # </Base class actions>

    def enterDeleteMultipleStatement(self, ctx) -> None:
        # <Base class actions>
        self.statementCommonFirstActions(ctx)
        # </Base class actions>
        self.is_delete_context = True
        # define start level for query
        if not self.is_start_delete:
            self.is_start_delete = True
            self.start_subquery_delete_depth = self.current_query_level

    def exitDeleteMultipleStatement(self, ctx) -> None:
        self.is_delete_context = False
        # <Base class actions>
        self.statementAferwordActions(ctx)
        # </Base class actions>
    # Subquery determination methods end

    # Entity name's length start
    def enterIdentifier(self, ctx) -> None:
        if self.max_entity_len < len(ctx.name):
            self.max_entity_len = len(ctx.name)

    def enterColumnName(self, ctx) -> None:
        if ctx.schema:
            if self.max_schema_len < len(ctx.schema.name):
                self.max_schema_len = len(ctx.schema.name)
            if ctx.schema.name.lower() in self.service_schemas:
                self.is_sys_entity = True
        if ctx.table:
            if self.max_table_len < len(ctx.table.name):
                self.max_table_len = len(ctx.table.name)
        if type(ctx.column) == Identifier:
            if self.max_column_len < len(ctx.column.name):
                self.max_column_len = len(ctx.column.name)

    def enterTableName(self, ctx) -> None:
        if ctx.schema:
            if self.max_schema_len < len(ctx.schema.name):
                self.max_schema_len = len(ctx.schema.name)
            if ctx.schema.name.lower() in self.service_schemas:
                self.is_sys_entity = True
        if self.max_table_len < len(ctx.table.name):
            self.max_table_len = len(ctx.table.name)

    def enterDbName(self, ctx) -> None:
        if self.max_schema_len < len(ctx.schema.name):
            self.max_schema_len = len(ctx.schema.name)
        if ctx.schema.name.lower() in self.service_schemas:
            self.is_sys_entity = True

    def enterUDFuncName(self, ctx) -> None:
        self.is_routine_proc = True
        if ctx.schema:
            if self.max_schema_len < len(ctx.schema.name):
                self.max_schema_len = len(ctx.schema.name)
            if ctx.schema.name.lower() in self.service_schemas:
                self.is_sys_entity = True
        if self.max_routine_len < len(ctx.routine.name):
            self.max_routine_len = len(ctx.routine.name)
        # add UserDefinedFunction name in list of all routines
        self.add_routine_key(ctx, "ufunction")
            
    def enterProcedureName(self, ctx) -> None:
        self.is_routine_proc = True
        if ctx.schema:
            if self.max_schema_len < len(ctx.schema.name):
                self.max_schema_len = len(ctx.schema.name)
            if ctx.schema.name.lower() in self.service_schemas:
                self.is_sys_entity = True
        if self.max_routine_len < len(ctx.routine.name):
            self.max_routine_len = len(ctx.routine.name)
        # add procedure name in list of all routines
        self.add_routine_key(ctx, "procedure")

    # TODO: finish descriptions for all entities
    # Entity name's length end

    # Functions start
    def add_routine_key(self, ctx, routine_type) -> None:
        """ Create and add key identified routine in query.

        Key is a tuple of format: (routine_type, routine_name, routine_schema, routine_db)
        list of acceptable types of routine_type's values :
          {'ifunction', 'ufunction', 'procedure', 'trigger', 'event'}
        ifunction - we get AST-obj FunctionCall
        ufunction, procedure - we get ProcedureName or UDFuncName
        case - is separate situation, process it special
        """
        routine_key = None
        if routine_type == "case":
            routine_key = ("ifunction", "case", None, None)
        if routine_type == "ifunction":
            routine_key = (routine_type, ctx.name, None, None)
        if routine_type in ["ufunction", "procedure"]:
            routine_key = (routine_type, ctx.routine.name, ctx.schema.name if ctx.schema else None, None)
        #TODO: add other routine
        self.function_names[routine_key] = True
    
    def enterSimpleFunctionCall(self, ctx) -> None:
        # TODO: find how do this thing more global and universal
        # define "Flow control functions"
        if ctx.name.lower() in self.flow_control_functions_names:
            self.is_flow_control_func = True
        # add function name in list of all routines
        self.add_routine_key(ctx, "ifunction")

    def enterCaseFunctionCall(self, ctx) -> None:
        self.is_flow_control_func = True
        # add function name in list of all routines
        self.add_routine_key(ctx, "case")

    def enterAggregateFunctionCall(self, ctx) -> None:
        # add function name in list of all routines
        self.add_routine_key(ctx, "ifunction")

    def enterNoParenthFunctionCall(self, ctx) -> None:
        # add function name in list of all routines
        self.add_routine_key(ctx, "ifunction")

    def enterExtArgFunctionCall(self, ctx) -> None:
        # add function name in list of all routines
        self.add_routine_key(ctx, "ifunction")
    # Functions end

    # Literal in ColumnClause start
    def enterColumnClause(self, ctx) -> None:
        self.column_clause_context = True

    def exitColumnClause(self, ctx) -> None:
        self.column_clause_context = False

    def enterStringLiteral(self, ctx) -> None:
        if self.column_clause_context:
            self.is_constant = True

    def enterRealLiteral(self, ctx) -> None:
        if self.column_clause_context:
            self.is_constant = True

    def enterHexadecimalLiteral(self, ctx):
        self.is_hex = True
        if self.column_clause_context:
            self.is_constant = True

    def enterBitStringLiteral(self, ctx) -> None:
        if self.column_clause_context:
            self.is_constant = True
    def enterNullLiteral(self, ctx) -> None:
        if self.column_clause_context:
            self.is_constant = True

    def enterBooleanLiteral(self, ctx) -> None:
        if self.column_clause_context:
            self.is_constant = True

    def enterNumberLiteral(self, ctx) -> None:
        if self.column_clause_context:
            self.is_constant = True
    # Literal in ColumnClause end

    def enterVariable(self, ctx) -> None:
        self.is_variable = True
        if self.max_variable_len < len(ctx.name):
            self.max_variable_len = len(ctx.name)

    def enterLogicalExpression(self, ctx) -> None:
        if ctx.isUnary is None or not ctx.isUnary:
            self.is_logical_operator = True

    def enterExportTextFile(self, ctx) -> None:
        self.is_rw_file = True

    def enterExportDumpFile(self, ctx) -> None:
        self.is_rw_file = True
