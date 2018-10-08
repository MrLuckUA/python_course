#! /usr/bin/python3
# -*- coding: utf-8 -*-S

letters = ['a', 'o', 'u', 'i', 'e', 'y']


def num_of_letter(line: str) -> int:
    return sum([line.count(i) for i in letters])


print(num_of_letter(input()))
