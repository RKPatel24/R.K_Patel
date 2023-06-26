""" Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.

"""

str1 = input("Enter a string: ")
dic = {} #creates an empty dictionary
for check in str1:
    if check in dic: #if next character is already in the dictionary
        dic[check] += 1
    else:
        dic[check] = 1 #if ch appears for the first time

for key in dic:
    print(key,':',dic[key])