import sys

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

# 방문하지않은 노드중에 최단거리가 제일 짧은 노드번호 반환
def get_smallest_node():
    min_value = INF
    index = 0  #스 가장 최단거리가 짧은 노드 인덱

    for i in range(1, n +1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    # 제일먼저 시작노드를 받은뒤 실행될테니, 시작노드를 0으로 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작노드를 제외한 전체 노드의 n -1 개 반복
    for i in (n - 1):
        # 현재 최단거리가 가장 짧은 노드 꺼내서 방문처리 하기
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드들 확인하기
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)

# 모든노드로 가기위한 최단거리 출력
for i in range(1, n +1):
    # 도달할 수 없을 땐
    if distance[i] == INF:
        print(" 갈수있는 방법이 없습니다. ")
    else:
        print(distance[i])




