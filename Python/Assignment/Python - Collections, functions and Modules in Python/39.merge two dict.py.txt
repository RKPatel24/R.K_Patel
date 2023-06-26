"""Write a Python script to merge two Python dictionaries """

d1 = {1:"aki",2:"nik"}
d2 ={3:"abc",4:"xyz"}

z = d1.copy()  # copy of d1 and store in z
z.update(d2)   #after store d2 in z
print(z)

