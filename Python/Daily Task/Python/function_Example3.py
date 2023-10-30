def findFactorial(num): # 5*4*3*2*1
    f = 1 # factorial initial value = 1

    for i in range (1,num+1):
        f*=i

        print("factorial= ", f)

    # accept number from user

    number = int (input("Enter number : "))

    findFactorial(number)