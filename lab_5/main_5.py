#! /usr/bin/python3
# -*- coding: utf-8 -*-
i = 2
numb = int(input())
while i < numb:
    if numb % i == 0:
        print("Not simple")
        break
    i += 1
else:
    print("Simple number")
