# Exercise 4: Area & Volume
def area(x, y):
    if x < 0 or y < 0:
        print("Please do not use negative numbers.")
        return
    return x * y

def perimeter(x, y):
    if x < 0 or y < 0:
        print("Please do not use negative numbers.")
        return
    return x * 2 + y * 2

def volume(x, y, z):
    if x < 0 or y < 0:
        print("Please do not use negative numbers.")
        return
    return x * y * z

def surfaceArea(x, y, z):
    if x < 0 or y < 0:
        print("Please do not use negative numbers.")
        return
    return x * y * 2 + x * z * 2 + y * z * 2

assert area(10, 10) == 100
assert area(0, 9999) == 0
assert area(5, 8) == 40
assert perimeter(10, 10) == 40
assert perimeter(0, 9999) == 19998
assert perimeter(5, 8) == 26
assert volume(10, 10, 10) == 1000
assert volume(9999, 0, 9999) == 0
assert volume(5, 8, 10) == 400
assert surfaceArea(10, 10, 10) == 600
assert surfaceArea(9999, 0, 9999) == 199960002
assert surfaceArea(5, 8, 10) == 340
print(area(10, -10))