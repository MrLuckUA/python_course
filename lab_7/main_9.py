#! /usr/bin/env/python3
# -*- coding: utf-8 -*-


def if_lucky(ticket: int) -> bool:
    ticket = [int(i) for i in str(ticket)]
    return sum(ticket[:3]) == sum(ticket[3:])


print(if_lucky(117234))
