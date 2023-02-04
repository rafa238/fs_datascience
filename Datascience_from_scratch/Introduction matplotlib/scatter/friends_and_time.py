# -*- coding: utf-8 -*-
"""
Scatter plot is a right choice for visualizing relationship between two paired 
sets of data.
For example:
Let's ilustrate the number of friends of users and the time they spend
on the site every day
"""

from matplotlib import pyplot as plt

friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

#label each point
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label, 
                 xy=(friend_count, minute_count),
                 xytext=(5, -5),
                 textcoords='offset points')

plt.title("Daily minutes vs. # of friends")
plt.xlabel("# of friends")
plt.ylabel("Daily minutes spent on site")
plt.show()

