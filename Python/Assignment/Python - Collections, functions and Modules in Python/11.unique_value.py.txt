"""Write a Python function that takes a list and returns a new list with unique
elements of the first list.
"""
def un():
    list1 = [1,5,8,20,35,67,2,5,1,20]

    print("original list : ",list1)

    my_unique = list(set(list1)) #set method remove the same element in list

    print("print unique number in list : ",my_unique)


un()