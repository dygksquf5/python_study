# 입력  " A man, a plan, a canal: Panama"
# result : true
import collections
import re
from typing import Deque



# strs = []


def some(s: str) -> bool:
    for char in s:
        # isalnum 알파벳이냐 넘버냐 하는 여부를 판별하는 함수!
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        # pop() 안에 인덱스 값! 그냥 빈공간은 제일 마지막 !
        if strs.pop(0) != strs.pop():
            return False
    return True


# print(some("A man, a plan,a canal: Panama"))


# 하지만 데크Deque 를 사용해서 속도를 좀더 높일 수 있음!! 큐의 연산때매 그냥 리스트에서는 시간복잡도가 좀더 올라감. 특히 .pop(0) 은
# 시간 복잡도가 0(n) 임 ㅠㅠㅠ 그래서 복사가 가능한 데크 사용 !


def some_2(s: str) -> bool:
    strs: Deque = collections.deque()
    # print(strs)
    # print(type(strs))

    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    # 2까지만 해야 되는 이유는 두개씩 비교해야 되기 때문!!!
    while len(strs) > 1:
        # pop으로 하나씩 빼면서 그냥 제일 끝네있는걸 비교해버리면 되니까 개꿀 !
        if strs.popleft() != strs.pop():
            return False

    return True


# print(some_2("A man, a plan,a canal: Panama"))


# 사실 파이썬에서 가장좋은건 슬라이싱 기능을 사용하는 것이다! 파이썬의 가장 큰 장점중 하나기때문 !

def some_3(s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)
    print(s)

    return s == s[::-1] # 슬라이싱! 특히 ::-1 를 하면 reverse 됨!


print(some_3("A man, a plan,a canal: Panama"))



