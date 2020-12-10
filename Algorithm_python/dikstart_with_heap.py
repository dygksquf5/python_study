import sys
import heapq

input = sys.stdin.readline

INF = int(1e9) # 무한으로 설정해주기! 10억


# 노드의 개수와 간선의 개수 입력받기
n, m = map(int, input().split())

# 시작노드 입력받기
start = int(input())

# 각 노드에 연결되어 있는 노드 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]

# 방문여부 체크 테이블
visited = [False] * (n + 1)

# 최단거리에 있는 테이블 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기!
for _ in range(m):
    a, b, c = map(int, input().split())
    # a 노드에서 b 노드로 가는 비용이 c 라는 뜻
    graph[a].append((b, c))


def dijkstart(start):
    q = []
    heapq.heappush(q, (0, start))
    # 시작노드로 가기위한 최단경로는 0으로 초기화
    distance[start] = 0
    while q:
        # 가장 최단거리 힙에서 꺼내기!
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된적 있는 노드라면 무시! 즉 1e9 보다 클 순 없으니까..!
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들 확인
        for i in graph[now]:
            cost = dist + i[1] # [0] 은 노드 번호인듯!
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 !
            # 처음엔 당연히 10억이 디폴트니까 distance에 cost 가 들어가고, 그 이후에는 더 짧은, 즉 cost가 더 작은경우 cost reset
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                # heap에 새로운 짧은 거리와 노드번호 올려주기
                heapq.heappush(q, (cost, i[0]))


dijkstart(1)

for i in range(1, n+1):
    if distance[i] == INF:
        print(" 갈 수 없는 경로! ")
    else:
        print(distance[i])



