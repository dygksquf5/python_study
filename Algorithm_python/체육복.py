# 전체 학생수는 1 ~ 30
# 만약 여벌있는애가 도난도 당하면 빌려줄 수 없음

import collections

def solution(n, lost, reserve):
    for i in reserve:
        if i in lost:
            lost.remove(i)
            continue
        if i + 1 in lost:
            lost.remove(i+1)
        elif i - 1 in lost:
            lost.remove(i-1)
    return n - len(lost)


 # 5번과 11번이 안된다.. 뭐때문일까
 