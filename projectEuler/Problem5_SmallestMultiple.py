# Problem 5: Smallest Multiple

# unfinished, will return

def smallestMultiple(max, maxFactor):
    multiples = []
    for i in range(1, max+1, maxFactor):
        if all(i % j == 0 for j in range(11, maxFactor)):
            multiples.append(i)
    return multiples
            
print(smallestMultiple(100_000, 20))
        
