#API osnovna vaja
#Ugotovi najstarejše ime

import requests

imena = ["Urban", "Gregor", "Luka", "Danilo", "Simona"]

"""
for i, imena in enumerate(imena):
    print(imena)"""

najstarejsi = 0


for i, imena in enumerate(imena):
    ime = "https://api.agify.io?name={imena}"

    call = requests.get(ime).json()

    print(call)
    print(call["name"], ["age"])
"""

for i, ime in enumerate(imena):
    ime = "https://api.agify.io?name={ime}"

    call = requests.get(ime).json()
    call_age = requests.get(age).json()

    if call_age > najstarejsi:
        najstarejsi = call_age
    print(call["name"], ["age"])



"""
"""
imena = ["Luka", "Jaka", "Bine"]

#for i in (range(len(imena))):
#    print(imena[i])

for i in imena:
    print(i)

# enumerate

print(list(enumerate(imena)))

for i, imena in enumerate(imena):
    print(imena)

"""