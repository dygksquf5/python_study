import heapq
import time

# 이건 최소 힙정렬 만약 최대 하려면
def heap_sort(array):
    h = []
    result = []
    for value in array:
        heapq.heappush(h, value)

    for i in range(len(array)):
        result.append(heapq.heappop(h))

    print(result)

# 이렇게 음수값으로 넣고 빼면 최대 값으로 힙정렬 가능함

def heap_sort(array):
    h = []
    result = []
    for value in array:
        heapq.heappush(h, -value)

    for i in range(len(array)):
        result.append(- heapq.heappop(h))

    print(result)



list = [1,3,7,4,2,4,1,6,8,65,0,9,8,7,43]

# a = time.time()
# heap_sort(list)
# print(a - time.time())

# b = time.time()
# print(list.sort())
# print(b - time.time())
