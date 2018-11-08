#! /usr/bin/env/python3
# -*- coding: utf-8 -*-


def len_of_short_word(line: str) -> int:
    clean_words = ''.join(e for e in line.lower() if e.isalpha() or e == ' ').split()
    return len(sorted(clean_words, key=lambda word: len(word))[0])


print(len_of_short_word("ahon, Some, kjkh sas cool, awesome"))
