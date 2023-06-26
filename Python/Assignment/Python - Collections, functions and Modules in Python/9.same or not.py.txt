"""
Write a Python function that takes two lists and returns true if they have
at least one common member.
"""
result=False
def common():
    a=[1,2,3,4,5]
    b=[6,7,5,8,9]
    for i in a:
        for j in b:
            if i==j:
                result= True
    print(result)
common()


