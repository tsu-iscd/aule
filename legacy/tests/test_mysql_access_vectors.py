from .context import SQLCollector as mysqlCollector
from .context import ASTParserFactory


ast_parser = ASTParserFactory.create("mysql")

def test_main_features():
    # Empty ACL 1
    query = "select 1"
    node = ast_parser.parse(query)
    acl = mysqlCollector.get_access_vectors(node)
    assert len(acl["access_vectors"]) == 0
    assert len(acl["loose_access_vectors"]) == 0

    # Empty ACL 2
    query = "select 0xfff, 'some string', null, @myvar"
    node = ast_parser.parse(query)
    acl = mysqlCollector.get_access_vectors(node)
    assert len(acl["access_vectors"]) == 0
    assert len(acl["loose_access_vectors"]) == 0

    # Empty ACL 3, with columns' aliases
    query = "select 0xfff as col1, 'some string' as col2, null as col3, @myvar as col4"
    node = ast_parser.parse(query)
    acl = mysqlCollector.get_access_vectors(node)
    assert len(acl["access_vectors"]) == 0
    assert len(acl["loose_access_vectors"]) == 0

    # Simple Select 1, with no loose
    query = "select bar from foo"
    node = ast_parser.parse(query)
    acl = mysqlCollector.get_access_vectors(node)
    assert len(acl["access_vectors"]) == 1
    assert len(acl["loose_access_vectors"]) == 0
    access_vector = acl["access_vectors"][0]
    assert access_vector["action"] == "Select"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    assert access_vector["table"] == "foo"
    assert len(access_vector["columns"]) == 1
    list(access_vector["columns"])[0] == "bar"

    # Simple Select 2, with no loose
    query = """
    select bar, baz, 'some str'
    from foo 
        where bazz = 'some string'
    """
    node = ast_parser.parse(query)
    acl = mysqlCollector.get_access_vectors(node)
    assert len(acl["access_vectors"]) == 1
    assert len(acl["loose_access_vectors"]) == 0
    access_vector = acl["access_vectors"][0]
    assert access_vector["action"] == "Select"
    assert access_vector["table"] == "foo"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    assert len(access_vector["columns"]) == 3
    assert "baz" in access_vector["columns"]
    assert "bazz" in access_vector["columns"]
    assert "bar" in access_vector["columns"]

    # Simple Select 3, with no loose
    query = """
    select 11, 12, 13 
    from foo as t 
        where t.col1 in ('val1', 'val2', t.col2) and t.col3 between 11 and 10*colN
    """
    node = ast_parser.parse(query)
    acl = mysqlCollector.get_access_vectors(node)
    assert len(acl["access_vectors"]) == 1
    assert len(acl["loose_access_vectors"]) == 0
    access_vector = acl["access_vectors"][0]
    assert access_vector["action"] == "Select"
    assert access_vector["table"] == "foo"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    assert len(access_vector["columns"]) == 4
    assert "col1" in access_vector["columns"]
    assert "col2" in access_vector["columns"]
    assert "col3" in access_vector["columns"]
    assert "colN" in access_vector["columns"]

    # Select with tables aliases 1
    query = """
    select col1 
    from tbl as t, anothertable as t2 join tt on tt.id = t2.link_id 
        where somecol > another_col / 2 and 5 in (col2, col1)
    """
    node = ast_parser.parse(query)
    acl = mysqlCollector.get_access_vectors(node)
    assert len(acl["access_vectors"]) == 3
    assert len(acl["loose_access_vectors"]) == 1
    access_vector = acl["access_vectors"][0]
    assert access_vector["action"] == "Select"
    assert access_vector["table"] == "anothertable"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    assert len(access_vector["columns"]) == 1
    assert "link_id" in access_vector["columns"]
    access_vector = acl["access_vectors"][1]
    assert access_vector["action"] == "Select"
    assert access_vector["table"] == "tbl"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    assert len(access_vector["columns"]) == 0
    access_vector = acl["access_vectors"][2]
    assert access_vector["action"] == "Select"
    assert access_vector["table"] == "tt"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    assert len(access_vector["columns"]) == 1
    assert "id" in access_vector["columns"]
    la_vector = acl["loose_access_vectors"][0]
    assert la_vector["action"] == "Select"
    assert len(la_vector["columns"]) == 4
    assert "another_col" in la_vector["columns"]
    assert "somecol" in la_vector["columns"]
    assert "col1" in la_vector["columns"]
    assert "col2" in la_vector["columns"]
    assert len(la_vector["resources"]) == 3
    res = la_vector["resources"][0]
    assert res["table"] == "anothertable"
    assert res["schema"] is None
    res = la_vector["resources"][1]
    assert res["table"] == "tbl"
    assert res["schema"] is None
    res = la_vector["resources"][2]
    assert res["table"] == "tt"
    assert res["schema"] is None

    # Select with tables aliases 2
    query = """
    select 1, 2, 3, t.col1, t2.col1, tbl5.col1 
    from 
        tbl1 as t inner join tbl2 as t2  on t.a = 'a' or t.ab = concat(t2.a, t2.b)
        left outer join tbl3 t3 on t3.cc = t.cc and t2.col1 > t3.cc, 
        tbl4 as t4 join tbl5
    where t4.cc in (select distinct cc from tbl3)
    """
    node = ast_parser.parse(query)
    acl = mysqlCollector.get_access_vectors(node)
    assert len(acl["access_vectors"]) == 5
    assert len(acl["loose_access_vectors"]) == 0
    access_vector = acl["access_vectors"][0]
    assert access_vector["action"] == "Select"
    assert access_vector["table"] == "tbl1"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    assert len(access_vector["columns"]) == 4
    assert "cc" in access_vector["columns"]
    assert "a" in access_vector["columns"]
    assert "ab" in access_vector["columns"]
    assert "col1" in access_vector["columns"]
    access_vector = acl["access_vectors"][1]
    assert access_vector["action"] == "Select"
    assert access_vector["table"] == "tbl2"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    assert len(access_vector["columns"]) == 3
    assert "a" in access_vector["columns"]
    assert "b" in access_vector["columns"]
    assert "col1" in access_vector["columns"]
    access_vector = acl["access_vectors"][2]
    assert access_vector["action"] == "Select"
    assert access_vector["table"] == "tbl3"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    assert len(access_vector["columns"]) == 1
    assert "cc" in access_vector["columns"]
    access_vector = acl["access_vectors"][3]
    assert access_vector["action"] == "Select"
    assert access_vector["table"] == "tbl4"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    assert len(access_vector["columns"]) == 1
    assert "cc" in access_vector["columns"]
    access_vector = acl["access_vectors"][4]
    assert access_vector["action"] == "Select"
    assert access_vector["table"] == "tbl5"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    assert len(access_vector["columns"]) == 1
    assert "col1" in access_vector["columns"]

    # Select with columns aliases 1
    query = """
    select ab as a1   
    from tbl inner join tbl2 on tbl.ab = tbl2.col
        where tbl.a = 5 and sqrt(ab) > 10 order by a1
    """
    node = ast_parser.parse(query)
    acl = mysqlCollector.get_access_vectors(node)
    assert len(acl["access_vectors"]) == 2
    assert len(acl["loose_access_vectors"]) == 1
    access_vector = acl["access_vectors"][0]
    assert access_vector["action"] == "Select"
    assert access_vector["table"] == "tbl"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    assert len(access_vector["columns"]) == 2
    assert "a" in access_vector["columns"]
    assert "ab" in access_vector["columns"]
    access_vector = acl["access_vectors"][1]
    assert access_vector["action"] == "Select"
    assert access_vector["table"] == "tbl2"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    assert len(access_vector["columns"]) == 1
    assert "col" in access_vector["columns"]
    la_vector = acl["loose_access_vectors"][0]
    assert la_vector["action"] == "Select"
    assert len(la_vector["columns"]) == 1
    assert "ab" in la_vector["columns"]
    assert len(la_vector["resources"]) == 2
    res = la_vector["resources"][0]
    assert res["table"] == "tbl"
    assert res["schema"] is None
    res = la_vector["resources"][1]
    assert res["table"] == "tbl2"
    assert res["schema"] is None

    # Select with columns aliases 2
    query = """
    select col as colal1, testcol as samecolname, col3
    from tbl
        where samecolname > 5
        order by samecolname asc
    """
    node = ast_parser.parse(query)
    acl = mysqlCollector.get_access_vectors(node)
    assert len(acl["access_vectors"]) == 1
    assert len(acl["loose_access_vectors"]) == 0
    access_vector = acl["access_vectors"][0]
    assert access_vector["action"] == "Select"
    assert access_vector["table"] == "tbl"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    assert len(access_vector["columns"]) == 4
    assert "col" in access_vector["columns"]
    assert "testcol" in access_vector["columns"]
    assert "col3" in access_vector["columns"]
    assert "samecolname" in access_vector["columns"]

    # Select with tables and columns aliases 1
    query = """
    select tt.col as colal1, testcol as samecolname, col3
    from tbl as tt
        where tt.samecolname > 5
        order by samecolname asc
    """
    node = ast_parser.parse(query)
    acl = mysqlCollector.get_access_vectors(node)
    assert len(acl["access_vectors"]) == 1
    assert len(acl["loose_access_vectors"]) == 0
    access_vector = acl["access_vectors"][0]
    assert access_vector["action"] == "Select"
    assert access_vector["table"] == "tbl"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    assert len(access_vector["columns"]) == 4
    assert "col" in access_vector["columns"]
    assert "testcol" in access_vector["columns"]
    assert "col3" in access_vector["columns"]
    assert "samecolname" in access_vector["columns"]

    # Select with tables and columns aliases 1
    query = """
    select t1.col1, t1.col2 as somecol, t3.col1 as c
    from tbl1 as t1, tt2 as t2, someschema.ttt as t3
        where t3.col1
        order by t3.c
    """
    node = ast_parser.parse(query)
    acl = mysqlCollector.get_access_vectors(node)
    assert len(acl["access_vectors"]) == 3
    assert len(acl["loose_access_vectors"]) == 0
    access_vector = acl["access_vectors"][0]
    assert access_vector["action"] == "Select"
    assert access_vector["table"] == "tbl1"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    assert len(access_vector["columns"]) == 2
    assert "col1" in access_vector["columns"]
    assert "col2" in access_vector["columns"]
    access_vector = acl["access_vectors"][1]
    assert access_vector["action"] == "Select"
    assert access_vector["table"] == "tt2"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    assert len(access_vector["columns"]) == 0
    access_vector = acl["access_vectors"][2]
    assert access_vector["action"] == "Select"
    assert access_vector["table"] == "ttt"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] == "someschema"
    assert len(access_vector["columns"]) == 2
    assert "col1" in access_vector["columns"]
    assert "c" in access_vector["columns"]

    # Subquery Select 1, with no loose
    query = """
    select bar, (select a from t where t.b > 0) as constCol 
    from ttt
    """
    node = ast_parser.parse(query)
    acl = mysqlCollector.get_access_vectors(node)
    assert len(acl["access_vectors"]) == 2
    assert len(acl["loose_access_vectors"]) == 0
    access_vector = acl["access_vectors"][0]
    assert access_vector["action"] == "Select"
    assert access_vector["table"] == "ttt"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    assert len(access_vector["columns"]) == 1
    assert "bar" in access_vector["columns"]
    access_vector = acl["access_vectors"][1]
    assert access_vector["action"] == "Select"
    assert access_vector["table"] == "t"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    assert len(access_vector["columns"]) == 2
    assert "a" in access_vector["columns"]
    assert "b" in access_vector["columns"]


