# 문제가 어렵 ㅠ// 순환그래프를 dfs 로 순환 가능인지 아닌지 알아보는건뎅 , 이해가 안가니 추후 다시 공부 ..



import collections


def solution(prerequisites):
    graph = collections.defaultdict(list)

    for x, y in prerequisites:
        graph[x].append(y)

    traced = set()

    def dfs(i):
        if i in traced:
            return False

        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False

        traced.remove(i)

        return True

    for x in list(graph):
        if not dfs(x):
            return False

    return True


print(solution([[1,0], [0,1]]))