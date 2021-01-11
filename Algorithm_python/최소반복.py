# 주어진 수가 커서, 나머지 테스트케이스는 전부 에러ㅓㅓㅓ


def solution(arr):
    answer = 0
    id = [0] * len(set(str(arr)))
    visited = [False] * len(id)

    for i in range(len(arr)):
        if not visited[arr[i] - 1]:
            id[arr[i] - 1] = i
            visited[arr[i] - 1] = True
            continue

        if visited[arr[i] - 1]:
            answer = min(i - id[arr[i] - 1], id[arr[i] - 1])
            id[arr[i] - 1] = max(i - id[arr[i] - 1], id[arr[i] - 1])

    if answer == 0:
        return -1
    else:
        return answer

    #     answer = []

#     id = collections.defaultdict(list)

#     for i in sorted(set(arr)):
#         id[i] = [dup for dup in range(len(arr)) if arr[dup] == i]