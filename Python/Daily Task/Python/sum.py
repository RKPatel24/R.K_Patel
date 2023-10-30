def sum_of_three_integers (a, b, c):
    if a == b or b == c or a == c:
        return 0
    else:
        return a + b + c
    
num1 = int(input("Enter the first integer : "))
num2 = int(input("Enter the first integer : "))
num3 = int(input("Enter the first integer : "))

result = sum_of_three_integers(num1, num2 , num3)

print("sum of the three integer : ", result)