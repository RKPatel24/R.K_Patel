e_list = []
o_list = []

for i in range(1,6):
    num = int(input("Enter number : "))
    if num>0:
        e_list.append(num)
    else:
        o_list.append(num)


print("positive number :")
for i in e_list:
    print(i)


print("nagative number : ")
for j in o_list:
    print(j)

# accept 6 number from user and positive and nagative numbers