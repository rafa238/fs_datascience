#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 20:15:20 2022

@author: rafajl
"""
from matplotlib import pyplot as plt
movies=["Annie Hall", "Ben-hur", "Casablanca", "Gandhi", "West Slide Story"]
num_oscars = [5, 11, 3, 8, 10]
plt.bar(range(len(movies)), num_oscars)

plt.title("Oscar Movies")
plt.ylabel("# of Academy awards")

plt.xticks(range(len(movies)), movies)
plt.show()

