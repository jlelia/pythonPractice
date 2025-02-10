# Exercise 6: Ordinal Suffix

def ordinalSuffix(n):
    n = str(n)
    if n[-1] == '1' and n[-2:] != '11':
        return n + 'st'
    elif n[-1] == '2' and n[-2:] != '12':
        return n + 'nd'
    elif n[-1] == '3' and n[-2:] != '13':
        return n + 'rd'
    else:
        return n + 'th'

assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'

def ordinalSuffixVirgin(n):
    if n % 10 == 1 and n % 100 != 11:
        return str(n) + 'st'
    elif n % 10 == 2 and n % 100 != 12:
        return str(n) + 'nd'
    elif n % 10 == 3 and n % 100 != 13:
        return str(n) + 'rd'
    else:
        return str(n) + 'th'
    
assert ordinalSuffixVirgin(0) == '0th'
assert ordinalSuffixVirgin(1) == '1st'
assert ordinalSuffixVirgin(2) == '2nd'
assert ordinalSuffixVirgin(3) == '3rd'
assert ordinalSuffixVirgin(4) == '4th'
assert ordinalSuffixVirgin(10) == '10th'
assert ordinalSuffixVirgin(11) == '11th'
assert ordinalSuffixVirgin(12) == '12th'
assert ordinalSuffixVirgin(13) == '13th'
assert ordinalSuffixVirgin(14) == '14th'
assert ordinalSuffixVirgin(101) == '101st'