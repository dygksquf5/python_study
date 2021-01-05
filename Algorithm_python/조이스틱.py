
# 이런식으로 아스키로드로 하려고했는데, 문제를 ㅇ살짝 처음에 잘못 이해해서,... 다시 새롭게 접근하기 !
# def solution(name):
#     print(int(ord("A")) - int(ord("J")))
#     answer = -1
#
#     nums = [0] * len(name)
#
#     for i, n in enumerate(name):
#         if n == "A":
#             nums[i] = 1
#         elif n != "A":
#             nums[i] = abs(int(ord("A")) - int(ord(n)))
#
#     print(nums)


# import string
#
#
# def solution(name):
#     alpa = [i for i in string.ascii_uppercase]
#
#     check = [min(alpa.index(i), alpa[::-1].index(i) + 1) for i in name]
#
#     if 'A' not in name:
#         answer = -1
#         for i in name:
#             answer += 1
#             # 일반 인덱스, 뒤집힌 인덱스  = 더 A 로부터 거리가 짧은걸 반환
#             minimum = min(alpa.index(i), alpa[::-1].index(i) + 1)
#             answer += minimum
#         return answer
#     if 'A' in name:
#         pass

# 이렇게 조금 검색해서 해결 완료. 쉽지않았따 ㅠ

import string

def solution(name):
    alpa = [i for i in string.ascii_uppercase]

    check = [min(alpa.index(i), alpa[::-1].index(i) + 1) for i in name]
    print(check)
    if 'A' not in name:
        return (len(name) - 1) + sum(check)

    if 'A' in name:
        answer = 0
        locat = 0

        while True:

            answer += check[locat]

            check[locat] = 0

            if sum(check) == 0: break

            left = 1
            right = 1

            while check[locat + right] == 0:
                right += 1

            while check[locat - left] == 0:
                left += 1

            if left >= right:
                locat += right
                answer += right

            else:
                locat -= left
                answer += left

    return answer

