# Project Euler 1: Multiples of 3 or 5

def sumOfMultiples(lessThan):
    multiples = []
    for n in range(1, lessThan):
        if n % 3 == 0 and n % 5 != 0:
            multiples.append(n)
        if n % 5 == 0 and n % 3 != 0:
            multiples.append(n)
        if n % 15 == 0:
            multiples.append(n)
    return sum(multiples)

print(sumOfMultiples(1000))

# Lovely solution I found on the forums:

print(sum(i for i in range(1,1000) if i%3 == 0 or i%5 == 0))