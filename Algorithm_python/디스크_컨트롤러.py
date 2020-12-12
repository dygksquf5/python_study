import heapq
from functools import reduce
from collections import deque

# 이건 내풀이 ... 한문제밖에 못맞춤 ㅠㅠ

# def solution(jobs):
#     time_sum = 0
#     average = []
#
#     while jobs:
#         jobs.sort(key=lambda x: x[1])
#         # hq.heapify(jobs)
#         tem = hq.heappop(jobs)
#
#         # 시간 각각 걸리는 합 먼저 구해보자!
#         time_sum += tem[1]
#         # 각 하드디스크마다 걸리는 시간 계산해서 리스트 넣기
#         average.append(time_sum - tem[0])
#
#     # 평균 계산해서 내보내기
#     answer = reduce(lambda x, y: x + y, average)
#     return answer // len(average)


def solution(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    q = []

    heapq.heappush(q, tasks.popleft())
    current_time, total_response_time = 0, 0
    while len(q) > 0:
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr

        while len(tasks) > 0 and tasks[0][1] <= current_time:
            heapq.heappush(q, tasks.popleft())
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.popleft())

    return total_response_time // len(jobs)



print(solution([[0, 3], [1, 9], [2, 6]]))