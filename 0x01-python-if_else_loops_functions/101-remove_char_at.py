#!/usr/bin/python3


def remove_char_at(str, j):
    if j >= 0:
        return (str[:j] + str[(j + 1):])
    else:
        return (str)

