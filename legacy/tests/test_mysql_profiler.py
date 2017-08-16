from .context import SQLCollector as mysqlCollector
from .context import ASTParserFactory


ast_parser = ASTParserFactory.create("mysql")


def test_simple_queries():
    sql = "select 1"
    node = ast_parser.parse(sql)
    profile = mysqlCollector.get_profile(node)
    assert profile["is_valid"] is True
    assert profile["is_subquery"] is False
    assert profile["is_insert_subquery"] is False
    assert profile["is_update_subquery"] is False
    assert profile["is_delete_subquery"] is False
    assert profile["max_subquery_depth"] == 0
    assert profile["max_select_depth"] == 0
    assert profile["max_insert_depth"] == 0
    assert profile["max_update_depth"] == 0
    assert profile["max_delete_depth"] == 0
    assert profile["is_union"] is False
    assert profile["max_union_len"] == 0
    assert profile["max_entity_len"] == 0
    assert profile["max_column_len"] == 0
    assert profile["max_table_len"] == 0
    assert profile["max_schema_len"] == 0
    assert profile["max_routine_len"] == 0
    assert profile["max_variable_len"] == 0
    assert profile["max_columns"] == 1
    assert profile["functions"] is None
    assert profile["is_stacked_queries"] is False
    assert profile["is_comment"] is False
    assert profile["is_sys_entity"] is False
    assert profile["is_exec_os_command"] is False
    assert profile["is_routine_proc"] is False
    assert profile["is_flow_control_func"] is False
    assert profile["is_rw_file"] is False
    assert profile["is_logical_operator"] is False
    assert profile["is_variable"] is False
    assert profile["is_constant"] is True
    assert profile["is_hex"] is False
    
    sql = "select insert select"
    node = ast_parser.parse(sql)
    profile = mysqlCollector.get_profile(node)
    assert profile["is_valid"] is False
    assert profile["is_subquery"] is None
    assert profile["is_insert_subquery"] is None
    assert profile["is_update_subquery"] is None
    assert profile["is_delete_subquery"] is None
    assert profile["max_subquery_depth"] is None
    assert profile["max_select_depth"] is None
    assert profile["max_insert_depth"] is None
    assert profile["max_update_depth"] is None
    assert profile["max_delete_depth"] is None
    assert profile["is_union"] is None
    assert profile["max_union_len"] is None
    assert profile["max_entity_len"] is None
    assert profile["max_column_len"] is None
    assert profile["max_table_len"] is None
    assert profile["max_schema_len"] is None
    assert profile["max_routine_len"] is None
    assert profile["max_variable_len"] is None
    assert profile["max_columns"] is None
    assert profile["functions"] is None
    assert profile["is_stacked_queries"] is None
    assert profile["is_comment"] is None
    assert profile["is_sys_entity"] is None
    assert profile["is_exec_os_command"] is None
    assert profile["is_routine_proc"] is None
    assert profile["is_flow_control_func"] is None
    assert profile["is_rw_file"] is None
    assert profile["is_logical_operator"] is None
    assert profile["is_variable"] is None
    assert profile["is_constant"] is None
    assert profile["is_hex"] is None

    sql = "select from"
    node = ast_parser.parse(sql)
    profile = mysqlCollector.get_profile(node)
    assert profile["is_valid"] is False
    assert profile["is_subquery"] is None
    assert profile["is_insert_subquery"] is None
    assert profile["is_update_subquery"] is None
    assert profile["is_delete_subquery"] is None
    assert profile["max_subquery_depth"] is None
    assert profile["max_select_depth"] is None
    assert profile["max_insert_depth"] is None
    assert profile["max_update_depth"] is None
    assert profile["max_delete_depth"] is None
    assert profile["is_union"] is None
    assert profile["max_union_len"] is None
    assert profile["max_entity_len"] is None
    assert profile["max_column_len"] is None
    assert profile["max_table_len"] is None
    assert profile["max_schema_len"] is None
    assert profile["max_routine_len"] is None
    assert profile["max_variable_len"] is None
    assert profile["max_columns"] is None
    assert profile["functions"] is None
    assert profile["is_stacked_queries"] is None
    assert profile["is_comment"] is None
    assert profile["is_sys_entity"] is None
    assert profile["is_exec_os_command"] is None
    assert profile["is_routine_proc"] is None
    assert profile["is_flow_control_func"] is None
    assert profile["is_rw_file"] is None
    assert profile["is_logical_operator"] is None
    assert profile["is_variable"] is None
    assert profile["is_constant"] is None
    assert profile["is_hex"] is None

    sql = "select foo from bar"
    node = ast_parser.parse(sql)
    profile = mysqlCollector.get_profile(node)
    assert profile["is_valid"] is True
    assert profile["is_subquery"] is False
    assert profile["is_insert_subquery"] is False
    assert profile["is_update_subquery"] is False
    assert profile["is_delete_subquery"] is False
    assert profile["max_subquery_depth"] == 0
    assert profile["max_select_depth"] == 0
    assert profile["max_insert_depth"] == 0
    assert profile["max_update_depth"] == 0
    assert profile["max_delete_depth"] == 0
    assert profile["is_union"] is False
    assert profile["max_union_len"] == 0
    assert profile["max_entity_len"] == 3
    assert profile["max_column_len"] == 3
    assert profile["max_table_len"] == 3
    assert profile["max_schema_len"] == 0
    assert profile["max_routine_len"] == 0
    assert profile["max_variable_len"] == 0
    assert profile["max_columns"] == 1
    assert profile["functions"] is None
    assert profile["is_stacked_queries"] is False
    assert profile["is_comment"] is False
    assert profile["is_sys_entity"] is False
    assert profile["is_exec_os_command"] is False
    assert profile["is_routine_proc"] is False
    assert profile["is_flow_control_func"] is False
    assert profile["is_rw_file"] is False
    assert profile["is_logical_operator"] is False
    assert profile["is_variable"] is False
    assert profile["is_constant"] is False
    assert profile["is_hex"] is False

    sql = "select foo from bar -- foo"
    node = ast_parser.parse(sql)
    profile = mysqlCollector.get_profile(node)
    assert profile["is_valid"] is True
    assert profile["is_subquery"] is False
    assert profile["is_insert_subquery"] is False
    assert profile["is_update_subquery"] is False
    assert profile["is_delete_subquery"] is False
    assert profile["max_subquery_depth"] == 0
    assert profile["max_select_depth"] == 0
    assert profile["max_insert_depth"] == 0
    assert profile["max_update_depth"] == 0
    assert profile["max_delete_depth"] == 0
    assert profile["is_union"] is False
    assert profile["max_union_len"] == 0
    assert profile["max_entity_len"] == 3
    assert profile["max_column_len"] == 3
    assert profile["max_table_len"] == 3
    assert profile["max_schema_len"] == 0
    assert profile["max_routine_len"] == 0
    assert profile["max_variable_len"] == 0
    assert profile["max_columns"] == 1
    assert profile["functions"] is None
    assert profile["is_stacked_queries"] is False
    assert profile["is_comment"] is True
    assert profile["is_sys_entity"] is False
    assert profile["is_exec_os_command"] is False
    assert profile["is_routine_proc"] is False
    assert profile["is_flow_control_func"] is False
    assert profile["is_rw_file"] is False
    assert profile["is_logical_operator"] is False
    assert profile["is_variable"] is False
    assert profile["is_constant"] is False
    assert profile["is_hex"] is False

    sql = "select foo from bar union select foo from baz"
    node = ast_parser.parse(sql)
    profile = mysqlCollector.get_profile(node)
    assert profile["is_valid"] is True
    assert profile["is_subquery"] is False
    assert profile["is_insert_subquery"] is False
    assert profile["is_update_subquery"] is False
    assert profile["is_delete_subquery"] is False
    assert profile["max_subquery_depth"] == 0
    assert profile["max_select_depth"] == 0
    assert profile["max_insert_depth"] == 0
    assert profile["max_update_depth"] == 0
    assert profile["max_delete_depth"] == 0
    assert profile["is_union"] is True
    assert profile["max_union_len"] == 2
    assert profile["max_entity_len"] == 3
    assert profile["max_column_len"] == 3
    assert profile["max_table_len"] == 3
    assert profile["max_schema_len"] == 0
    assert profile["max_routine_len"] == 0
    assert profile["max_variable_len"] == 0
    assert profile["max_columns"] == 1
    assert profile["functions"] is None
    assert profile["is_stacked_queries"] is False
    assert profile["is_comment"] is False
    assert profile["is_sys_entity"] is False
    assert profile["is_exec_os_command"] is False
    assert profile["is_routine_proc"] is False
    assert profile["is_flow_control_func"] is False
    assert profile["is_rw_file"] is False
    assert profile["is_logical_operator"] is False
    assert profile["is_variable"] is False
    assert profile["is_constant"] is False
    assert profile["is_hex"] is False

    sql = "select 1; select 2"
    node = ast_parser.parse(sql)
    profile = mysqlCollector.get_profile(node)
    assert profile["is_valid"] is True
    assert profile["is_subquery"] is False
    assert profile["is_insert_subquery"] is False
    assert profile["is_update_subquery"] is False
    assert profile["is_delete_subquery"] is False
    assert profile["max_subquery_depth"] == 0
    assert profile["max_select_depth"] == 0
    assert profile["max_insert_depth"] == 0
    assert profile["max_update_depth"] == 0
    assert profile["max_delete_depth"] == 0
    assert profile["is_union"] is False
    assert profile["max_union_len"] == 0
    assert profile["max_entity_len"] == 0
    assert profile["max_column_len"] == 0
    assert profile["max_table_len"] == 0
    assert profile["max_schema_len"] == 0
    assert profile["max_routine_len"] == 0
    assert profile["max_variable_len"] == 0
    assert profile["max_columns"] == 1
    assert profile["functions"] is None
    assert profile["is_stacked_queries"] is True
    assert profile["is_comment"] is False
    assert profile["is_sys_entity"] is False
    assert profile["is_exec_os_command"] is False
    assert profile["is_routine_proc"] is False
    assert profile["is_flow_control_func"] is False
    assert profile["is_rw_file"] is False
    assert profile["is_logical_operator"] is False
    assert profile["is_variable"] is False
    assert profile["is_constant"] is True
    assert profile["is_hex"] is False

    sql = "SELECT t.*, a+b AS total_sum FROM ( SELECT SUM(column1) AS a, SUM((select column2 from test where id = (select 2))) AS b FROM tab) t WHERE id = (select 1)"
    node = ast_parser.parse(sql)
    profile = mysqlCollector.get_profile(node)
    assert profile["is_valid"] is True
    assert profile["is_subquery"] is True
    assert profile["is_insert_subquery"] is False
    assert profile["is_update_subquery"] is False
    assert profile["is_delete_subquery"] is False
    assert profile["max_subquery_depth"] == 3
    assert profile["max_select_depth"] == 3
    assert profile["max_insert_depth"] == 0
    assert profile["max_update_depth"] == 0
    assert profile["max_delete_depth"] == 0
    assert profile["is_union"] is False
    assert profile["max_union_len"] == 0
    assert profile["max_entity_len"] == 9
    assert profile["max_column_len"] == 7
    assert profile["max_table_len"] == 4
    assert profile["max_schema_len"] == 0
    assert profile["max_routine_len"] == 0
    assert profile["max_variable_len"] == 0
    assert profile["max_columns"] == 2
    assert len(profile["functions"]) == 1
    print(profile["functions"])
    assert ('ifunction', 'SUM', None, None) in profile["functions"]
    assert profile["is_stacked_queries"] is False
    assert profile["is_comment"] is False
    assert profile["is_sys_entity"] is False
    assert profile["is_exec_os_command"] is False
    assert profile["is_routine_proc"] is False
    assert profile["is_flow_control_func"] is False
    assert profile["is_rw_file"] is False
    assert profile["is_logical_operator"] is False
    assert profile["is_variable"] is False
    assert profile["is_constant"] is True
    assert profile["is_hex"] is False


    sql = "select foo.a, bar.b from tab1 as foo, tab2 as bar"
    node = ast_parser.parse(sql)
    profile = mysqlCollector.get_profile(node)
    assert profile["is_valid"] is True
    assert profile["is_subquery"] is False
    assert profile["is_insert_subquery"] is False
    assert profile["is_update_subquery"] is False
    assert profile["is_delete_subquery"] is False
    assert profile["max_subquery_depth"] == 0
    assert profile["max_select_depth"] == 0
    assert profile["max_insert_depth"] == 0
    assert profile["max_update_depth"] == 0
    assert profile["max_delete_depth"] == 0
    assert profile["is_union"] is False
    assert profile["max_union_len"] == 0
    assert profile["max_entity_len"] == 4
    assert profile["max_column_len"] == 1
    assert profile["max_table_len"] == 4
    assert profile["max_schema_len"] == 0
    assert profile["max_routine_len"] == 0
    assert profile["max_variable_len"] == 0
    assert profile["max_columns"] == 2
    assert profile["functions"] is None
    assert profile["is_stacked_queries"] is False
    assert profile["is_comment"] is False
    assert profile["is_sys_entity"] is False
    assert profile["is_exec_os_command"] is False
    assert profile["is_routine_proc"] is False
    assert profile["is_flow_control_func"] is False
    assert profile["is_rw_file"] is False
    assert profile["is_logical_operator"] is False
    assert profile["is_variable"] is False
    assert profile["is_constant"] is False
    assert profile["is_hex"] is False

    sql = "select a,b,c from d union select 1,1,1"
    node = ast_parser.parse(sql)
    profile = mysqlCollector.get_profile(node)
    assert profile["is_valid"] is True
    assert profile["is_subquery"] is False
    assert profile["is_insert_subquery"] is False
    assert profile["is_update_subquery"] is False
    assert profile["is_delete_subquery"] is False
    assert profile["max_subquery_depth"] == 0
    assert profile["max_select_depth"] == 0
    assert profile["max_insert_depth"] == 0
    assert profile["max_update_depth"] == 0
    assert profile["max_delete_depth"] == 0
    assert profile["is_union"] is True
    assert profile["max_union_len"] == 2
    assert profile["max_entity_len"] == 1
    assert profile["max_column_len"] == 1
    assert profile["max_table_len"] == 1
    assert profile["max_schema_len"] == 0
    assert profile["max_routine_len"] == 0
    assert profile["max_variable_len"] == 0
    assert profile["max_columns"] == 3
    assert profile["functions"] is None
    assert profile["is_stacked_queries"] is False
    assert profile["is_comment"] is False
    assert profile["is_sys_entity"] is False
    assert profile["is_exec_os_command"] is False
    assert profile["is_routine_proc"] is False
    assert profile["is_flow_control_func"] is False
    assert profile["is_rw_file"] is False
    assert profile["is_logical_operator"] is False
    assert profile["is_variable"] is False
    assert profile["is_constant"] is True
    assert profile["is_hex"] is False


    sql = "select a,b,c from d union select 1,1,0xFF"
    node = ast_parser.parse(sql)
    profile = mysqlCollector.get_profile(node)
    assert profile["is_valid"] is True
    assert profile["is_subquery"] is False
    assert profile["is_insert_subquery"] is False
    assert profile["is_update_subquery"] is False
    assert profile["is_delete_subquery"] is False
    assert profile["max_subquery_depth"] == 0
    assert profile["max_select_depth"] == 0
    assert profile["max_insert_depth"] == 0
    assert profile["max_update_depth"] == 0
    assert profile["max_delete_depth"] == 0
    assert profile["is_union"] is True
    assert profile["max_union_len"] == 2
    assert profile["max_entity_len"] == 1
    assert profile["max_column_len"] == 1
    assert profile["max_table_len"] == 1
    assert profile["max_schema_len"] == 0
    assert profile["max_routine_len"] == 0
    assert profile["max_variable_len"] == 0
    assert profile["max_columns"] == 3
    assert profile["functions"] is None
    assert profile["is_stacked_queries"] is False
    assert profile["is_comment"] is False
    assert profile["is_sys_entity"] is False
    assert profile["is_exec_os_command"] is False
    assert profile["is_routine_proc"] is False
    assert profile["is_flow_control_func"] is False
    assert profile["is_rw_file"] is False
    assert profile["is_logical_operator"] is False
    assert profile["is_variable"] is False
    assert profile["is_constant"] is True
    assert profile["is_hex"] is True

    sql = "SELECT Email FROM Customer WHERE CustomerId = 0x1F1111"
    node = ast_parser.parse(sql)
    profile = mysqlCollector.get_profile(node)
    assert profile["is_valid"] is True
    assert profile["is_subquery"] is False
    assert profile["is_insert_subquery"] is False
    assert profile["is_update_subquery"] is False
    assert profile["is_delete_subquery"] is False
    assert profile["max_subquery_depth"] == 0
    assert profile["max_select_depth"] == 0
    assert profile["max_insert_depth"] == 0
    assert profile["max_update_depth"] == 0
    assert profile["max_delete_depth"] == 0
    assert profile["is_union"] is False
    assert profile["max_union_len"] == 0
    assert profile["max_entity_len"] == 10
    assert profile["max_column_len"] == 10
    assert profile["max_table_len"] == 8
    assert profile["max_schema_len"] == 0
    assert profile["max_routine_len"] == 0
    assert profile["max_variable_len"] == 0
    assert profile["max_columns"] == 1
    assert profile["functions"] is None
    assert profile["is_stacked_queries"] is False
    assert profile["is_comment"] is False
    assert profile["is_sys_entity"] is False
    assert profile["is_exec_os_command"] is False
    assert profile["is_routine_proc"] is False
    assert profile["is_flow_control_func"] is False
    assert profile["is_rw_file"] is False
    assert profile["is_logical_operator"] is False
    assert profile["is_variable"] is False
    assert profile["is_constant"] is False
    assert profile["is_hex"] is True

