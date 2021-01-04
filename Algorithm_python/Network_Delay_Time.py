# 네트워크 딜레이 타임 _ 다익스트라


# K부터 출발해 모든 노드가 신호를 받을 수 있는 시간을 계산하기. 불가능할경우 -1 을 리턴하기. 입력값 u,v,w 는 각각 출발지 도착지 소요시간으로. 전체노드 = N

import collections
import heapq


def networkDealyTime(times, N, K):
    graph = collections.defaultdict(list)
    # 그래프 인접 리스트 구성
    for u, v, w, in times:
        graph[u].append((v, w))

    # 큐 변수 [(소요시간, 정점)]
    Q = [(0, K)]
    dist = collections.defaultdict(int)

    # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
    while Q:
        time, node = heapq.heappop(Q)

        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))
    print(dist)
    # 모든 노드의 최단 경로 존재 여부 판별
    if len(dist) == N:
        return max(dist.values())
    return - 1


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
N = 4
K = 2
print(networkDealyTime(times, N, K))
