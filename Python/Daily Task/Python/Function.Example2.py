'''
    Function with parameters and without return types

    syntax : 

    def funname(parameter) :
        block of code

'''

def mysum(num1,num2):
    ans = num1 + num2
    print(ans)


    # function calling
    n1 = int(input("Enter number 1 : "))
    n2 = int(input("Enter number 2 : "))

    mysum(n1,n2)