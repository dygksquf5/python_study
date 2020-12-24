# 예제 #1
# [1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.
#
# 예제 #2
# [0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.
#
# 11과 011은 같은 숫자로 취급합니다.


import itertools as i
import functools
import math


def permu(nums, lens):
    return map(tuple, i.permutations(nums, lens))


def solution(numbers):
    first = [[0]] * len(numbers)
    second = []

    for i in list(map(lambda x: x, [x for x in range(1, len(numbers) + 1)])):
        first[i-1] = list(set(permu(numbers, i)))  # 중복 없애기

    for i in first:
        for j in i:
            second.append(int(functools.reduce(lambda x, y: x + y, j)))  # str 하나로 합치기

    second = [str(i) for i in list(sorted(set(second)))]

    t_f = [False, False] + [True] * (int(second[-1]) - 1)

    index = 0
    for i in range(2, int(second[-1]) + 1):
        if t_f[i] == True and str(i) in second:
            index += 1
        for j in range(2 * i, int(second[-1]) + 1, i):
            t_f[j] = False
    return index

    # if 0 in second:
    #     second.remove(0)
    # if 1 in second:
    #     second.remove(1)

    # t_f = [False, False] + [True] * int(math.sqrt(max(second)))

#     for i in range(2, int(math.sqrt(max(second)) + 1)):
#         for j in second:
#             if i == j:
#                 continue
#             if j % i == 0:
#                 second.remove(j)

#     return len(second)



# 다른사람 풀이 ! set 을 잘 활용한 풀이닷! 참고하기 @!!
# from itertools import permutations
#
#
# def solution(n):
#     a = set()
#     for i in range(len(n)):
#         # 단순 a 를 replace 하는게 아닌, |= 합집합으로 a 에 중복된거 없이 계속 추가할 수 있게 하기. 쩌넹
#         a |= set(map(int, map("".join, permutations(list(n), i + 1))))
#
#     a -= set(range(0, 2))  # a 에 쌓여있는 애들중에 소수는 결국 0과 1 제외해야 되니까, set으로
#     # range 0~1 까지 수의 차집합 구하는 방식으로 제외시켜버리기.
#     print(int(max(a)))
#     for i in range(2, int(max(a) ** 0.5) + 1):
#         a -= set(range(i * 2, max(a) + 1, i))
#     return len(a)



print(solution("17"))
print(solution("011"))