def test_complex_queries():
    sql = "INSERT INTO TempCustomer SELECT CustomerId, FirstName, LastName, Email FROM Customer WHERE CustomerId = @CustomerId; call some_proc()"
    node = ast_parser.parse(sql)
    profile = mysqlCollector.get_profile(node)
    assert profile["is_valid"] is True
    assert profile["is_subquery"] is True
    assert profile["is_insert_subquery"] is True
    assert profile["is_update_subquery"] is False
    assert profile["is_delete_subquery"] is False
    assert profile["max_subquery_depth"] == 1
    assert profile["max_select_depth"] == 0
    assert profile["max_insert_depth"] == 1
    assert profile["max_update_depth"] == 0
    assert profile["max_delete_depth"] == 0
    assert profile["is_union"] is False
    assert profile["max_union_len"] == 0
    assert profile["max_entity_len"] == 12
    assert profile["max_column_len"] == 10
    assert profile["max_table_len"] == 12
    assert profile["max_schema_len"] == 0
    assert profile["max_routine_len"] == 9
    assert profile["max_variable_len"] == 10
    assert profile["max_columns"] == 4
    assert len(profile["functions"]) == 1
    assert ('procedure', 'some_proc', None, None) in profile["functions"]
    assert profile["is_stacked_queries"] is True
    assert profile["is_comment"] is False
    assert profile["is_sys_entity"] is False
    assert profile["is_exec_os_command"] is False
    assert profile["is_routine_proc"] is True
    assert profile["is_flow_control_func"] is False
    assert profile["is_rw_file"] is False
    assert profile["is_logical_operator"] is False
    assert profile["is_variable"] is True
    assert profile["is_constant"] is False
    assert profile["is_hex"] is False

    sql = "select if(1 > 1+1, false, true) as c into outfile 'somefile'; select 1 union select 2"
    node = ast_parser.parse(sql)
    profile = mysqlCollector.get_profile(node)
    assert profile["is_valid"] is True
    assert profile["is_subquery"] is False
    assert profile["is_insert_subquery"] is False
    assert profile["is_update_subquery"] is False
    assert profile["is_delete_subquery"] is False
    assert profile["max_subquery_depth"] == 0
    assert profile["max_select_depth"] == 0
    assert profile["max_insert_depth"] == 0
    assert profile["max_update_depth"] == 0
    assert profile["max_delete_depth"] == 0
    assert profile["is_union"] is True
    assert profile["max_union_len"] == 2
    assert profile["max_entity_len"] == 1
    assert profile["max_column_len"] == 0
    assert profile["max_table_len"] == 0
    assert profile["max_schema_len"] == 0
    assert profile["max_routine_len"] == 0
    assert profile["max_variable_len"] == 0
    assert profile["max_columns"] == 1
    assert len(profile["functions"]) == 1
    assert ('ifunction', 'if', None, None) in profile["functions"]
    assert profile["is_stacked_queries"] is True
    assert profile["is_comment"] is False
    assert profile["is_sys_entity"] is False
    assert profile["is_exec_os_command"] is False
    assert profile["is_routine_proc"] is False
    assert profile["is_flow_control_func"] is True
    assert profile["is_rw_file"] is True
    assert profile["is_logical_operator"] is False
    assert profile["is_variable"] is False
    assert profile["is_constant"] is True
    assert profile["is_hex"] is False

    sql = "select (select 1) as cc, @somevar, col1 /*some is_comment*/ from t where col1 >= 0xaaff55 and col2 is not null union all select 11, 12, 13"
    node = ast_parser.parse(sql)
    profile = mysqlCollector.get_profile(node)
    assert profile["is_valid"] is True
    assert profile["is_subquery"] is True
    assert profile["is_insert_subquery"] is False
    assert profile["is_update_subquery"] is False
    assert profile["is_delete_subquery"] is False
    assert profile["max_subquery_depth"] == 1
    assert profile["max_select_depth"] == 1
    assert profile["max_insert_depth"] == 0
    assert profile["max_update_depth"] == 0
    assert profile["max_delete_depth"] == 0
    assert profile["is_union"] is True
    assert profile["max_union_len"] == 2
    assert profile["max_entity_len"] == 4
    assert profile["max_column_len"] == 4
    assert profile["max_table_len"] == 1
    assert profile["max_schema_len"] == 0
    assert profile["max_routine_len"] == 0
    assert profile["max_variable_len"] == 7
    assert profile["max_columns"] == 3
    assert profile["functions"] is None
    assert profile["is_stacked_queries"] is False
    assert profile["is_comment"] is True
    assert profile["is_sys_entity"] is False
    assert profile["is_exec_os_command"] is False
    assert profile["is_routine_proc"] is False
    assert profile["is_flow_control_func"] is False
    assert profile["is_rw_file"] is False
    assert profile["is_logical_operator"] is True
    assert profile["is_variable"] is True
    assert profile["is_constant"] is True
    assert profile["is_hex"] is True

    sql = """
    insert into t select * from tbl 
        where substring(col, 5) ='abcde' and col2 between sqrt(5) and log(255);
    update t1, t2, t3 set t2.col1 = (select somecol from t3) 
         where t2.defcol between t1.somecol and t3.anothercol;
    """
    node = ast_parser.parse(sql)
    profile = mysqlCollector.get_profile(node)
    assert profile["is_valid"] is True
    assert profile["is_subquery"] is True
    assert profile["is_insert_subquery"] is True
    assert profile["is_update_subquery"] is True
    assert profile["is_delete_subquery"] is False
    assert profile["max_subquery_depth"] == 1
    assert profile["max_select_depth"] == 0
    assert profile["max_insert_depth"] == 1
    assert profile["max_update_depth"] == 1
    assert profile["max_delete_depth"] == 0
    assert profile["is_union"] is False
    assert profile["max_union_len"] == 0
    assert profile["max_entity_len"] == 10
    assert profile["max_column_len"] == 10
    assert profile["max_table_len"] == 3
    assert profile["max_schema_len"] == 0
    assert profile["max_routine_len"] == 0
    assert profile["max_variable_len"] == 0
    assert profile["max_columns"] == 1
    print(profile["functions"])
    assert len(profile["functions"]) == 3
    assert ('ifunction', 'substring', None, None) in profile["functions"]
    assert ('ifunction', 'log', None, None) in profile["functions"]
    assert ('ifunction', 'sqrt', None, None) in profile["functions"]
    assert profile["is_stacked_queries"] is True
    assert profile["is_comment"] is False
    assert profile["is_sys_entity"] is False
    assert profile["is_exec_os_command"] is False
    assert profile["is_routine_proc"] is False
    assert profile["is_flow_control_func"] is False
    assert profile["is_rw_file"] is False
    assert profile["is_logical_operator"] is True
    assert profile["is_variable"] is False
    assert profile["is_constant"] is False
    assert profile["is_hex"] is False

    sql = "load data infile 'abc'  into table t1; load data local infile 'somepath_here' replace into table `some table` character set cp1251 fields terminated by '_ff' lines terminated by '\\n' ignore 1 lines(col1, col2, col3)"
    node = ast_parser.parse(sql)
    profile = mysqlCollector.get_profile(node)
    assert profile["is_valid"] is True
    assert profile["is_subquery"] is False
    assert profile["is_insert_subquery"] is False
    assert profile["is_update_subquery"] is False
    assert profile["is_delete_subquery"] is False
    assert profile["max_subquery_depth"] == 0
    assert profile["max_select_depth"] == 0
    assert profile["max_insert_depth"] == 0
    assert profile["max_update_depth"] == 0
    assert profile["max_delete_depth"] == 0
    assert profile["is_union"] is False
    assert profile["max_union_len"] == 0
    assert profile["max_entity_len"] == 12
    assert profile["max_column_len"] == 4
    assert profile["max_table_len"] == 12
    assert profile["max_schema_len"] == 0
    assert profile["max_routine_len"] == 0
    assert profile["max_variable_len"] == 0
    assert profile["max_columns"] == 0
    assert profile["functions"] is None
    assert profile["is_stacked_queries"] is True
    assert profile["is_comment"] is False
    assert profile["is_sys_entity"] is False
    assert profile["is_exec_os_command"] is False
    assert profile["is_routine_proc"] is False
    assert profile["is_flow_control_func"] is False
    assert profile["is_rw_file"] is True
    assert profile["is_logical_operator"] is False
    assert profile["is_variable"] is False
    assert profile["is_constant"] is False
    assert profile["is_hex"] is False

    sql = """
    call `some_proc_name_very_long_length`;
    delete ignore from t 
        where col in (select c1 from t1 join t2 using(c1, c2, c3)
    union
        select cc from ttt 
            where col in (select * from some_dict));
    """
    node = ast_parser.parse(sql)
    profile = mysqlCollector.get_profile(node)
    assert profile["is_valid"] is True
    assert profile["is_subquery"] is True
    assert profile["is_insert_subquery"] is False
    assert profile["is_update_subquery"] is False
    assert profile["is_delete_subquery"] is True
    assert profile["max_subquery_depth"] == 2
    assert profile["max_select_depth"] == 1
    assert profile["max_insert_depth"] == 0
    assert profile["max_update_depth"] == 0
    assert profile["max_delete_depth"] == 2
    assert profile["is_union"] is True
    assert profile["max_union_len"] == 2
    assert profile["max_entity_len"] == 33
    assert profile["max_column_len"] == 3
    assert profile["max_table_len"] == 9
    assert profile["max_schema_len"] == 0
    assert profile["max_routine_len"] == 33
    assert profile["max_variable_len"] == 0
    assert profile["max_columns"] == 1
    assert len(profile["functions"]) == 1
    assert ('procedure', '`some_proc_name_very_long_length`', None, None) in profile["functions"]
    assert profile["is_stacked_queries"] is True
    assert profile["is_comment"] is False
    assert profile["is_sys_entity"] is False
    assert profile["is_exec_os_command"] is False
    assert profile["is_routine_proc"] is True
    assert profile["is_flow_control_func"] is False
    assert profile["is_rw_file"] is False
    assert profile["is_logical_operator"] is False
    assert profile["is_variable"] is False
    assert profile["is_constant"] is False
    assert profile["is_hex"] is False

    sql = """call `some_proc_name_very_long_length`; 
    delete ignore from t where col in (select c1 from t1 join t2 using(c1, c2, c3) union select cc from ttt where col in (select * from some_dict));
    select c1 from t1 join t2 using(c1, c2, c3) union select cc from ttt where col in (select (select 1) as c from some_dict);"""
    node = ast_parser.parse(sql)
    profile = mysqlCollector.get_profile(node)
    assert profile["is_valid"] is True
    assert profile["is_subquery"] is True
    assert profile["is_insert_subquery"] is False
    assert profile["is_update_subquery"] is False
    assert profile["is_delete_subquery"] is True
    assert profile["max_subquery_depth"] == 2
    assert profile["max_select_depth"] == 2
    assert profile["max_insert_depth"] == 0
    assert profile["max_update_depth"] == 0
    assert profile["max_delete_depth"] == 2
    assert profile["is_union"] is True
    assert profile["max_union_len"] == 2
    assert profile["max_entity_len"] == 33
    assert profile["max_column_len"] == 3
    assert profile["max_table_len"] == 9
    assert profile["max_schema_len"] == 0
    assert profile["max_routine_len"] == 33
    assert profile["max_variable_len"] == 0
    assert profile["max_columns"] == 1
    assert len(profile["functions"]) == 1
    assert ('procedure', '`some_proc_name_very_long_length`', None, None) in profile["functions"]
    assert profile["is_stacked_queries"] is True
    assert profile["is_comment"] is False
    assert profile["is_sys_entity"] is False
    assert profile["is_exec_os_command"] is False
    assert profile["is_routine_proc"] is True
    assert profile["is_flow_control_func"] is False
    assert profile["is_rw_file"] is False
    assert profile["is_logical_operator"] is False
    assert profile["is_variable"] is False
    assert profile["is_constant"] is True
    assert profile["is_hex"] is False
