from collections import deque




# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input("입력하시오 : ").split())

graph = []
# 2차원 리스트 입력받자 ! 문제풀이를 위해
for i in range(n):
    graph.append(list(map(int, input("입력하시오 : "))))
print(graph)


def dfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # 상하좌우 다 경우 보기!
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # 주어진 문제가 가장 최 하단까지의 거리를 나타내는거고, 최단거리를 나타낼 때, 한칸당 1이 플러스가 되는데
    # 그걸 리스트에 넣어놨고! 마지막 제일 끝 인덱스에 해당하는 애를 불러오기!
    # 근데 인덱스로 되어있으니까 4 *4 인 이차원 리스트는 결국 인덱스 부를 때 -1 해서 [3][3] 으로 줘야 됨!
    return graph[n - 1][m - 1]


print(dfs(0, 0))