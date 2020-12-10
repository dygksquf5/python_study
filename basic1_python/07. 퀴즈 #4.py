# from random import *
# atd = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# # print (atd)
# a = shuffle(atd)
# a = sample (atd, 1)
# print (a)

# # b = shuffle(atd)
# # b = sample (atd, 3)
# # print(b)


# print("-- 당첨자 발표 --")
# print(f"치킨 당첨자 : {a}"")
# # print(f"커피 당첨자 : {b}"")
# # print("-- 축하합니다 --" )

from random import *

users = range(1,21)
# print(type(users))
users = list(users)
# print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) #4명중 한명은 치킨 세명은 커피 주기 


print("-- 당첨자 발표 --")
print(f"치킨 당첨자 : {winners[0]}")
print(f"커피 당첨자 : {winners[1:]}")
print("-- 축하합니다 --" )