#! /usr/bin/env/python3
# -*- coding: utf-8 -*-

first_line = set(sorted(''.join([a for a in input() if a.isalnum()])))
second_line = set(sorted(''.join([a for a in input() if a.isalnum()])))

print(first_line)
print(second_line)

for i in second_line:
    if i not in first_line:
        print("We can't do it")
        break
else:
    print("We can do it")
