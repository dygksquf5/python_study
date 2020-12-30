

# 나는 ㅠㅠ 전혀 못품 ㅠㅠㅠㅠ
# def solution(begin, target, words):
#     answer = 0
#     # visited = [[v, 0] for i, v in enumerate(words)]
#     visited = [0 for _ in range(len(words))]
#
#     if target not in words:
#         return 0
#
#     stack = [begin]
#
#     for i in range(len(words)):
#         j = stack.pop()
#         stack.append(words[i])
#         idx = 0
#         if visited[i] == 0:
#             visited[i] = 1
#             for v in range(len(j)):
#                 if j[v] != words[i][v]:
#                     idx += 1
#             if idx == 1:
#                 answer += 1
#
#     return answer

# 다른사람 코드 참고해서 품 !
def bfs(begin, target, words):
    q = [begin]
    visited = [0] * len(words)
    index = words.index(target)

    while q:
        text = q.pop(0)
        if text == target:
            return visited[index]

        for i in range(1, len(words)):
            number = 0
            if visited[i] == 0:
                for a, b in zip(text, words[i]):
                    if a == b:
                        number += 1
                    if number == len(text) - 1:
                        visited[i] = visited[words.index(text)] + 1
                        q.append(words[i])


def solution(begin, target, words):

    if target not in words:
        return 0
    else:
        words.insert(0, begin)
        return bfs(begin, target, words)