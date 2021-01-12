# ex) a, b, c (빨 파 초) = 4, 4, 0
# d, e, f ( 만들고 싶은 갯수) = 2, 1, 2
# 구슬 2개로 1개를 만들 수 있음
# 4 4 0 으로 2 1 2 만들 수 있으니까 true return ( 2 1 2 이상으로 만들 수 있으면 가능 )
# 만약 2 2 1 로 1 1 2 만들라고 하면 불가능함으로 false
# 이거 해결하는 솔루션 함수 작성하기
# a~f 는 1,000,000 보다 작거나 같은 자연수



# 이런식으로 해결을 당장은 할 순 있찌만 .... 1000000 이 최대 숫자기때문에 이렇게 해결하면 무조건 런타임에러 .. 재귀가 너무많이된다. 뭘로 해결해야되지 그럼 ?
def recursive(original, wish, index):
    for i in range(len(original)):
        if original[i] > wish[i] and original[i] - 2 >= wish[i]:
            original[i] -= 2
            original[i + 1] += 1
            recursive(original, wish, index)
    for o, w in zip(original, wish):
        if o - w >= 0:
            index += 1
            if index == 3:
                return True
    return False


def solution(a, b, c, d, e, f):
    original = [a, b, c]
    wish = [d, e, f]
    ori_index = 0
    wis_index = 0
    index = 0

    # 이걸로 일단 wish 이상을 이미 지니고 있는 경우는 True 먼저 뽑아내주기
    while True:
        if original[ori_index] >= wish[wis_index]:
            ori_index += 1
            wis_index += 1
            if ori_index == len(original):
                return True
        else:
            ori_index, wis_index = 0, 0
            break

    return recursive(original, wish, index)


print(solution(4, 4, 0, 2, 1, 2)) # True
print(solution(3, 3, 3, 2, 2, 2)) # True
print(solution(2, 2, 1, 1, 2, 2)) # False



