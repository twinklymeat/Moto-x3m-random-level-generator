import random

motoX3M = []
motoX3Mpool = []
motoX3Mspooky = []
motoX3Mwinter = []

for i in range(1,26):
    motoX3M.append(i)
    motoX3Mwinter.append(i)
    if i <= 22:
        motoX3Mspooky.append(i)
        motoX3Mpool.append(i)

games = [motoX3M, motoX3Mspooky, motoX3Mwinter, motoX3Mpool]
gameStr = ["Moto X3M", "Moto X3M Spooky Land", "Moto X3M Winter", "Moto X3M Pool Party"]
gameInt = random.randint(0, len(games)-1)
chosenGame = games[gameInt]
chosenLevel = chosenGame[random.randint(0,len(chosenGame)-1)]

print(gameStr[gameInt])
print("Level:", chosenLevel)