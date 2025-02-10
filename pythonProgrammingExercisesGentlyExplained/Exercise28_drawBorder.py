# Exercise 28: Border Drawing

def drawBorder(x, y):
    if x < 2 or y < 2:
        return
    print('+' + '-' * (x - 2) + '+')
    for i in range(y - 2):
        print('|' + ' ' * (x - 2) + '|')
    print('+' + '-' * (x - 2) + '+')

drawBorder(16,4)