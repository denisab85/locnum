# ===================================================
#  Application name: locnum test
#  Interpreter: Python 3.6
#  Description: functional tests for locnum, uses test.txt for test cases
#  Version: 0.1
#  Date: 05/31/2017
#  Author: Denis Abakumov
# ===================================================

from locnum import LocalNumeral
from collections import Counter


test_file = None
try:
    test_file = open("test.txt")
except:
    print("Error opening file")

total_cnt = Counter({True: 0, False: 0})

dictionary = ""
ln = None

if test_file:
    for line in test_file.readlines():
        line = line.strip()
        if not len(line):
            dictionary = ""
        else:
            if dictionary == "":
                dictionary = line
                print("\nLoading dictionary: '{}'".format(dictionary))
                ln = LocalNumeral(dictionary)
                # test 2-way coversion of the maximum possible abbreviated value for this dictionary
                result = (ln.to_loc(ln.to_int(dictionary)) == dictionary)
            else:
                tokens = line.split(":")
                method = tokens[0].strip()
                parameter = tokens[1].strip()
                expected = tokens[2].strip()
                print("Testing: {}('{}') == '{}'.".format(method, parameter, expected))
                if method == "to_loc":
                    result = (ln.to_loc(parameter) == expected)
                elif method == "to_int":
                    result = (str(ln.to_int(parameter)) == expected)
                elif method == "abbreviate":
                    result = (ln.abbreviate(parameter) == expected)
            print(result)
            total_cnt[result] += 1


    print("\n============ totals ============")
    for cnt, num in total_cnt.items():
        print("{}: {}".format(cnt, num))
