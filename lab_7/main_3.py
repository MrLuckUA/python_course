#! /usr/bin/python3
# -*- coding: utf-8 -*-S


def is_brackets_done(line: str) -> bool:
    opening = tuple('({[')
    closing = tuple(')}]')
    mapping = dict(zip(opening, closing))
    queue = []

    for letter in line:
        if letter in opening:
            queue.append(mapping[letter])
        elif letter in closing:
            if not queue or letter != queue.pop():
                return False
    return not queue


print(is_brackets_done(input()))
