from random import randrange
from sys import exit

def getInt():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            continue
        break
    return n

n = getInt()
while n<1:
    n= getInt()

target = randrange(1,n)
guess = -1
while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue

    if guess<1:
        continue

    if target == guess:
        print("Just right!")
        exit()

    if guess>target:
        print("Too large!")
        continue

    if guess<target:
        print("Too small!")
        continue
