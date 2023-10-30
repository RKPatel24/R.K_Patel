# function without parameter and function with return type

def checkPosNeg():
    num = int(input("Enter number : "))
    if num>0:
        return "Positive Number"
    else:
        return "Nagative Number"
    
print(checkPosNeg())