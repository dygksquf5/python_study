from typing import List


def numIslands(grid: List[List[str]]) -> int:
    def dfs(i, j):
        # 더이상 땅이 아닌경우 종료!
        if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                grid[i][j] != "1":
            return

        grid[i][j] = 0

        # 동ㅇ서남북 탐색!! 탐색하고 1 이었던 곳은  0 으로 바꿔주면서 1을 찾아 하나씩 세어보기!!
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                # 모든 육지 탐색 후 카운트 1 증가
                count += 1
    return count


print(numIslands([
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
]))
