# Exercise 26: Handshake

def factorial(number):
    result = 1
    for i in range(1, number+1):
        result *= i
    return result


def printHandshakes(people):
    i = 1
    j = 0
    while j < len(people):
        while i < len(people):
            print(f'{people[j]} shakes hands with {people[i]}')
            i += 1
        j += 1
        i = j + 1
    return factorial(len(people)) / len(people)

# gonna try a different approach and come back to the above if needed

def printHandshakes2(people):
    handshakes = 0
    for i in range(0, len(people)):
        for j in range(i, len(people)-1):
            print(f"{people[i]} shakes hands with {people[j+1]}")
            handshakes += 1
    return handshakes

assert printHandshakes2(['Alice', 'Bob']) == 1
assert printHandshakes2(['Alice', 'Bob', 'Carol']) == 3
assert printHandshakes2(['Alice', 'Bob', 'Carol', 'David']) == 6

# wow okay sort of amazing the above works. Mine is different from the example, which is simpler:

def printHandshakes3(people):
    handshakes = 0
    for i in range(0, len(people)-1):
        for j in range(i+1, len(people)):
            print(f"{people[i]} shakes hands with {people[j]}")
            handshakes += 1
    return handshakes

assert printHandshakes3(['Alice', 'Bob']) == 1
assert printHandshakes3(['Alice', 'Bob', 'Carol']) == 3
assert printHandshakes3(['Alice', 'Bob', 'Carol', 'David']) == 6