"""
defaultdict:
Is a regular dictionary, when you try to look up a key 
that it doensn't contain, adds a value for it using a zero-argument
"""
from collections import defaultdict
word_counts = defaultdict(int) #receives the data type argument
word_counts[2] = word_counts[2] + 3 #word_count initialize in 0
print(word_counts)

"""
Counters:  
Turns a sequence of values into a defaultdict
"""
from collections import Counter
coun = Counter([0, 1, 2, 0]) #returns a defaultdict {0:2, 1:1, 2:1}
print(coun)

"""
Set:
Set represents a collection of distinct elements
"""
s = set()
s.add(1)
s.add(2)
s.add(2)
x = len(s) #return an integer which is the lenght of the set
y = 2 in s #return True, set is containig number 2
z = 3 in s #return False, set doesn't contain number 3
print("set:", x, y, z)

"""
Sorting
"""
c = [4,1,3,2]
y = sorted(c) #y is the c sorted list
c.sort() #c convert in a sorted list
print("sort list:", c, " and: ", y)

for b in [1, -1]:
    print(b)
    
range()
