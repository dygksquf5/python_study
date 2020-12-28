import itertools


def solution(arr, K):
    tmp = []
    answer = 0
    for i in list(map(list, itertools.combinations(arr, K))):
        tmp.append([max(list(map(int, set(i)))), min(list(map(int, set(i))))])

    for j in list(set(map(tuple, tmp))):
        a = j[0] - j[1]
        if answer == 0:
            answer = a
        answer = min(answer, a)
    return answer


#         a = int(sorted(i)[-1]) - int(sorted(i)[0])

#         if answer == 0:
#             answer = int(a)
#         answer = min(answer,  int(a) )


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [9, 11, 9, 6, 4, 19]
K = 4
ret = solution(arr, K)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")


# 시간초과가 뜨는게 있어서 ㅠㅠ 이렇게 수정을 했는데도 뜬당 ㅠㅠㅠ 아마 멕스 민 이랑 셋 이게 시간 많이 잡아먹는듯 .. 아니면 이터툴 ..? ㅠㅠ