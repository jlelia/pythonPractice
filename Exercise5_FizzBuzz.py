# Exercise 5: Fizz Buzz
## My first solution
def fizzBuzz(upTo):
    for n in range(1, upTo+1):
        if n % 3 != 0 and n % 5 != 0:
            print(n, end=' ')
        if n % 3 == 0 and n % 5 != 0:
            print('Fizz', end=' ')
        if n % 5 == 0 and n % 3 != 0:
            print('Buzz', end=' ')
        if n % 3 == 0 and n % 5 == 0:
            print('FizzBuzz', end=' ')

fizzBuzz(35)

## My second solution after reading 'special cases and gotchas'
def fizzBuzz2(upTo):
    for n in range(1,upTo+1):
        if n % 15 == 0:
            print('FizzBuzz', end=' ')
        elif n % 3 == 0:
            print('Fizz', end=' ')
        elif n % 5 == 0:
            print('Buzz', end=' ')
        else:
            print(n, end=' ')

fizzBuzz2(35)
# This ended up being the book solution