import random

n = random.randint(1,30)

while True:
    x = input("guess what")
    g = int(x)
    if g == n:
        print (" YES!!")
        break
    if g < n:
        print ("Small")

    if g > n:
        print ("too big")
        


