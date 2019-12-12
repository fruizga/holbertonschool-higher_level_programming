#!/usr/bin/python3
import sys
end = len(sys.argv)
i = 1
if end == 2:
    print("{:d} argument:".format(end - 1))
    print("{:d}: {:s}".format(i, sys.argv[i]))
else:
    print("{:d} arguments:".format(end - 1))
    for i in range(i, end):
        print("{:d}: {:s}".format(i, sys.argv[i]))
