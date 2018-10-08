#! /usr/bin/python3
# -*- coding: utf-8 -*-S


def string_rotate(line: str, num_of_symbol: int) -> str:
    """
    Function make left rotate for string
    :param line: Line to rotate
    :param num_of_symbol: Number of symbol to rotate
    :return: Rotating line
    """
    return line[num_of_symbol:] + line[:num_of_symbol]


print(string_rotate(input(), int(input())))
