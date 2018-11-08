#!/usr/bin/env/python3
# -*- coding: utf-8 -*-


def int_sort(iter_int: list) -> int:
    max_el = iter_int[0]
    for i in iter_int:
        if i > max_el:
            max_el = i
    return max_el


print(int_sort([10, 40, 30]))
