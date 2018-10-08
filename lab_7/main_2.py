#! /usr/bin/python3
# -*- coding: utf-8 -*-S


def is_palindrome(line: str) -> bool:
    formatted_line = ''.join(e for e in line.lower() if e.isalnum())
    return formatted_line == formatted_line[::-1]


print(is_palindrome(input()))
