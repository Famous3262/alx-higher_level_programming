#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    count = len(args)

    if count == 0:
        print("Number of argument(s): 0.")
    elif count == 1:
        print("Number of argument(s): 1, argument:")
        print("1: {}".format(args[0]))
    else:
        print("Number of argument(s): {}, arguments:".format(count))
        for i in range(count):
            print("{}: {}".format(i+1, args[i]))
