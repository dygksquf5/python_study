from random import *

number = range(0,10)
number = list(number)
shuffle(number)
lottery = sample(number, 7)

print(f"{lottery[0]}조, {lottery[1:]} 번 입니다.")
