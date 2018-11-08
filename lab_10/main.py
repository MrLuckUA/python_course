#!/usr/bin/env/python3
# -*- coding: utf8 -*-

img_bin = list()
with open('img.bmp', 'r+b') as img:
    for i in img:
        for b in i:
            img_bin.append(b)
    img.close()
message = list()
with open('message.txt', 'r+b') as txt:
    for i in txt:
        for b in i:
            message.append(b)

# Write to file
key = len(message)
img_bin[len(img_bin) // 2] = key
c_key = key
for i in message:
    img_bin[len(img_bin) - c_key] = i
    c_key -= 1

with open("img_crypt.bmp", 'w+b') as img_crypt:
    img_crypt.write(bytearray(img_bin))
    img_crypt.close()

img_en = list()
with open('img_crypt.bmp', 'r+b') as img_encrypt:
    for i in img_encrypt:
        for b in i:
            img_en.append(b)
    img_encrypt.close()

# Read from file
txt_en = list()
crypt_key = img_en[len(img_en) // 2]
for i in message:
    txt_en.append(img_en[len(img_en) - crypt_key])
    crypt_key -= 1

print([bytes([t]) for t in txt_en])
