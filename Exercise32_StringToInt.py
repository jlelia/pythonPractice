# Exercise 32: String to Integer

def convertStrToInt(stringNum):
    strArray = []
    intArray = []
    sum = 0
    sign = ''
    DIGIT_DICTIONARY = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, 
                        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    
    if stringNum[0] == '-':
        stringNum = stringNum.strip('-')
        sign += '-'

    digitMultiplier = 10**(len(stringNum)-1)

    for i in range (0, len(stringNum)):
        # Set up string as individual integer digits
        strArray.append(stringNum[i])
        intArray.append(DIGIT_DICTIONARY[strArray[i]])

        # Multiply each integer by its digit value
        sum += intArray[i] * digitMultiplier
        digitMultiplier //= 10

    if sign == '-':
        sum = -sum

    return sum

for i in range(-10000, 10000):
    assert convertStrToInt(str(i)) == i