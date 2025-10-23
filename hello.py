import random

questions = ["Vilken är Sveriges Huvudstad?","Vad heter senaste Minecraft versionen?"]
alternatives = [["Oslo","Stockholm","Köpenhamn"],["1.22.1","1.21.10","1.21.4","1.22.5","1.22","1.21.8"]]
rights = ["Stockholm","1.21.10"]

def question(question,alts,correct):
    print(question)
    random.shuffle(alts)
    for i in range(len(alts)):
        print(f"{i+1}. {alts[i]}")
    answer = int(input("Vilket Nummer? "))
    if alts[answer-1] == correct:
        print("Rätt")
        return 1
    else:
        print(f"Fel, rätt svar var {correct}")
        return 0

score = 0
for i in range(len(questions)):
    score += question(questions[i],alternatives[i],rights[i])
    print(f"Your score is {score} / {i+1}\n")
