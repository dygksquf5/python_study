# 일단 BFS 는 재귀가 불가능하다! 큐를 이용해서 코드를 짜보자 !

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


def iterative_bfs(start_v):
    discoverd = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discoverd:
                discoverd.append(w)
                queue.append(w)
