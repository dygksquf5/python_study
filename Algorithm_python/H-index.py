# 이건 사실 결국 어떤 특별한 규칙을 못찾아서 못풀었는데 ..
# 사람들 푼거보면 어떻게 이런생각을 했는지 놀라울 따름이다 ..


def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

# 이건 그냥 ..인덱스 값이랑 주어진 값이랑 비교해서 최솟값을 내놓고 map 으로 전부 연산한다음 그중 최댓값을 내뿜는데 ..
# 대체 이걸 어떻게 생각 해 낸건지 ..? ..



def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0


# 이사람도 이걸 어떻게 생각한건지 ... 나 잘 이해가 ..대체 어케 이런 규칙을 찾아내징 ..?