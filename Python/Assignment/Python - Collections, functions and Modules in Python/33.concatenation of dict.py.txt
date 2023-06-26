"""Write a Python script to concatenate following dictionaries to create a
new one."""


dic1={1:"akhil", 2:"nik"}
dic2={3:"ajay", 4:"saiyam"}

dic3 = {}

for i in (dic1, dic2):
    for key, value in i.items():
       dic3[key] = value

print("dic1",dic1)
print("dic1",dic2)
print("concentation of dic1,dic2,dic3 : ",dic3)







