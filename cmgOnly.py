import random

motoX3M       = list(range(1,26))
motoX3Mwinter = list(range(1,26))
motoX3Mpool   = list(range(1,23))
motoX3Mspooky = list(range(1,23))


games     = [motoX3M, motoX3Mwinter, motoX3Mpool, motoX3Mspooky]
gamesName = ["Moto X3M", "Moto X3M Winter", "Moto X3M Pool Party", "Moto X3M Spooky Land"]
while True:
    gameIndex = random.randint(0,3)

    name       = gamesName[gameIndex]
    chosenGame = games[gameIndex]

    level = chosenGame[random.randint(0, len(chosenGame) - 1)]


    print(name)
    print("Level:", level)
    
    
    if input() == "end":
        break
