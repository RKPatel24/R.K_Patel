'''
    dicitionary : which is contain key and value ia a pair

    syntax : 

    dictionary_name = {
        "key" : value,
        "key2": value,
        .
        .
    }
'''

# student dicitionary here.
student={
    "name":"raj",
    "subject" : "python",
    "mark" : 85,
}

print(student)

# proper formated display dicitionary

for k,v in student.items():
    print(f"{k} = {v}")