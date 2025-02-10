# Exercise 27: Rectangle Drawing

def drawRectangle(x, y):
    for i in range(y):
        for j in range(x):
            print('#', end='')
        print('')

drawRectangle(10,4)
drawRectangle(0, 0)

def drawRectangle2(x, y):
    for i in range(y):
        print('#' * x)

drawRectangle2(10, 4)
drawRectangle2(0, 0)