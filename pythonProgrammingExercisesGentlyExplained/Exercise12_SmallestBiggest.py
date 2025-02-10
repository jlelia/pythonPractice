# Exercise 12: Smallest & Biggest

# first attempt
def getSmallestStupid(numbers):
    i = 0
    j = 1
    sortedNumbers = []
    while i != len(numbers) - 1:
        while numbers[i] <= numbers[j] and j < len(numbers):
            i += 1
            j += 1
        if numbers[i] > numbers[j] and j < len(numbers):
            sortedNumbers.append(numbers[i])
            i += 1
            j += 1      
    print(sortedNumbers)

# second attempt after reading more
def getSmallest(numbers):
    if len(numbers) == 0:
        return None
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

def getBiggest(numbers):
    if len(numbers) == 0:
        return None
    biggest = numbers[0]
    for number in numbers:
        if number > biggest:
            biggest = number
    return biggest

assert getSmallest([1, 2, 3]) == 1
assert getSmallest([3, 2, 1]) == 1
assert getSmallest([28, 25, 42, 2, 28]) == 2
assert getSmallest([1]) == 1
assert getSmallest([]) == None

print(getBiggest([1,5,2,10,19,23,3,4]))