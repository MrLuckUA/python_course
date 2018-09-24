#! /usr/bin/python3
# -*-coding: utf-8-*-

# Size door
width: int = int(input("Enter width of door: "))
height: int = int(input("Enter height of door: "))

# Size box
x: int = int(input("Enter x of box: "))
y: int = int(input("Enter y of box: "))
z: int = int(input("Enter z of box: "))


def check():
    res = [z < height or z < width, x < height or x < width, y < height or y < width]
    return res.count(True) == 2


print(check())
