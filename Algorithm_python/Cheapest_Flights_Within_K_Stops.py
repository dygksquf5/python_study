# K 경유지 내 가장 저렴한 항공권
# 다익스트라로 풀기 좋은 문제

import collections
import heapq
# 시작점에서 도착점까지의 가장 저렴한 가격을 계산하되, K개의 경유지 이내에 도착하는 가격을 리턴하라. 경로가 없으면 -1 리턴

n = 3
edges = [[0, 1, 100],[1, 2, 100],[0, 2, 500]]
src = 0
dst = 2
K = 0

# explain : 시작점 src 노드 0 에서 도착점 dst 2 노드까지 최저가는 0 -> 1-> 2 경로인 200이지만
# 여기서는 입력값이 K =0 으로 경유지가 하나도 없어야 하므로, 이 조건을 만족시키는 0 -> 2 인 500이다.


def findCheapestPrice(n, flights, src, dst, K):
    graph = collections.defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))

    # 큐 변수 [(가격, 정점, 남은 가능 경유지 수 )]
    Q = [(0, src, K)] # K 의 최대 경유횟수 추가해놓고 한번경유 될 때 마다 -1 해주자

    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k >= 0:
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(Q, (alt, v, k-1))
    return -1


print(findCheapestPrice(n, edges, src, dst, K))



