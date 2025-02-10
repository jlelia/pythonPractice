# Exercise 8 Read Write File

def writeToFile(file, text):
    with open(file, mode='w') as fileObj:
        fileObj.write(str(text))

def appendToFile(file, text):
    with open(file, mode='a') as fileObj:
        fileObj.write(str(text))

def readFromFile(file):
    with open(file, mode='r') as fileObj:
        return fileObj.read()

writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'