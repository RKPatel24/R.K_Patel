class NagativeExcepetion(Exception):
    pass

try:
    num = int(input("Enter number : "))
    if num<0:
        raise NagativeExcepetion
    else:
        print("num = ",num)
except NagativeExcepetion:
    print("Nagative number entered")