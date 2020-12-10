from bisect import bisect_right, bisect_left

# 오름차순으로 정렬 되어 있는 리스트 있을 때 ! 해당 숫자가 몇개 있는지 알아내기!
array = [1, 1, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 6, 7, 7, 8]


def get_nums(arrays, number):
    right_index = bisect_right(arrays, number)
    left_index = bisect_left(arrays, number)
    return right_index - left_index


print(get_nums(array, 8))