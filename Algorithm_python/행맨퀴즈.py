import random


answer = ["apple", "banana", "orange"]

Q = [*answer[random.randint(0,2)]]
for_index = Q[:] # 여기 인덱스 사용하자 그냥 .. 귀찮
index = 0

print(*Q)

str_basic = ["_"] * len(Q)


while True:
    answer_by_player = input("값을 입력하세요 : ")
    if answer_by_player in Q:
        print("Correct")
        str_basic[Q.index(answer_by_player)] = answer_by_player
        Q[Q.index(answer_by_player)] = "0"
        index += 1
        print(*str_basic)
    else:
        print("Wrong")
        print(*str_basic)

    if index == len(Q):
        print(" Success :) ")
        break

