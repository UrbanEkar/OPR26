import requests
urlTrivia = "https://opentdb.com/api.php?amount=2&type=multiple"

kt = requests.get(urlTrivia).json()

rez = kt["results"]

ques = kt["results"]

print(ques)

print(len(rez))

for r in rez:
    print("-"*80)
    question = r["question"]
    correct = r["correct_answer"]
    incorrect = r["incorrect_answers"]
    print(type(correct), type(incorrect))

    sez = incorrect + [correct]

    print(question)
    print(sez)

    izbira = input("Pick a choice: ")

    if izbira == correct:
        print("Pravilen odgovor")
    elif izbira != correct:
        print("Napačen odgovor")
        print("Pravilen odgovor je", correct)