def test_complex_alias_naming():
    # Cross-aliases query 1
    query = "select col as c from tbl as t having c > 1"
    node = ast_parser.parse(query)
    acl = mysqlCollector.get_access_vectors(node)
    assert len(acl["access_vectors"]) == 1
    assert len(acl["loose_access_vectors"]) == 0
    access_vector = acl["access_vectors"][0]
    assert access_vector["action"] == "Select"
    assert access_vector["table"] == "tbl"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    assert len(access_vector["columns"]) == 1
    assert "col" in access_vector["columns"]

    # Cross-aliases query 2
    query = "select t.col as c from tbl as t having c > 1"
    node = ast_parser.parse(query)
    acl = mysqlCollector.get_access_vectors(node)
    assert len(acl["access_vectors"]) == 1
    assert len(acl["loose_access_vectors"]) == 0
    access_vector = acl["access_vectors"][0]
    assert access_vector["action"] == "Select"
    assert access_vector["table"] == "tbl"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    assert len(access_vector["columns"]) == 1
    assert "col" in access_vector["columns"]


def test_complex_subqueries():
    pass


def test_schema_naming():
    # Simple test 1
    query = "select * from myschema.tbl as t where t.col > 1"
    node = ast_parser.parse(query)
    acl = mysqlCollector.get_access_vectors(node)
    assert len(acl["access_vectors"]) == 1
    assert len(acl["loose_access_vectors"]) == 0
    access_vector = acl["access_vectors"][0]
    assert access_vector["action"] == "Select"
    assert access_vector["table"] == "tbl"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] == "myschema"
    assert len(access_vector["columns"]) == 2
    assert "*" in access_vector["columns"]
    assert "col" in access_vector["columns"]


