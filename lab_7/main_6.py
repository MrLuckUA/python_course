#! /usr/bin/python3
# -*- coding: utf-8 -*-S


def star_print(line: str) -> str:
    return f'{"*" * (len(line) + 4)}\n* {line} *\n{"*" * (len(line) + 4)}'


print(star_print("Hello wold"))
