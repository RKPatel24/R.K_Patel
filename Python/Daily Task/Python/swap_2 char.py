str1=input("Enter the first string:-")

str2=input("Enter the second string:-")

x=str1[0:2]

str1=str1.replace(str1[0:2],str2[0:2])
str2=str2.replace(str2[0:2],x)

print("First string has become:",str1)
print("Second string has become:",str2)