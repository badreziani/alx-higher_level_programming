#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argc = len(argv)
    if argc <= 0:
        print("0 arguments.")
    else:
        s = "" if argc == 1 else "s"
        print("{:d} argument{:s}:".format(argc, s))
        for i, arg in enumerate(argv):
            print("{:d}: {:s}".format(i + 1, arg))
