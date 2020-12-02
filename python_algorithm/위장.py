import collections
from functools import reduce

list = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]


def solution(c):
    cnt = collections.Counter([b for a, b in c])
    return reduce(lambda x, y: x*(y + 1), cnt.values(), 1) - 1


print(solution(list))


