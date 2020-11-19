graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


# 재귀 이용한 DFS
def recursive_dfs(v, discoverd=[]):
    discoverd.append(v)
    for w in graph[v]:
        if w not in discoverd:
            recursive_dfs(w, discoverd)
    return discoverd


print(recursive_dfs(1))


# 스택 이용한 DFS

def iterative_dfs(start_v):
    discoverd = []
    stack = [start_v]
    while stack:
        # 스택으로 구현하면 순서는 좀 달라져! 제일 끝에부터 pop 해서 반복하니까! 하지만 사실상 DFS 가 맞음 !
        v = stack.pop()
        if v not in discoverd:
            discoverd.append(v)
            for w in graph[v]:
                stack.append(w)
    return discoverd


print(iterative_dfs(1))