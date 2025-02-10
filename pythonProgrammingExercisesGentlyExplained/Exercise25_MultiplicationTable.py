# Exercise 25: Multiplication Table

def multiTable():
    factors = [1,2,3,4,5,6,7,8,9,10]
    print('  |  1  2  3  4  5  6  7  8  9 10')
    print('--+-------------------------------')
    for i in factors:
        print(f'{i}| '.rjust(4), end="")
        for j in factors:
            print(str(i*j).rjust(2), end=" ")
        print('\n')

multiTable()