"""
Write a Python program to remove an empty tuple(s) from a list of tuples.
"""

l1 = [(),('abc'),('xyz')]

l2 =[]

for i in range(0,len(l1)):
    if len(l1[i])==0:
        continue
    else:
        l2.append(l1[i])
print(l2)