

#무작위로 1등 당첨자 한명과, 커피당첨자 3명을 뽑는 과정



from random import *

users = range(1,21)
# print(type(users))
users = list(users)
print(type(users))
shuffle(users)

winners = sample(users,4)

print(" 당첨자 발 표 ! ")
print("치킨 당 첨 자 :{0}".format(winners[0]))
print(" 커피당첨자 : {0}".format(winners[1:]))
