#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 13:50:03 2022

@author: rafajl
"""

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

pairs = [pair for pair in zip(lis1. list2)] #it returns [(a,1), (b,2), (c,3)]


# * unpacking argument uses the elements of pairs as individual arguments

letters, numbers = zip(*pairs) #we unzip with operator *
