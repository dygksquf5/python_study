import random

number = random.sample(range(100), 10)


def merge(left, right):
    merged = []
    left_point, right_point = 0, 0  # 인덱스 첫번째부터 시작하기위해

    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
        else:
            merged.append(left[left_point])
            left_point += 1

    # left 만 남아있을 때
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1

    # left 만 남아있을 때
    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1

    return merged


def split(data):
    if len(data) <= 1:
        return data
    m = int(len(data) / 2)

    left = split(data[:m])
    right = split(data[m:])

    return merge(left, right)




print(split(number))