import collections


def solution(p, loc):
    answer = 0
    queue = collections.deque([(a, b) for a, b in enumerate(p)])

    while True:
        cur = queue.popleft()
        if any(cur[1] < i[1] for i in queue):
            queue.append(cur)
            print(queue)
        else:
            answer += 1
            if cur[0] == loc:
                return answer



print(solution([2,1,3,4], 2))





