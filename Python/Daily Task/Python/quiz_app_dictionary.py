# quiz dictionary - Nested dictionary

quiz = {
    1 : {
        "que" : "most popular programing language"
        "ans" : "python"
    }
    2 : {
        "que" : "Hyper text markup language shot from",
        "ans" : "html",
    },
}
score = 0
for i in range(1,len(quiz)+1):
    print(f"{i}) {quiz[i]['que']} ")
    answer = input("Enter your ans : ")

    #logic implementation
    if answer == quiz[i]["ans"]:
        print("Rignt answer")
        score+=50
    else:
        print("wrong answer")
        score -= 20

print("YOUR SCORE = " ,score)