# Project Euler 2: Sum of even Fibonacci

def sumOfEvenFibonacci(maxNumber):
    a = 0
    b = 1
    fibonacciSequence = [a, b]

    while b < maxNumber:
        c = a + b
        fibonacciSequence.append(c)
        a = b
        b = c

    fibonacciSequenceEven = [n for n in fibonacciSequence if n % 2 == 0]
    return sum(fibonacciSequenceEven)

print(sumOfEvenFibonacci(4e6))