#!/usr/bin/python3
"""A function that reads a text
"""


def read_file(filename="my_file_0.txt"):
    """A function that reads a text file using the
    with keyword for easy clean-up
    """

    with open(filename, "r", encoding = "utf-8") as f:
        for line in f:
            print(f.read() end="")

