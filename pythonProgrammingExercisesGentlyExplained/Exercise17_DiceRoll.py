# Exercise 17: Dice Roll
import random

def rollDice(numberOfDice):
    dice = []
    for n in range(1, numberOfDice+1):
        dice.append(random.randint(1,6))
    sum = 0
    for n in dice:
        sum += n
    return sum

def rollDiceOfSideN(numberOfDice, N):
    dice = []
    for n in range(1, numberOfDice+1):
        dice.append(random.randint(1,N))
    sum = 0
    for n in dice:
        sum += n
    return sum

print(rollDiceOfSideN(2, 10))


assert rollDice(0) == 0
assert rollDice(1000) != rollDice(1000)
for i in range(1000):
    assert 1 <= rollDice(1) <= 6
    assert 2 <= rollDice(2) <= 12
    assert 3 <= rollDice(3) <= 18
    assert 100 <= rollDice(100) <= 600