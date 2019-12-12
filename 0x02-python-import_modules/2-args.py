#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    end = len(sys.argv)
    i = 1
    if end == 2:
        print("{:d} argument:".format(end - 1))
        print("{:d}: {:s}".format(i, sys.argv[i]))
    if end == 1:
        print("{:d} arguments.".format(end - 1))
    else:
        print("{:d} arguments:".format(end - 1))
        for i in range(i, end):
            print("{:d}: {:s}".format(i, sys.argv[i]))
