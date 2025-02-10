# Exercise 9: Chess Square Color

# first attempt
def getChessSquareColor(x, y):
    while x in range(1, 9) and y in range(1, 9):
        break
    else:
        return ''
    if (x + y) % 2 == 0:
        return 'white'
    return 'black'

assert getChessSquareColor(1, 1) == 'white'
assert getChessSquareColor(2, 1) == 'black'
assert getChessSquareColor(1, 2) == 'black'
assert getChessSquareColor(8, 8) == 'white'
assert getChessSquareColor(0, 8) == ''
assert getChessSquareColor(2, 9) == ''

# second attempt
def getChessSquareColor2(x, y):
    if x in range(1, 9) and y in range(1,9):
        if (x + y) % 2 == 0:
            return 'white'
        return 'black'
    else:
        return ''

assert getChessSquareColor2(1, 1) == 'white'
assert getChessSquareColor2(2, 1) == 'black'
assert getChessSquareColor2(1, 2) == 'black'
assert getChessSquareColor2(8, 8) == 'white'
assert getChessSquareColor2(0, 8) == ''
assert getChessSquareColor2(2, 9) == ''