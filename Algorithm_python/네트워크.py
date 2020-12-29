
# 나는 그냥 이렇게 꼼수아닌 꼼수를 부리려 했지만 ㅎㅎ ...

# def solution(n, computers):
#     answer = 0
#     sums = list(map(sum, computers))
#     if n in sums:
#         return 1
#
#     for i in sums:
#         if i == 1:
#             answer += 1
#     return answer + 1



# 이렇게 정석으로 ..풀어보자 .... dfs 풀이 ... ㅠㅠ
def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            # for i in range(len(computers)-1, -1, -1):
            for i in range(0, len(computers)):
                if computers[j][i] ==1 and visited[i] == 0:
                    stack.append(i)
    i=0
    while 0 in visited:
        if visited[i] ==0:
            dfs(computers, visited, i)
            answer +=1
        i+=1
    return answer