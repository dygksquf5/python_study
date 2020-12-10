from typing import List


def array_pair_sum(nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()

    for i in nums:
        pair.append(i)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum


a = [1, 4, 3, 2]
# print(array_pair_sum(a))


def array_pair_sum_2(nums : List[int]) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n

    return sum


def array_pair_sum_3(nums):
    # sum 이랑 sorted 쓰고 슬라이싱 써서 한줄로 표현 !
    return sum(sorted(nums)[::2])


print(array_pair_sum_2(a))
print(array_pair_sum_3(a))
