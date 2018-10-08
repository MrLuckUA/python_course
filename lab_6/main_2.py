#! /usr/bin/python3
# -*- coding: utf-8 -*-


def ui_deposit_input() -> list:
    """
    This function make input for 3 side of triangle
    :return: List of 3 sides of triangle
    """
    amount = int(input("Enter amount: "))
    percentage = int(input("Enter percentage in %: "))
    years = int(input("Enter years: "))
    return [amount, percentage, years]


def ui_area_output(final_amount: float):
    """
    This function print area of triangle
    :param final_amount: Final amount after deposit
    """
    print(f'Final amount = {final_amount}')


def bl_calculate_deposit(amount: int, percentage: int, years: int) -> float:
    """
    This function calculate amount of deposit
    :param amount: Start amount
    :param percentage: Bank percentage
    :param years: Time of deposit
    :return: Amount of deposit
    """

    return amount * (1 + (percentage / 100) / 1) ** years


ui_area_output(bl_calculate_deposit(*ui_deposit_input()))
