#!/usr/bin/env/python3
# -*- coding: utf8 -*-


def get_rand():
    number = "654321"
    while True:
        seed = str(int(number[3:] + number[:3]) * int(number))
        seed = "0" * (12 - len(seed)) + seed[:]
        number = seed[3:9]
        yield number


a = get_rand()
print(*[a.__next__() for _ in range(16)], sep=', ')
