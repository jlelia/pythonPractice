# Exercise 31: Integer to String

# I'm guessing this is cheating so I will try to think of another way lol
def convertIntToStrEasy(integerNum):
    return f'{integerNum}'

def convertIntToStr(integerNum):
    if integerNum == 0:
        return '0'
    
    string = ''
    sign = ''
    DIGIT_DICTIONARY = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
    
    if integerNum < 0:
        sign = '-'

    posIntegerNum = abs(integerNum)

    while posIntegerNum != 0:
        string = DIGIT_DICTIONARY[posIntegerNum % 10] + string 
        posIntegerNum //= 10

    return sign + string

for i in range(-10000, 10000):
    assert convertIntToStr(i) == str(i) 