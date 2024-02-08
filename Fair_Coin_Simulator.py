from random import randrange

for test in [100,1000,10000,100000, 1000000, 10000000]:
    heads = tails = 0
    for i in range (experiment) :
        if randrange (2) == 0: heads = heads + 1
        else: tails = tails + 1
    print("Test:", test)
    print("heads =", heads," tails = ",tails)
    print("the ratio of #heads/#tails is", (round (heads/tails,4)))
    print ("Difference", (round(heads/tails,4)) - 1)
    print() 
