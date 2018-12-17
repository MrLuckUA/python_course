#!/usr/bin/env/python3
# -*- coding: utf8 -*-


def all_same(items):
    return all(x == items[0] for x in items)


def table_print(board: list):
    for col in board:
        print('|', end='')
        for row in col:
            print(row, end='|')
        print()


def make_move(board: list, pos_x: int, pos_y: int, val: str):
    board[pos_y - 1][pos_x - 1] = val


def check_draw(board: list) -> bool:
    return '-' not in board


def check_horizontal(board: list) -> tuple:
    for line in board:
        if '-' not in line and all_same(line):
            return True, line[0]
    else:
        return False, ''


def check_vertical(board: list) -> tuple:
    for line in zip(*board):
        if '-' not in line and all_same(line):
            return True, line[0]
    else:
        return False, ''


def check_diagonals(board: list) -> tuple:
    diagonals = [[row[i] for i, row in enumerate(board)],
                 [row[len(row) - 1 - i] for i, row in enumerate(board)]]
    for diagonal in diagonals:
        if '-' not in diagonal and all_same(diagonal):
            return True, diagonal[0]
    else:
        return False, ''


def check_winner(board: list) -> tuple:
    in_game = any(check_diagonals(board)[0])
    if check_diagonals(board)[0]:
        print("here")


# TicTacToe board 3x3
# |-|-|-|
# |-|-|-|
# |-|-|-|
board = [['O', 'X', 'O'],
         ['O', '-', 'X'],
         ['X', 'O', 'O']]

table_print(board)
print(check_winner(board))
