"""Write a Python program to find the highest 3 values in a dictionary """

dict = {"a":111,"b":150,"c":14,"d":20,"e":50,"f":100}

dic1 = sorted(dict.values())

print(dic1)

print(sorted(dic1[3:],reverse=True))
