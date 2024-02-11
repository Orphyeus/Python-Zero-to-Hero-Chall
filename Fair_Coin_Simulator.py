from random import randrange

for test in [100, 1000, 10000, 100000, 1000000, 10000000]:
    heads, tails = 0, 0  # Initialize heads and tails count
    for _ in range(test):
        if randrange(2) == 0:
            heads += 1
        else:
            tails += 1
    ratio = heads / tails if tails else 1  # Avoid division by zero
    difference = ratio - 1

    print(f"Test: {test}")
    print(f"heads = {heads}, tails = {tails}")
    print(f"The ratio of #heads/#tails is {ratio:.4f}")
    print(f"Difference: {difference:.4f}\n")
