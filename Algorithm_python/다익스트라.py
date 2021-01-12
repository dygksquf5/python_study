import heapq


def dijkstra(graph, start ):
    dis = {node: int(1e9) for node in graph}

    dis[start] = 0

    queue = []
    heapq.heappush(queue ,[dis[start], start])

    while queue:
        current_dis, current_node = heapq.heappop(queue)

        if dis[current_node] < current_dis:
            continue

        for adj, weight in graph[current_node].items():
            distance = current_dis + weight

            if distance < dis[adj]:
                dis[adj] = distance
                heapq.heappush(queue, [distance, adj])
    return dis


data = {
    'A' : {'B': 8, 'C': 1, 'D': 2},
    'B' : {},
    'C' : {'B': 5, 'D': 2},
    'D' : {'E': 3, 'F': 5},
    'E' : {'F': 1},
    'F' : {'A': 5}
}

print(dijkstra(data, 'A'))