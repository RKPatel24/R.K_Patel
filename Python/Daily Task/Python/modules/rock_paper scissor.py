import random

menu = '''
                    MANU

                choose your choice

                        ROCK
                        PAPER
                        SCISSOR 

'''

game_list = ["ROCK","PAPER","SCISSOR"]
computer = random.choice(game_list)

status = True
while status:

    print(menu)
    user_choice = input("Enter your choice : ").upper()

    print("COMPUTER CHOICE : ",computer)
    if user_choice == computer:
        print("TIE")
    elif user_choice == "ROCK" and computer == "PAPER":
        print("COMPUTER WON")
    elif user_choice == "ROCK" and computer == "SCISSOR":
        print("USER WON")

    elif user_choice == "PAPER" and computer == "ROCK":
        print("USER WON")
    elif user_choice == "PAPER" and computer == "SCISSOR":
        print("COMPUTER WON")

    elif user_choice == "SCISSOR" and computer == "ROCK":
        print("COMPUTER WON")
    elif user_choice == "SCISSOR" and computer == "PAPER":
        print("USER WON")


    exit_choice = input("do you want to play again ? press y for yes and press n for no : ")
    if exit_choice == 'y' or exit_choice == 'Y':
        status = True
    else:
        status = False