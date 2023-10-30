# dynamic dictionary

# blan dictionary

students = {} # data set


status = True
while status:
    email = input("Enter your email address : ")
    name = input("Enter your name : ")

    # store key amd value in dectionary
    students[email] = name

    choice = input("do you want to continue press y for yes : ")
    if choice == 'y':
        status = True
    else:
        status = False
print(students)

# accept email from user
u_email = input("Enter your email : ")


# fetch value from dectionary by key
print(students[u_email])