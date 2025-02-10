# Exercise 23: 99 Bottles

def bottlesOfBeer():
    bottles = 99
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall,")
        print(f"{bottles} bottles of beer,")
        print("Take one down,")
        print("Pass it around,")
        bottles -= 1
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall!")
        if bottles == 1:
            print(f"{bottles} bottle of beer on the wall!")
    if bottles == 1:
        print(f"{bottles} bottle of beer on the wall,")
        print(f"{bottles} bottle of beer,")
        print("Take it down,")
        print("Pass it around,")
        bottles -= 1
    if bottles == 0:
        print("No more bottles of beer on the wall!")

bottlesOfBeer()