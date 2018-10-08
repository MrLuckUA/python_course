#! /usr/bin/python3
# -*- coding: utf-8 -*-S


def crypt(line: str) -> str:
    result = str()
    for symbol in line:
        result += chr(ord(symbol) + 1)
    return result


print(crypt(input()))
