import random


def qsort(data):
    if len(data) <= 1:
        return data

    left, right = list(), list()
    pivot = data[0]
    # 이부분 좀더 간결하게 리스트 컴프리핸션으로 바꿔보기!
    # for i in range(1, len(data)):
    #     if pivot > data[i]:
    #         left.append(data[i])
    #     else:
    #         right.append(data[i])

    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot < item]

    return qsort(left) + [pivot] + qsort(right)


number = random.sample(range(100), 10)
print(qsort(number))

