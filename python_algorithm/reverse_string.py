# ["h", "e", "l", "l", "o"] 입력값 !

# 가장 전통적인 방법으로 투포인트 방식을 이용한 스왑!
from typing import List


def reverse_string(s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    # return s


a = ["h", "e", "l", "l", "o"]


# print(reverse_string(a))


# 하지만 pythonic way로 ! 아주 간결하게!!

def reverse_string_1(s: List[str])->None:
    # 참고!! reverse() 는 리턴값이 없는 함수임!! 그저 reverse 만 할 뿐 !
    s.reverse()
    return s


print(reverse_string_1(a))
