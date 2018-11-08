#!/usr/bin/env/python3
# -*- coding: utf8 -*-


def parse_nginx_log(filename: str) -> str:
    with open(filename, 'r') as log:
        for line in log:
            yield line.split()[9]


a = parse_nginx_log("2017_05_07_nginx-1.txt")
count = 0
for s in a:
    count += int(s)

print(count)

# import subprocess
#
# f = subprocess.Popen(['tail', '-F', "2017_05_07_nginx-1.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# while True:
#     line = f.stdout.readline()
#     print(line)
