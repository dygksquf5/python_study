#전역변수를 적용하기!


gun = 10

#전역쓰기


def sumOfgun(soldiers):
    global gun
    gun = gun - soldiers
    print("현재 남은 총 갯수 : {0}".format(gun))

#지역쓰기! 대신 return으로 값 지역밖으로 던져주기!


def sumOfgun_2(gun, soldiers):
    gun = gun-soldiers
    print("현재 남은 총 갯수 : {0}".format(gun))
    return gun


print("현재 총의 갯수: {0}".format(gun))
# sumOfgun(3)
gun = sumOfgun_2(gun, 3)

print("이후 총의 갯수: {0}".format(gun))