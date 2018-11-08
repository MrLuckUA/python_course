#!/usr/bin/env/python3
# -*- coding: utf8 -*-


def get_rand():
    seed = "654321"
    while True:
        number = str(int(seed[3:] + seed[:3]) * int(seed))
        number = "0" * (12 - len(number)) + number[:]
        seed = number[3:9]
        yield seed


a = get_rand()
print(*[a.__next__() for _ in range(16)], sep=', ')
