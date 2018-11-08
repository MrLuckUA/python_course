#! /usr/bin/env/python3
# -*- coding: utf-8 -*-


def sort_words(line: str) -> list:
    clean_words = ''.join(e for e in line.lower() if e.isalpha() or e == ' ').split()
    clean_words.sort(key=lambda word: len(word))
    return clean_words


print(*sort_words("ahon, Some, kjkh s cool, awesome"))
