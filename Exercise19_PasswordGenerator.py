# Exercise 19: Password Generator
import random

SPECIAL = '~!@#$%^&*()_+'
UPPER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
LOWER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '0123456789'
CHARACTERS = SPECIAL + UPPER_LETTERS + LOWER_LETTERS + NUMBERS

def generatePassword(length):
    if length < 12:
        length = 12
    password = [
        random.choice(SPECIAL),
        random.choice(UPPER_LETTERS),
        random.choice(LOWER_LETTERS),
        random.choice(NUMBERS)
    ]

    while len(password) < length:
        password.append(random.choice(CHARACTERS))

    random.shuffle(password)
    password = ''.join(password)
    print(password)
    return password
    
assert len(generatePassword(8)) == 12
pw = generatePassword(14)
assert len(pw) == 14
hasLowercase = False
hasUppercase = False
hasNumber = False
hasSpecial = False
for character in pw:
    if character in LOWER_LETTERS:
        hasLowercase = True
    if character in UPPER_LETTERS:
        hasUppercase = True
    if character in NUMBERS:
        hasNumber = True
    if character in SPECIAL:
        hasSpecial = True
assert hasLowercase and hasUppercase and hasNumber and hasSpecial