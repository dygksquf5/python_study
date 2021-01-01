

# 내가 푼 방식, 테스트케이스 1,2 통과못하고 3,4 통과함
from collections import defaultdict


def dfs(tmp, answer, airport):
    for i in tmp:
        if i == airport and len(tmp[i]) != 0:
            answer.append(tmp[i].pop(0))
            dfs(tmp, answer, answer[-1])

    return answer


def solution(tickets):
    answer = ["ICN"]
    tmp = defaultdict(list)

    for s, e in tickets:
        tmp[s].append(e)
        tmp[s] = sorted(tmp[s])

    return dfs(tmp, answer, answer[-1])



# 이렇게 dfs 를 살짝 수정해서 테스트  통과함!
from collections import defaultdict


def solution(tickets):
    answer = []
    tmp = defaultdict(list)

    for s, e in tickets:
        tmp[s].append(e)
        tmp[s] = sorted(tmp[s])

    def dfs(airport):
        while tmp[airport]:
            dfs(tmp[airport].pop(0))
        answer.append(airport)

    dfs("ICN")
    return (answer[::-1])