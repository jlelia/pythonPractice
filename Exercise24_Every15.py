# Exercise 24: Every 15 Minutes

def every15():
    hour = ['12', '1', '2', '3', '4', '5',
            '6', '7', '8', '9', '10', '11']
    minute = ['00', '15', '30', '45']
    time = ['am', 'pm']
    for i in range(0, 2):
        for j in range(0, 12):
          for k in range(0, 4):
            print(f"{hour[j]}:{minute[k]}{time[i]}")

every15()