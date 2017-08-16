from aule import ASTParserFactory, ASTParser
from aule.codegen import *


def main(code_name):
    sources = dict(
        code1="""
        namespace test {
            policy medicalPolicy {
                target clause user.id subset ["admin", "root"] and action == "select"
                apply denyoverrides
                rule {
                    permit
                    target clause "admin" in user.roles and "admin" == user.id
                        clause entity.role == "doctor" and entity.age > 18
                }
                rule aa { 
                    deny
                    target clause entity.age == 18
                } 
                rule aaa { 
                    deny
                    target clause user.id subset ["admin", "root"]

                }
                rule bb {
                    deny
                    target clause entity.role == "doctor" and entity.age > 18
                }
            }
        }
    """,
        code2="""
        namespace com {
            namespace example {
                policy printerPolicy {
                    target clause entity.type == "medicalRecord"
                    apply denyOverrides
                    rule a {
                        permit
                        target clause Attributes.role == "doctor"
                    }
                }
            }
        }
    """,
        code4="""
        namespace example {
            export policySet mainTopLevel {
                target clause Attributes.resource == "medical"
                apply denyOverrides
                medicalPolicy1
                policy printerPolicy {
                    target clause Attributes.resourceType == "medicalRecord"
                    apply denyOverrides
                    rule {
                        permit
                        target clause Attributes.role == "doctor"
                    }
                }
                medicalPolicy2
                medicalPolicy3
            }

            policy printerPolicy100 {
                target clause entity.type == "medicalRecord"
                apply denyOverrides
                rule a {
                    permit
                    target clause Attributes.role == "doctor"
                }
            }

            policy printerPolicy200 {
                target clause entity.type == "medicalRecord"
                apply denyOverrides
                rule a {
                    permit
                    target clause Attributes.role == "doctor"
                }
            }
        }
    """,
        code5="""
        namespace aa {
            export policy Main {
                target clause action == "select" and a.b.c.d == 1
                condition check_levels() == true
                apply denyUnlessPermit
                rule aaa{
                    permit
                    condition check_roles() == true and check_groups() == true
    
                }
            }
        }
    """,
        code6="""
        namespace example {
            export policy Main {
                target clause action == "update"
                apply denyUnlessPermit
                rule r1 {
                    permit
                    target clause subject.level > entity.level
                }
            }
        }
    """,
        code7="""
        namespace example {
            export policy Main {
              target clause action == "select"
                apply denyUnlessPermit
                rule r1 {
                    permit
                    target clause subject.level > entity.level
                }
            }
        }
    """,

        code8="""
        namespace example {
            export policy Main {
                target clause action == "select"
                apply denyUnlessPermit
                rule r1 {
                    permit
                    target clause session.user.id == 4
                }
            }
        }
    """,
        code9="""
        namespace example {
            export policy Main {
                target clause action == "select"
                apply denyUnlessPermit
                rule r1 {
                    permit
                    condition session.user.id == call()
                }
            }
        }
    """,
        code10="""
        namespace example {
            export policy Main {
                target clause action == "select" clause action == "select1"
                apply denyUnlessPermit
                rule r1 {
                    permit
                    condition session.user.id == call()
                }
            }
        }
    """
    )

    code = sources.get(code_name, sources["code9"])
    ast_parser = ASTParserFactory.create("alfa", is_validating=True)
    node = ast_parser.parse(code)
    print(ASTParser.dumps(node))

    luagen = GeneratorFactory.create(
        language=Language.lua,
    ).use_tree(node)
    print(luagen.generate())


if __name__ == "__main__":
    import sys
    try:
        name = sys.argv[1]
    except:
        name = ""
    main(name)
