q1 = "Vilken är Sveriges Huvudstad?"
q1_alt = ["Oslo","Stockholm","Köpenhamn"]
q1_right = "Stockholm"


def question(question,alternatives,correct):
    print(question)
    for i in range(len(alternatives)):
        print(f"{i+1}. {alternatives[i]}")
    answer = int(input("Vilket Nummer? "))
    if alternatives[answer-1] == correct:
        return 1
    else:
        return 0

score = 0
score += question(q1,q1_alt,q1_right)
print(f"Your score is {score}\n")
