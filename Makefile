ANTLR4=java -jar "/usr/local/lib/antlr-4.7-complete.jar"
PYTHON=python3.6

kotlin-sql-ast:
	@echo "Generate SQL AST in Kotlin:"
	${PYTHON} -m aule.codegen -t kotlinIDL -n sql -i "aule/resources/idl/sql.idl" -o "aule/generated/" -p "com.ptsecurity.ktdbfw.generated.ast"

sql-ast: kotlin-sql-ast

alfa-ast:
	@echo "Generate ALFA AST in Python:"
	${PYTHON} -m aule.codegen -t pythonIDL -n alfa -i "aule/resources/idl/alfa.idl" -o "aule/generated/"

sql-lexer:
	@echo "Compile universal SQL lexer:"
	cd aule/grammars/sqllexer && ${ANTLR4} -Dlanguage=Python3 sqlLexer.g4 -o ../../../generated/

kotlin-parser:
	@echo "Compile Kotlin parser:"
	cd aule/resources/grammars/kotlin && ${ANTLR4} -Dlanguage=Python3 kotlinLexer.g4 kotlinParser.g4 -o ../../../generated/ -visitor

lua-parser:
	@echo "Compile Lua parser:"
	cd aule/resources/grammars/lua && ${ANTLR4} -Dlanguage=Python3 lua.g4 -o ../../../generated/ -visitor

idl-parser:
	@echo "Compile IDL parser:"
	cd aule/resources/grammars/idl && ${ANTLR4} -Dlanguage=Python3 idl.g4 -o ../../../generated/ -visitor

alfa-parser:
	@echo "Compile ALFA parser:"
	cd aule/resources/grammars/alfa && ${ANTLR4} -Dlanguage=Python3 alfaLexer.g4 alfaParser.g4 -o ../../../generated/ -visitor

mysql-parser:
	@echo "Compile MySQL parser:"
	cd aule/resources/grammars/mysql && ${ANTLR4} -Dlanguage=Python3 mysqlLexer.g4 mysqlParser.g4 -o ../../../generated/ -visitor

tsql-parser:    
	@echo "Compile TSQL parser:"
	cd aule/resources/grammars/tsql && ${ANTLR4} -Dlanguage=Python3 tsql.g4 -o ../../../generated/ -visitor

parsers: mysql-parser tsql-parser idl-parser alfa-parser sql-ast alfa-ast
		
clean-parsers:
	@echo "ANTLR parsers cleaning:"
	rm -r aule/generated/.*; touch aule/generated/__init__.py; rm -r aule/generated/resources/grammars/*

clean:
	@echo "Cleaning:"
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

antlr:
	@echo "ANTLR4 installation:"
	cd /usr/local/lib && \
	curl -O http://www.antlr.org/download/antlr-4.7-complete.jar && \
	${PYTHON} -m pip install antlr4-python3-runtime
	@echo "export CLASSPATH=.:/usr/local/lib/antlr-4.7-complete.jar:'${CLASSPATH}'"

packages:
	${PYTHON} -m pip install -r requirements.txt

types:
	@echo "Static type checking:"
	${PYTHON} tools/mypy-runner.py

tests: parsers clean types
	@echo "Project testing:"
	${PYTHON} $(shell which nosetests) tests/

test: clean
	@echo "Project testing:"
	${PYTHON} $(shell which nosetests) tests/$(unittest).py

init:
	@echo "export PYTHONPATH=${PYTHONPATH}:`pwd`"

install: antlr packages

all: install parsers test

.PHONY: clean test
