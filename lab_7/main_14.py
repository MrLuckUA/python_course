#! /usr/bin/env/python3
# -*- coding: utf-8 -*-

import re

email = input()
if not re.match(r'^[\w.+\-]+@[\w]+\.[a-z]{2,3}$', email):
    print("Wrong email")
else:
    print("All done")
