#!/usr/bin/env/python

"""
Diagnostic tool to work with Dejector via CLI.
"""

# General
import sys
import getopt

# Internal
from aule.dejector import DejectorFactory


def main(argv):
    """
    Main function.
    """
    
    def usage():
        """ Print usage. """
        print("Usage:")
        print("  dejector-cli [options]")
        print("")
        print("Available options:")
        print("")
        print("   -v, --vendor <vendor>                    SQL grammar vendor. Supported: mysql, tsql.")
        print("   -n, --name   <name>                      Dejector name (e.g. submysql).")
        print("   -h, --help                               Display this help.")
        print("   -f, --filename <file>                    File with queries in string format.")
        print("   -m, --mode <file>                        Mode for merging CST in Dejector. Supported: strict, loose.")
        print("   -c, --command <dispose, generate>        Command to perform.")
        print("")
       
    vendor = "mysql"
    name = None
    filename = None
    command = "generate"
    mode = "strict"

    try:
        opts, args = getopt.getopt(argv, "hv:f:n:m:c:", ["help", "vendor=", "filename=", "name=", "mode=", "command="])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            usage()
            sys.exit()
        elif opt in("-f", "--filename"):
            filename = arg
        elif opt in ("-v", "--vendor"):
            vendor = arg
        elif opt in ("-n", "--name"):
            name = arg
        elif opt in ("-c", "--command"):
            command = arg
        elif opt in ("-m", "--mode"):
            mode = arg
        else:
            assert False, "unhandled option"

    if mode not in ("strict", "loose"):
        print("Invalid arguments for mode")
        sys.exit(2)
    
    if command == "dispose":
        DejectorFactory.dispose_by_name(name)
        sys.exit()

    if command == "generate":
        if filename and name:
            dejector = DejectorFactory.create(vendor, name, mode)
            dejector.from_file(filename)
        else:
            print("Invalid arguments")
            sys.exit(2)

if __name__ == '__main__':
    main(sys.argv[1:])
