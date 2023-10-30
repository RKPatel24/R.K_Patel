# function witout parameters and function with return types

def checkEvenOdd(number):
    if number % 2 == 0:
        return "Even number"
    else:
        return " Odd number"
    


num = int(input("Enter your number : "))
print(checkEvenOdd(num))