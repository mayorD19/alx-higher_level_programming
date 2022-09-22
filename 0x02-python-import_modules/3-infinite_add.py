#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    total_arg = 0
    for x in range(1, length):
        total_arg += int(argv[x])
    print("{:d}".format(total_arg))
