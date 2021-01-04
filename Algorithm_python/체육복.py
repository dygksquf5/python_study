# 전체 학생수는 1 ~ 30
# 만약 여벌있는애가 도난도 당하면 빌려줄 수 없음

import collections


# def solution(n, lost, reserve):
#     for r in reserve[:]:
#         if r in lost:
#             lost.remove(r)
#             reserve.remove(r)
#
#     for i in reserve[:]:
#         if i + 1 in lost:
#             lost.remove(i + 1)
#             continue
#         if i - 1 in lost:
#             lost.remove(i - 1)
#             continue
#     return n - len(lost)


# 5번은 중복되는 경우를 따로 다시 for 문으로 빼줘서 해결

# 11번이 안된다.. 뭐때문일까


def solution(n, lost, reserve):
    for r in reserve[:]:
        if r in lost:
            lost.remove(r)
            reserve.remove(r)

    for i in reserve[:]:
        if i - 1 in lost:
            lost.remove(i - 1)
            continue
        if i + 1 in lost:
            lost.remove(i + 1)
            continue
    return n - len(lost)

# 이걸로 해결함!!!
# 빼기를 먼저 해서 왼쪽에 있는 애 먼저 해결하고, -1 이 없는경우에 +1 을 한 오른쪽 있는 애를 해결하는 식으로 해야 테스트 케이스 해결 가능 