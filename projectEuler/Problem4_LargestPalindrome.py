# Project Euler 4: Largest palindrome product of two 3-digit numbers

def isPalindrome(x, y):
    ijList = []
    palindromeList = []
    for i in range(x, y):
        for j in range(i,y):
            ijList.append(i * j)
    for i in ijList:
        if str(i) == str(i)[::-1]:
            palindromeList.append(i)
    palindromeList = sorted(palindromeList)
    return palindromeList[-1]

print(isPalindrome(100, 1000))