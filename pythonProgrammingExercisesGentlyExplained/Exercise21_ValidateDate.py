# Exercise 21: Validate Date
from Exercise20_LeapYear import isLeapYear

def isValidDate(year, month, day):
    thirtyDayMonths = [4, 6, 9, 11]
    thirtyoneDayMonths = [1, 3, 5, 7, 8, 10, 12]

    if month in thirtyDayMonths and 30 >= day >= 1:
        return True

    if month in thirtyoneDayMonths and 31 >= day >= 1:
        return True

    if month == 2 and isLeapYear(year) == False and 28 >= day >= 1:
        return True

    if month == 2 and isLeapYear(year) == True and 29 >= day >= 1:
        return True

    return False

assert isValidDate(1999, 12, 31) == True
assert isValidDate(2000, 2, 29) == True
assert isValidDate(2001, 2, 29) == False
assert isValidDate(2029, 13, 1) == False
assert isValidDate(1000000, 1, 1) == True
assert isValidDate(2015, 4, 31) == False
assert isValidDate(1970, 5, 99) == False
assert isValidDate(1981, 0, 3) == False
assert isValidDate(1666, 4, 0) == False

import datetime
d = datetime.date(1970, 1, 1)
oneDay = datetime.timedelta(days=1)
for i in range(1000000):
    assert isValidDate(d.year, d.month, d.day) == True
    d += oneDay

# it seems like the book was looking for a fail-fast method. I will try to write a new one accordingly:

def isValidDate2(year, month, day):

    thirtyDayMonths = [4,6,9,11]
    thirtyoneDayMonths = [1,3,5,7,8,10,12]
    february = 2
    validMonths = thirtyDayMonths + thirtyoneDayMonths + [february]

    if month not in validMonths:
        return False
    
    if month == february and isLeapYear(year) and not 1 <= day <= 29:
        return False
    
    if month == february and not isLeapYear(year) and not 1 <= day <= 28:
        return False
    
    if month in thirtyDayMonths and not 1 <= day <= 30:
        return False
    
    if month in thirtyoneDayMonths and not 1 <= day <= 31:
        return False
    
    return True

assert isValidDate2(1999, 12, 31) == True
assert isValidDate2(2000, 2, 29) == True
assert isValidDate2(2001, 2, 29) == False
assert isValidDate2(2029, 13, 1) == False
assert isValidDate2(1000000, 1, 1) == True
assert isValidDate2(2015, 4, 31) == False
assert isValidDate2(1970, 5, 99) == False
assert isValidDate2(1981, 0, 3) == False
assert isValidDate2(1666, 4, 0) == False

import datetime
d = datetime.date(1970, 1, 1)
oneDay = datetime.timedelta(days=1)
for i in range(1000000):
    assert isValidDate2(d.year, d.month, d.day) == True
    d += oneDay