def test_access_types():
    # Simple Insert 1
    query = "insert into tbl values (1, @val, 5), (5, @val, 1)"
    node = ast_parser.parse(query)
    acl = mysqlCollector.get_access_vectors(node)
    assert len(acl["access_vectors"]) == 1
    assert len(acl["loose_access_vectors"]) == 0
    access_vector = acl["access_vectors"][0]
    assert access_vector["action"] == "Insert"
    assert access_vector["table"] == "tbl"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    assert len(access_vector["columns"]) == 0

    # TODO: make complex accesses types, when using multiple tables
    #  for example this:
    """
    delete ignore 
    from tbl_a.*, tbl_b.* 
    using 
        tbl_a inner join tbl_b on tbl_a.col1 = tbl_b.col2 
        join tbl_c on tbl_c.id = tbl_b.id
"""
    # Simple multiple Delete 1
    query = """
    delete ignore 
    from tbl_a.*, tbl_b.* 
    using 
        tbl_a inner join tbl_b on tbl_a.col1 = tbl_b.col2 
    """
    node = ast_parser.parse(query)
    acl = mysqlCollector.get_access_vectors(node)
    assert len(acl["access_vectors"]) == 2
    assert len(acl["loose_access_vectors"]) == 0
    access_vector = acl["access_vectors"][0]
    assert access_vector["action"] == "Delete"
    assert access_vector["table"] == "tbl_a"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    access_vector = acl["access_vectors"][1]
    assert access_vector["action"] == "Delete"
    assert access_vector["table"] == "tbl_b"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None

    # Multiple Delete with subquery Select (1)
    query = """
    delete ignore 
    from tbl_a.*, tbl_b.* 
    using 
        tbl_a inner join tbl_b on tbl_a.col1 = tbl_b.col2 
    where tbl_a.col_b in (select distinct t.somecol from ttt as t where anothercol > 1)
    """
    node = ast_parser.parse(query)
    acl = mysqlCollector.get_access_vectors(node)
    assert len(acl["access_vectors"]) == 3
    assert len(acl["loose_access_vectors"]) == 0
    access_vector = acl["access_vectors"][0]
    assert access_vector["action"] == "Delete"
    assert access_vector["table"] == "tbl_a"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    access_vector = acl["access_vectors"][1]
    assert access_vector["action"] == "Delete"
    assert access_vector["table"] == "tbl_b"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    access_vector = acl["access_vectors"][2]
    assert access_vector["action"] == "Select"
    assert access_vector["table"] == "ttt"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    assert len(access_vector["columns"]) == 2
    assert "somecol" in access_vector["columns"]
    assert "anothercol" in access_vector["columns"]


