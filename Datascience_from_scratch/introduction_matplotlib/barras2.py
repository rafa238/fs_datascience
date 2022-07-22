#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  6 14:07:15 2022

@author: rafajl
"""
from matplotlib import pyplot as plt

mentions = [500, 505]
years = [2017, 2018]

plt.bar(years, mentions)
plt.xticks(years)
plt.ylabel("# of times i herad someone say 'Data science'")

plt.ticklabel_format(useOffset=False)
plt.title("Look at the huge increase")
plt.axis([2016.5, 2018.5, 499, 506])

plt.show()