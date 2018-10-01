#! /usr/bin/python3
# -*- coding: utf-8 -*-

a, b, c = map(int, input('Enter 3 side: ').split())
print(a + b > c and a + c > b and b + c > a)
