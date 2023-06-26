import random

f = open("hello.txt", "r")

lines = f.readlines()

print(random.choice(lines))