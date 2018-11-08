#! /usr/bin/python3
# -*- coding: utf-8 -*-S


def to_camel_case(line: str) -> str:
    result = str()
    next_upper = False
    for el in line:

        if next_upper:
            el = el.upper()
            next_upper = False
        if el == '_':
            el = ''
            next_upper = True
        result += el
    return result


def to_snake_case(line: str) -> str:
    result = str()
    for el in line:
        if el.isupper():
            el = '_' + el.lower()
        result += el
    return result


print(to_camel_case('print([res_square ** 2 for res_square in input_array if res_square > 18 ])'))
