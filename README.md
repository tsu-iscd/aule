# Aule

Aule is a set of tools designed to work with language applications.

## Getting started

### Fast Installation

Run the following command:

```
make all
```

### Manual ANTLR Installation

`1`. Install Java (version 1.6 or higher):

```
sudo apt-get install default-jdk
```

`2.` Install `ANTLR`:

Download and copy:

```
cd /usr/local/lib
wget http://www.antlr.org/download/antlr-4.6-complete.jar
export CLASSPATH=".:/usr/local/lib/antlr-4.6-complete.jar:$CLASSPATH"
alias antlr4='java -jar /usr/local/lib/antlr-4.6-complete.jar'
alias grun='java org.antlr.v4.gui.TestRig'
```

### Python

`1.` Install Python runtime:

```
sudo pip install antlr4-python3-runtime
```

`2.` Install dev packages:

```
cd aule
sudo pip install -r requirements.txt
```

## Testing

```
make test
make types
```

## Original grammar changes

`1.` Add at the end  of the file `ERROR: .;` to get all tokens via lexer

`2.` Change 
`SPACE:              [ \t\r\n]+    -> skip;`
to
`SPACE:              [ \t\r\n]+    -> channel(HIDDEN);`

It is required for token deletion from payload in WAF SQLi detector.


## Tools

### parser-cli

The `tools/parser-cli.py` utility can be used to parse SQL strings from command line.

It accepts the following options:

```
-v, --vendor <vendor>                                    SQL grammar vendor. Supported: mysql, tsql.
-h, --help                                               Display this help.
-m, --mode <ac, profiler, validator, tokenizer, ast>     Parser mode. Default is validator.
-t, --text <text>                                        Text to parse.
-d, --debug                                              Enable debug mode.
-f, --form <json, string>                                Format to print AST when needed.
```

## Sources
* [Original Transact-SQL Grammar](https://github.com/antlr/grammars-v4/tree/master/tsql)
* [Original PL/SQL Grammar](https://github.com/antlr/grammars-v4/tree/master/plsql)
