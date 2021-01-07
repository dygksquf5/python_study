# 처음엔 itertools 로 한줄로 해결을 했었는데, 시간초과때문에 최대한 뺄건 배고 다시 itertools 로 돌렸눈데.. 그래도 시간초과 ㅠㅠ
# 다른방법을 생각 해 보자


import itertools

def solution(number, k):
    number = list(number)
    times = 0
    for i in range(0, k):
        if number[i] < number[i + 1]:
            number.pop(i)
            times += 1

    a = max(list(map(''.join, itertools.combinations(number, len(number) - (k - times)))))
    return a



# 다른 코드의 도움을 받아 작성해봤다. 그리디는 아직 좀더 공부가 필요한듯 하다.
def solution(number, k):
    stack = []

    for i in range(len(number)):
        if not stack:
            stack.append(number[i])
            continue

        isRemove = False

        while stack and int(stack[-1]) < int(number[i]):
            stack.pop()
            k -= 1
            if not k:
                isRemove = True
                stack += number[i:]
                break

        if isRemove:
            break

        stack.append(number[i])

    return "".join(stack[:len(number) - k]) if k else "".join(stack)
