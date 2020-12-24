# 다른사람이 2차방정식으로 푼 문제

import math

def solution(brown, yellow):
    term = math.sqrt((brown+4)**2 /4 - 4 * (brown + yellow)) # math 대신 ** 0.5 도 가능
    w = ((brown + 4) / 2 + term) / 2
    h = ((brown + 4) / 2 - term) / 2
    return [w,h]




# 내가 푼 문제! 이렇게 하면 4,6,7, 번 문제 못품 ㅠㅠ
def solution(b, y):
    sums = b + y
    for i in range(3, sums):
        for j in range(3, i + 1):
            a = i*j
            if ((b // 2) - 3) == y and b > 10:
                return [((b//2)-1), sums//((b//2)-1)]
            if a == sums and i > j or a == sums and i == j:
                return [i, j]