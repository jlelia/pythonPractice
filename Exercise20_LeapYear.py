# Exercise 20: Leap Year

def isLeapYear(year):
    if year % 100 == 0 and not year % 400 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


assert isLeapYear(1999) == False
assert isLeapYear(2000) == True
assert isLeapYear(2001) == False
assert isLeapYear(2004) == True
assert isLeapYear(2100) == False
assert isLeapYear(2400) == True