#! /usr/bin/python3
# -*- coding: utf-8 -*-

import cmath

a, b, c = map(int, input('Enter a, b, c:').split())

discriminator = b ** 2 - 4 * a * c

discriminator_sqrt = cmath.sqrt(discriminator)

if discriminator < 0:
    x1 = complex((-b + discriminator_sqrt) / (2 * a))
    x2 = complex((-b - discriminator_sqrt) / (2 * a))
elif discriminator == 0:
    x1 = -b / (2 * a)
    x2 = -b / (2 * a)
elif discriminator > 0:
    x1 = (-b - discriminator_sqrt) / (2 * a)
    x2 = (-b + discriminator_sqrt) / (2 * a)
print(f'x1 = {x1}\nx2 = {x2}')
