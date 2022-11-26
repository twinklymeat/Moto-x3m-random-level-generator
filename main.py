import random
import sys


while True:
    inputs = input("type 1 for random, 2 for only CMG: ")
    if inputs == "2":
        exec(open("cmgOnly.py").read())
        sys.exit()
    elif inputs == "1":
        break


motoX3M           = list(range(1,26))
motoX3Mpool       = list(range(1,23))
motoX3Mspooky     = list(range(1,23))
motoX3Mwinter     = list(range(1,26))
motoX3Mpoki       = list(range(1,51))
motoX3MspookyPoki = list(range(1,33))

#initializes lists
games     = [motoX3M, motoX3Mspooky, motoX3Mwinter, motoX3Mpool] #makes a list containing all the lists with level numbers
gamesPoki = [motoX3Mpoki, motoX3MspookyPoki, motoX3Mwinter, motoX3Mpool]
gameStr   = ["Moto X3M", "Moto X3M Spooky Land", "Moto X3M Winter", "Moto X3M Pool Party"]
platforms = ["CMG", "Poki"]

#chooses items from lists with random numbers
while True:
    chosenPlat = random.choice(platforms)
    gameInt = random.randint(0, len(games)-1)
    if chosenPlat == "Poki":
        chosenGame = gamesPoki[gameInt]
    else:
        chosenGame = games[gameInt]
    chosenLevel = chosenGame[random.randint(0,len(chosenGame)-1)]

    print(gameStr[gameInt], chosenPlat)
    print("Level:", chosenLevel)
    if input() == "end":
        break