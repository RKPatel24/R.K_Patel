"""34.Write a Python script to check if a given key already exists in a
dictionary.
"""

dict1 = {1:20,2:50,3:100,4:500}
def key_present(i):
    if  i in dict1:
        print("key already exist in dictionary")
    else:
        print("key is not present in dictionary")
        
key_present(5)
key_present(2)



