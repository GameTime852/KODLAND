import random

litery = '"+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEF'
dlugosc = int(input("jak długie ma być hasło? "))
haslo = ""

for i in range(dlugosc):
    haslo = haslo + random.choice(litery)

print("Twoje wygenerowane hasło to: " + haslo)