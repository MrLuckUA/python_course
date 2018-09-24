#! /usr/bin/python3
# -*-coding: utf-8-*-

import random


def human_win(human_move_id, computer_move_id):
    if human_move_id == computer_move_id:
        return "Draw"
    elif human_move_id == 0 and computer_move_id == 2:
        return "YOU WIN!!!!!!!"
    elif human_move_id > computer_move_id and human_move_id != 2:
        return "YOU WIN!!!!!!!"
    else:
        return "YOU LOSE!!!!!!"


moves = ["Rock", "Paper", "Scissors"]

while True:
    print('*****NEW GAME*****')
    human_move = moves[
        (int(input("Your move hoose one & press enter:\n1. Rock\n2. Paper\n3. Scissors\nYour choose: ")) - 1)]
    computer_move = moves[random.randrange(0, 3)]
    print(human_move + " VS " + computer_move)
    print(human_win(moves.index(human_move), moves.index(computer_move)), end='\n\n\n')
