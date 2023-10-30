'''
    *args and **kargs

    args : arguments   (tuple as a perameter)

    kargs : key with arguments (dictionary as a parameter)

'''

def args_example(*a):
    print(a)


args_example(12,23,34,45,67,98,45)



# dictionary as a parameter

def mydict_example(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}={v}")

mydict_example(name="python",category="programing")