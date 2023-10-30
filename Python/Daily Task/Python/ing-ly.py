mystr=input("Enter a string:-")

if len(mystr)<3:
    print("unchange",mystr)

elif mystr.endswith('ing'):
    mystr+="ly"

elif len(mystr)>=3:
    mystr+="ing"

    print(mystr)