import random

computer_guess = random.randint(1,100)

status = True

while status:
    user_choice = int(input("Enter your choice : "))
    if user_choice > computer_guess:
        print("HINT : Guess lower number ")
    elif user_choice < computer_guess:
        print("HINT : Guess Higher number")
    else:
        print("RIGHT GUESS")
        status = False