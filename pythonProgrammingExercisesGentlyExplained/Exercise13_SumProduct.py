# Exercise 13: Sum & Product

def calculateSum(numbers):
    Sum = 0
    if len(numbers) == 0:
        return 0
    for j in range(len(numbers)):
        Sum += numbers[j]
    return Sum

assert calculateSum([]) == 0
assert calculateSum([2, 4, 6, 8, 10]) == 30

def calculateProduct(numbers):
    product = 1
    if len(numbers) == 0:
        return 1
    for i in range(len(numbers)):
        product *= numbers[i]
    return product

assert calculateProduct([]) == 1
assert calculateProduct([2, 4, 6, 8, 10]) == 3840