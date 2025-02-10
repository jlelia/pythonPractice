# Exercise 14: Average

def average(numbers):
    if len(numbers) == 0:
        return None
    Sum = 0
    for i in range(len(numbers)):
        Sum += numbers[i]
    return Sum / len(numbers)


assert average([1, 2, 3]) == 2
assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
assert average([12, 20, 37]) == 23
assert average([0, 0, 0, 0, 0]) == 0

import random
random.seed(42)
testData = [1, 2, 3, 1, 2, 3, 1, 2, 3]
for i in range(1000):
    random.shuffle(testData)
assert average(testData) == 2