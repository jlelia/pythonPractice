# Project Euler 3: Largest Prime Factor
import math

def factor(number):
    factors1 = []
    factors2 = []
    for n in range (1, int(math.sqrt(number)+1)):
        if number % n == 0:
            factors1.append(n)

    for factor in factors1:
        factors2.append(number // factor)
    factors = factors1 + factors2
    return sorted(factors)

def isPrime(number):
    for n in range (2, int(math.sqrt(number)+1)):
        if number % n == 0:
            return False
    return True

def primeFactor(number):
    primeFactors = []
    for n in factor(number):
        if isPrime(n):
            primeFactors.append(n)
    return primeFactors[-1]

print(primeFactor(600851475143))
