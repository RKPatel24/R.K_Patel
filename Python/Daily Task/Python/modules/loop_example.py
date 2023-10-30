e_list = []
o_list = []

for i in range(1,6):
    num = int(input("Enter number : "))
    if num%2==0:
        e_list.append(num)
    else:
        o_list.append(num)


print("Even List :")
for i in e_list:
    print(i)


print("odd List : ")
for j in o_list:
    print(j)