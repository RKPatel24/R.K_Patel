"""
Write a Python program to find the repeated items of a tuple.
"""

tup = (1,4,5,7,5)

for i in tup:
    if tup.count(i) >1 :
        print(i)
        
        
