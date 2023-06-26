"""Write a Python function to check whether a number is in a given range
"""
def test(i):
    if i in range(1,10) :
        print("given range : ",str(i))
    else :
        print("not in given range")

test(15)