def test_correlate_queries():
    # Correlate query 1 on Exists
    query = """
    select fio 
    from player p 
    where not exists 
        (select * from sport s 
        where not exists 
            (select * from games g 
            where g.sport = s.name and g.player = p.id 
            )
        )
    """
    node = ast_parser.parse(query)
    acl = mysqlCollector.get_access_vectors(node)
    assert len(acl["access_vectors"]) == 3
    assert len(acl["loose_access_vectors"]) == 0
    access_vector = acl["access_vectors"][0]
    assert access_vector["action"] == "Select"
    assert access_vector["table"] == "player"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    assert len(access_vector["columns"]) == 2
    assert "id" in access_vector["columns"]
    assert "fio" in access_vector["columns"]
    access_vector = acl["access_vectors"][1]
    assert access_vector["action"] == "Select"
    assert access_vector["table"] == "sport"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    assert len(access_vector["columns"]) == 2
    assert "*" in access_vector["columns"]
    assert "name" in access_vector["columns"]
    access_vector = acl["access_vectors"][2]
    assert access_vector["action"] == "Select"
    assert access_vector["table"] == "games"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    assert len(access_vector["columns"]) == 3
    assert "player" in access_vector["columns"]
    assert "sport" in access_vector["columns"]
    assert "*" in access_vector["columns"]


