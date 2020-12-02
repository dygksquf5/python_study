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
    

