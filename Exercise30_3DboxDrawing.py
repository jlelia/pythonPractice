# Exercise 30: 3D Box Drawing

def drawBox(size):
    print('+' + '--'*size + '+').rjust()
    print('/' + '  '*size + '/' + ' '*(size-1) + '|').rjust()
