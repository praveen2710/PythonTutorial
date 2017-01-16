import random

def diceRoll():
    for x in range(5):
        result = random.randint(1,6)
        print(result)

diceRoll()