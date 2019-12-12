#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    end = len(sys.argv)
    i = 1
    if end == 1:
        print(0)
    elif end == 2:
        print(int(sys.argv[1]))

    else:
        i = 1
        suma = 0
        for i in range(i, end):
            suma += int(sys.argv[i])
        print(suma)
