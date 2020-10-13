# 택시기사가 하루에 50명의 승객만 태운다고 가정했을 때, 총 몇명의 승객을 태울 수 있을까요 ?

# 조건1) 승객별 소요 시간은 5~50분 사이의 난수로 지정
# 조건2) 5~15분 사이의 소요시간만 필요로 하는 승객만 손님으로 받을 예정! (그 외에는 승객을 받지않음)


from random import *

count = 0 #총 탑승객 수
for i in range(1,51):
    time = randrange(5,51)
    if 5 <= time <= 15:
        print("[0], {0} 번째손님, '소요시간  :' {1} 분".format(i, time))
        count += 1
    else:
        print("[ ], {0} 번째손님, '소요시간  :' {1} 분".format(i, time))

print("총 탑승 승객 수 : {0}".format(count))
