# Exercise 29: Pyramid Drawing

def drawPyramid(height):
    for i in range(height):
        print(('#' + 2 * i * '#').center(height * 2 + 1))

drawPyramid(8)