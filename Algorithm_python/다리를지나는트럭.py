import collections


def solution(b_len, weight, tw):
    answer = 0
    q = collections.deque([0] * b_len)
    tw = collections.deque(tw)

    while q:
        answer += 1
        q.popleft()

        if sum(q) + tw[0] <= weight:
            q.append(tw.popleft())
        else:
            q.append(0)

        if len(tw) == 0:
            return answer + b_len


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))