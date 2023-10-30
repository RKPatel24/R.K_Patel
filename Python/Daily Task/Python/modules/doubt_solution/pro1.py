'''
    zip :


'''
'''

t1 = ("Tv","AC","Mobile")

t2 = (45000,78000,1500)

data = tuple(zip(t1,t2))

print(data)

'''
'''
----------------------------------------------------------------------------------------
 Vowal
'''
'''
l1 = ["a","e","i","o","u"]


letter = input("Enter letter : ")
if letter not in l1:
    print("not vowal")
else:
    print("vowal")

'''

'''
write a python program to sum of three given integers. However, if two values are equal sum will be zero
'''

n1 = int(input("Enter n1 : "))
n2 = int(input("Enter n2 : "))
n3 = int(input("Enter n3 : "))

ans = 0
if n1==n2 or n1==n3 or n2==n3:
    ans = 0
else:
    ans = n1 + n2 + n3

print(ans)

