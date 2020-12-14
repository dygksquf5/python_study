
# 내가푼거! 이거 다시 한줄로 바꿔보기!

def solution(array, commands):
    answer = []
    tem = []

    for i in commands:
        tem = i
        a = sorted(array[tem[0] - 1:tem[1]])
        answer.append(a[tem[2] - 1])

    return answer


# 람다식으로 한번에 풀어보기!

def solution(array, commands):
    return list(map(lambda x: sorted(array[x[0]-1: x[1]])[x[2]-1], commands))


# 입력값 〉	[1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# 기댓값 〉	[5, 6, 3]

