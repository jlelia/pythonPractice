# Exercise 11: Hours Minutes Seconds

# My solution (apparently psychopathic)
def getDaysHoursMinutesSeconds(seconds):
    days = 0
    hours = 0
    minutes = 0
    if seconds < 60:
        return str(seconds) + 's'
    else:
        minutes = seconds // 60
        seconds = seconds % 60

    if minutes < 60 and seconds == 0:
        return str(minutes) + 'm'
    elif minutes < 60 and seconds > 0:
        return str(minutes) + 'm ' + str(seconds) + 's'
    else:
        hours = minutes // 60
        minutes = minutes % 60

    if hours < 24 and minutes == 0 and seconds == 0:
        return str(hours) + 'h'
    elif hours < 24 and minutes == 0 and seconds > 0:
        return str(hours) + 'h ' + str(seconds) + 's'
    elif hours < 24 and minutes > 0 and hours > 0:
        return str(hours) + 'h ' + str(minutes) + 'm ' + str(seconds) + 's'
    else:
        days = hours // 24
        hours = hours % 24
    
    if hours == 0 and minutes == 0 and seconds == 0:
        return str(days) + 'd'
    elif hours == 0 and minutes == 0 and seconds > 0:
        return str(days) + 'd ' + str(seconds) + 's'
    elif hours == 0 and minutes > 0 and seconds > 0:
        return str(days) + 'd ' + str(minutes) + 'm ' + str(seconds) + 's'
    elif hours == 0 and minutes > 0 and seconds == 0:
        return str(days) + 'd ' + str(minutes) + 'm'
    elif hours > 0 and minutes == 0 and seconds == 0:
        return str(days) + 'd ' + str(hours) + 'h '
    elif hours > 0 and minutes > 0 and seconds == 0:
        return str(days) + 'd ' + str(hours) + 'h ' + str(minutes) + 'm' 
    elif hours > 0 and minutes == 0 and seconds > 0:
        return str(days) + 'd ' + str(hours) + 'h ' + str(seconds) + 's' 
    return str(days) + 'd ' + str(hours) + 'h ' + str(minutes) + 'm ' + str(seconds) + 's'

assert getDaysHoursMinutesSeconds(30) == '30s'
assert getDaysHoursMinutesSeconds(60) == '1m'
assert getDaysHoursMinutesSeconds(90) == '1m 30s'
assert getDaysHoursMinutesSeconds(3600) == '1h'
assert getDaysHoursMinutesSeconds(3601) == '1h 1s'
assert getDaysHoursMinutesSeconds(3661) == '1h 1m 1s'
assert getDaysHoursMinutesSeconds(90042) == '1d 1h 42s'
assert getDaysHoursMinutesSeconds(0) == '0s'
print(getDaysHoursMinutesSeconds(1_000))
print(getDaysHoursMinutesSeconds(1_000_000))
print(getDaysHoursMinutesSeconds(1_000_000_000))

def getDaysHoursMinutesSeconds2(seconds):
    result = []
    minutes = 0
    hours = 0
    days = 0

    if seconds == 0:
        return seconds
    
    while seconds >= 86400:
        days += 1
        seconds -= 86400

    while seconds >= 3600:
        hours += 1
        seconds -= 3600

    while seconds >= 60:
        minutes += 1
        seconds -= 60
    
    stringSeconds = str(seconds) + 's'
    stringMinutes = str(minutes) + 'm'
    stringHours = str(hours) + 'h'
    stringDays = str(days) + 'd'

    if days > 0:
        result.append(stringDays)
    if hours > 0:
        result.append(stringHours)
    if minutes > 0:
        result.append(stringMinutes)
    if seconds >= 0:
        result.append(stringSeconds)
    
    return ' '.join(result)

assert getDaysHoursMinutesSeconds2(30) == '30s'
assert getDaysHoursMinutesSeconds2(60) == '1m'
assert getDaysHoursMinutesSeconds2(90) == '1m 30s'
assert getDaysHoursMinutesSeconds2(3600) == '1h'
assert getDaysHoursMinutesSeconds2(3601) == '1h 1s'
assert getDaysHoursMinutesSeconds2(3661) == '1h 1m 1s'
assert getDaysHoursMinutesSeconds2(90042) == '1d 1h 42s'
assert getDaysHoursMinutesSeconds2(0) == '0s'