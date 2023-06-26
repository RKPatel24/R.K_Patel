"""
Write a Python program to check whether a list contains a sub list 
"""

list1 = [20,30,40,50,60,70]
list2 = [40,70]



for i in list1:  #loop start in list1 0 to n element
    for j in list2: #loop start in list2 o to n element
        if i == j :  #check the element will be same or not 
            print(i) #same value store in i and print same number