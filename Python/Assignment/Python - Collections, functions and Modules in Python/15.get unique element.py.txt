"""
Write a Python program to get unique values from a list 
"""

list1 = [1,3,5,5,3,4,8,9,10]

print("original list : ",list1)

my_unique = list(set(list1)) #set method remove the same element in list

print(my_unique)
