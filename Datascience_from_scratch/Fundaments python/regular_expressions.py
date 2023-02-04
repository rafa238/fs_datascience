#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 23:09:06 2022

@author: rafajl
"""

import re

re_examples = [
    not re.match("a", "cat"), #it doesn't begin with a
    re.search("a", "cat"), #cat has an a in it
    3 == len(re.split("[ab]", "carbs")), #split 'a' and 'b' to ['c', 'r', 's']
    "R-D-" == re.sub("[0-9]", "-", "R2D2")
    ]

assert all(re_examples)