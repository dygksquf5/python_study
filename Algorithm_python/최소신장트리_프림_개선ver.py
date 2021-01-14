from heapdict import heapdict


graph = {
    'A': {'B': 7, 'D': 5},
    'B': {'A': 7, 'D': 9, 'C': 8, 'E': 7},
    'C': {'B': 8, 'E': 5},
    'D': {'A': 5, 'B': 9, 'E': 7, 'F': 6},
    'E': {'B': 7, 'C': 5, 'D': 7, 'F': 8, 'G': 9},
    'F': {'D': 6, 'E': 8, 'G': 11},
    'G': {'E': 9, 'F': 11}
}


def prim(graph, start):
    mst, keys, pi, total_weight = list(), heapdict(), dict(), 0
    for node in graph.keys():
        keys[node] = 1e9
        pi[node] = None
    keys[start], pi[start] = 0, start # 초기화

    while keys:
        current_node, currnet_key = keys.popitem()
        mst.append([pi[current_node], current_node, currnet_key])
        total_weight += currnet_key
        print(mst,'\n', pi,'\n', total_weight,'\n', dict(keys))
        for adjacent, weight in graph[current_node].items():
            if adjacent in keys and weight < keys[adjacent]:
                keys[adjacent] = weight
                pi[adjacent] = current_node

    return mst, total_weight


print(prim(graph,'A'))
