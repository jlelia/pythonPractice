# Exercise 16: Mode

def mode(numbers):
    most = None
    mostCount = 0
    counter = {}
    if len(numbers) == 0:
        return None
    for n in numbers:
        if n not in counter:
            counter[n] = 0
        counter[n] += 1
        if counter[n] > mostCount:
            most = n
            mostCount = counter[n]
    return most
        
testSet = [1, 1, 2, 4, 6, 9]
mode(testSet)

assert mode([]) == None
assert mode([1, 2, 3, 4, 4]) == 4
assert mode([1, 1, 2, 3, 4]) == 1
import random
random.seed(42)
testData = [1, 2, 3, 4, 4]
for i in range(1000):
    random.shuffle(testData)
    assert mode(testData) == 4