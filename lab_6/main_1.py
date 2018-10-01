#! /usr/bin/python3
# -*- coding: utf-8 -*-

import math


def bl_area(sides: list) -> float:
    """
    This function calculate area of triangle.
    :param sides: List of 3 sides of triangle
    :return: Area of triangle
    """
    half_perimeter = (1 / 2) * (sides[0] + sides[1] + sides[2])
    return math.sqrt(
        half_perimeter * (half_perimeter - sides[0]) * (half_perimeter - sides[1]) * (half_perimeter - sides[2]))


def ui_triangle_input() -> list:
    """
    This function make input for 3 side of triangle
    :return: List of 3 sides of triangle
    """
    return [int(i) for i in input().split()]


def ui_area_output(area: float):
    """
    This function print area of triangle
    :param area: Area of triangle
    """
    print(f'Area of triangle = {area}')


ui_area_output(bl_area(ui_triangle_input()))
