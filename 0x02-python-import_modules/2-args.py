#!/usr/bin/python3
import sys
end = len(sys.argv)
i = 1
print("{:d} arguments:".format(end - 1))
for i in range(i, end):
    print("{:d}: {:s}".format(i, sys.argv[i]))