def test_routines():
    # Routines Test 1
    query = """
    select col1, a, myFunc(), a*(b+anotherFunc())/(sqrt(specNumberFunc('arg1', 'arg2')))
    from tbl1 as t1 inner join tbl2 as t2 on func_schema.myFunc('arg1') = t1.f1 + t2.f2
        where substring(somecol, t1.pos1 + t2.pos1) = ownSubstring(somecol, t1.pos1, t2.pos1)
    """
    node = ast_parser.parse(query)
    acl = mysqlCollector.get_access_vectors(node)
    assert len(acl["access_vectors"]) == 7
    assert len(acl["loose_access_vectors"]) == 1
    access_vector = acl["access_vectors"][0]
    assert access_vector["action"] == "Select"
    assert access_vector["table"] == "tbl1"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    assert len(access_vector["columns"]) == 2
    assert "f1" in access_vector["columns"]
    assert "pos1" in access_vector["columns"]
    access_vector = acl["access_vectors"][1]
    assert access_vector["action"] == "Select"
    assert access_vector["table"] == "tbl2"
    assert access_vector["resource_type"] == "table"
    assert access_vector["schema"] is None
    assert len(access_vector["columns"]) == 2
    assert "f2" in access_vector["columns"]
    assert "pos1" in access_vector["columns"]
    access_vector = acl["access_vectors"][2]
    assert access_vector["action"] == "execute"
    assert access_vector["resource_type"] == "function"
    assert access_vector["schema"] is None
    assert access_vector["routine_name"] == "anotherFunc"
    access_vector = acl["access_vectors"][3]
    assert access_vector["action"] == "execute"
    assert access_vector["resource_type"] == "function"
    assert access_vector["schema"] is None
    assert access_vector["routine_name"] == "myFunc"
    access_vector = acl["access_vectors"][4]
    assert access_vector["action"] == "execute"
    assert access_vector["resource_type"] == "function"
    assert access_vector["schema"] is None
    assert access_vector["routine_name"] == "ownSubstring"
    access_vector = acl["access_vectors"][5]
    assert access_vector["action"] == "execute"
    assert access_vector["resource_type"] == "function"
    assert access_vector["schema"] is None
    assert access_vector["routine_name"] == "specNumberFunc"
    access_vector = acl["access_vectors"][6]
    assert access_vector["action"] == "execute"
    assert access_vector["resource_type"] == "function"
    assert access_vector["schema"] == "func_schema"
    assert access_vector["routine_name"] == "myFunc"
    la_vector = acl["loose_access_vectors"][0]
    assert la_vector["action"] == "Select"
    assert len(la_vector["columns"]) == 4
    assert "a" in la_vector["columns"]
    assert "somecol" in la_vector["columns"]
    assert "b" in la_vector["columns"]
    assert "col1" in la_vector["columns"]
    assert len(la_vector["resources"]) == 2
    res = la_vector["resources"][0]
    assert res["table"] == "tbl1"
    assert res["schema"] is None
    res = la_vector["resources"][1]
    assert res["table"] == "tbl2"
    assert res["schema"] is None