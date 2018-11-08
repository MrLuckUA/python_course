#! /usr/bin/python3
# -*- coding: utf-8 -*-S
import random


def prog() -> str:
    number = random.randrange(1, 101)
    print(number)
    result = ""
    if number % 3 == 0:
        result += 'Fizz'
    if number % 5 == 0:
        result += 'Bizz'
    return result


print(prog())
