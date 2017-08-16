import time
import sys
import os
import getopt
from aule.parser import ParserFactory


def usage():
        """ Print usage. """
        print("Usage:")
        print("  parsing-time [options]")
        print("")
        print("Available options:")
        print("")
        print("   -v, --vendor <vendor>                                    SQL grammar vendor. Supported: mysql, tsql.")
        print("   -h, --help                                               Display this help.")
        print("   -m, --mode <file, lines>                                 Parser mode. ")
        print("   -f, --file <text>                                        File name.")
        print("")


def parse_file(vendor, filename):
    parser = ParserFactory.create(vendor)
    is_valid, size, exec_time = None, None, None
    try:
        f = open(filename, "r")
    except IOError as err:
        print("File IO error.")
        print(err)
    else:
        size = os.path.getsize(filename)
        sql = f.read()
        start_time = time.time()
        is_valid = parser.check_syntax(sql)
        exec_time = time.time() - start_time
        f.close()

    print("Code is valid: " + str(is_valid))
    print("File size: " + str(size))
    print("Parsing time: " + str(exec_time))
    print("Parsing speed: " + str(size/exec_time) + " B/sec")


def parse_lines(vendor, filename):
    parser = ParserFactory.create(vendor)
    is_valid, size, exec_time = None, None, None

    with open(filename, "r") as f:
        content = f.readlines() 
    
    size = len(content)
    start_time = time.time()
    for line in content:
        is_valid = parser.check_syntax(line)
    exec_time = time.time() - start_time

    print("Code is valid: " + str(is_valid))
    print("Size: " + str(size))
    print("Parsing time: " + str(exec_time))
    print("Parsing speed: " + str(size/exec_time) + " Query/sec")


def main(argv):
    mode = "file"
    vendor = "mysql"
    filename = ""

    try:
        opts, args = getopt.getopt(argv, "hf:v:m:", ["help", "file=", "vendor=", "mode="])
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
        elif opt in ("-f", "--file"):
            filename = arg
        else:
            assert False, "unhandled option"

    if not filename:
        usage()
        sys.exit(1)

    if mode == "file":
        parse_file(vendor, filename)
    elif mode == "lines":
        parse_lines(vendor, filename)
    else:
        assert False, "unhandled mode"


if __name__ == '__main__':
    main(sys.argv[1:])