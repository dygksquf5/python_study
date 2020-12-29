from itertools import product
import collections


# 완전탐색 & 데카르트의 곱으로 푼문제
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)


print(solution([1, 1, 1, 1, 1], 3))



#  bfs 솔루션
def solution_bfs(numbers, target):
    answer = 0
    stack = collections.deque([(0, 0)])
    while stack:
        current_sum, num_idx = stack.popleft()

        if num_idx == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            number = numbers[num_idx]
            stack.append((current_sum + number, num_idx + 1))
            stack.append((current_sum - number, num_idx + 1))

    return answer


print(solution_bfs([1, 1, 1, 1, 1], 3))



# dfs 로 풀어보기 !
answer_dfs = 0


def DFS(idx, numbers, target, value):
    global answer_dfs
    N = len(numbers)
    if idx == N and target == value:
        answer_dfs += 1
        return
    if idx == N:
        return

    DFS(idx + 1, numbers, target, value + numbers[idx]) # 이렇게 재귀로 두개를 넣어놔서 dfs로 딥하게 끝까지 파고들게 만들기 !
    DFS(idx + 1, numbers, target, value - numbers[idx]) # 재귀 두개로 + , - 둘다 재귀 안에서 또 재귀로 돌 리기, 해당 인덱스가 len와 같을 때 까지 


def solution_dfs(numbers, target):
    global answer_dfs
    DFS(0, numbers, target, 0)
    return answer_dfs


print(solution_dfs([1, 1, 1, 1, 1], 3))