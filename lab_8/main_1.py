#! /usr/bin/env/python3
# -*- coding: utf-8 -*-


count = list(range(10))
step = 3


def dropwhile(predicate, iterable):
    # dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
    iterable = iter(iterable)
    for x in iterable:
        if not predicate(x):
            yield x
            break
    for x in iterable:
        yield x


a = dropwhile(, count)
print(a)
for i in a:
    print(i)
