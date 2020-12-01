# 3,4 크기의 2차원 공간
n, m = 3, 4

# 각 칸마다의 금 갯수
array = [1, 3, 3, 2, 2, 1, 4, 1, 0, 6, 4, 7]

# d = [[0] * 4] * n
d = []
index = 0
for _ in range(n):
    d.append(array[index: index + m])
    index += m

for j in range(1, m):
    for i in range(n):
        # 왼쪽 위에서 오는경우
        # i 가 제일 윗칸일 때는 위에서 오는게 없으니..
        if i == 0:
            left_up = 0
        else:
            left_up = d[i - 1][j - 1]
        # 왼쪽 아래에서 오는 경우
        # 만약 i 가 제일 밑바닥일땐, 더 아래에서 올 수 있는것이 없으니 ..
        if i == n - 1:
            left_down = 0
        else:
            left_down = d[i + 1][j - 1]
        # 왼쪽에서 오는 경우
        left = d[i][j - 1]
        d[i][j] = d[i][j] + max(left_up, left_down, left)

result = 0
for i in range(n):
    # 그럼 테이블의 각 제일 마지막 칸에 최대값들이 들어가 있을텐데, 그거 3개를 비교해서 가장 큰 값을 return
    result = max(result, d[i][m - 1])
print(result)
