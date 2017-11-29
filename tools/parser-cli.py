#!/usr/bin/env/python

"""
Diagnostic tool to work with parsers stuff via CLI.
"""

# General
import sys
import getopt
import time
from pprint import pprint

# Internal
from aule.ast_parser import ASTParserFactory, ASTParser
from aule.parser import ParserFactory


def main(argv):
    """
    Main function.
    """

    # Default values.
    debug = False
    form = "string"
    mode = "checker"
    vendor = "mysql"
    text = None
    file_name = None
    
    def usage():
        """ Print usage. """
        print("Usage:")
        print("  parser-cli [options]")
        print("")
        print("Available options:")
        print("")
        print("   -v, --vendor <vendor>                                SQL grammar vendor. Supported: mysql, tsql.")
        print("   -h, --help                                           Display this help.")
        print("   -m, --mode <checker, validator, tokenizer, ast>      Parser mode. Default is validator.")
        print("   -t, --text <text>                                    Text to parse.")
        print("   -f, --file <file name>                               File to parse.")
        print("   -d, --debug                                          Enable debug mode.")
        print("   -p, --print <json, string>                           Format to print AST when needed.")
        print("")

    try:
        opts, args = getopt.getopt(argv, "hdp:v:m:t:f:", [
            "help", "debug", "print=", "vendor=", "mode=", "text=", "file="
        ])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(1)
    for opt, arg in opts:
        if opt == "-h":
            usage()
            sys.exit()
        elif opt in ("-m", "--mode"):
            mode = arg
        elif opt in ("-v", "--vendor"):
            vendor = arg
        elif opt in ("-t", "--text"):
            text = arg
        elif opt in ("-f", "--file"):
            file_name = arg
        elif opt in ("-p", "--print"):
            form = arg
        elif opt in ("-d", "--debug"):
            debug = True
        else:
            assert False, "unhandled option"

    if (not text and not file_name) or (text and file_name):
        print("Please specify text or file name.")
        print("")
        usage()
        sys.exit(1)

    if file_name:
        with open(file_name, "r") as f:
            text = f.read()
        f.close()

    parser = ParserFactory.create(vendor)
    ast_parser = None
    if mode == "ast":
        ast_parser = ASTParserFactory.create(vendor)

    if mode == "validator":
        parser.set_validating()
        print("Mode: validator")
        start_time = time.time()
        parser.validate(text)
        exec_time = time.time() - start_time
        print("Errors: " + str(parser.get_errors()))
        print("Parsing time: " + str(exec_time))

    elif mode == "checker":
        print("Mode: syntax checker")
        start_time = time.time()
        is_valid = parser.check_syntax(text)
        exec_time = time.time() - start_time
        print("Code is valid: " + str(is_valid))
        print("Parsing time - 1: " + str(exec_time))
        start_time = time.time()
        _ = parser.check_syntax(text)
        exec_time = time.time() - start_time
        print("Parsing time - 2: " + str(exec_time))

    elif mode == "ast":
        print("Mode: AST")
        start_time = time.time()
        _ = ast_parser.parse(text)
        exec_time = time.time() - start_time
        is_valid = parser.check_syntax(text)
        print("Code is valid: " + str(is_valid))
        print("AST creation time - 1: " + str(exec_time))
        start_time = time.time()
        node = ast_parser.parse(text)
        exec_time = time.time() - start_time
        print("AST creation time - 2: " + str(exec_time))
        print(ASTParser.dumps(node))

    elif mode == "tokenizer":
        print("Mode: tokenizer")
        print("Tokens:")
        pprint(parser.get_tokens(text))
    
    if debug:
        if form == "string":
            print("AST in LISP format:")
            parser.print_string_tree(text)
        elif form == "json":
            print("AST in JSON format:")
            parser.print_json_tree(text)


if __name__ == "__main__":
    main(sys.argv[1:])
