# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
random.seed(10) #get the same result every time
print(random.random())
random.seed(10)
print(random.random())
#we get the same result by the seed


random.randrange(3,  6) #takes one number between 3 and 6, [3,4,5]

#shuffle
up_to_ten = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(up_to_ten) #reorder in a random sequence
print(up_to_ten)

best_friend = random.choice(["Bob", "Karl", "Louis"]) #pick a random value from the collection

lotery_numbers=range(30)
winning_numbers = random.sample(lotery_numbers, 6) #takes a sample from the collection without duplicates

four_winners = [random.choice(range(10)) for _ in range(4)]#4 elements


