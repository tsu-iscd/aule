""" Testing utils. """
import os


def get_tests(file, begin, end):
    with open(file, "r") as f:
        tests = []
        for line in f:
            if line.strip() == begin:
                test = ""
                for line in f:
                    if line.strip() == end:
                        break
                    test += line
                tests.append(test)
    return tests


def get_tests_from_file(file, begin, end):
    with open(file, "r") as f:
        tests = []
        for line in f:
            if line.strip() == begin:
                test = ""
                for line in f:
                    if line.strip() == end:
                        break
                    test += line
                tests.append(test)
    return tests


def get_tests_from_dir(path):
    tests = []
    files = os.listdir(path)
    for file in files:
        fname = path + file
        tests.extend(get_tests_from_file(fname, "#begin", "#end"))
    return tests
