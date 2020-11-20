# 꼭 복습 해보기!!
import itertools
from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    result = []
    prev_elements = []

    def dfs(elements):
        # 리프 노드일 때 결과 추가
        if len(elements) == 0:
            # 변수를 그대로 넣지말고, 안에있는 값을 복사해서 넣는식으로 넣자! 파이썬은 객체를 참고하는 형태로 처리되니까 에러방지!
            result.append(prev_elements[:])

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return result


print(permute([1,2,3]))


# 하지만 파이썬은 itertools 라는 좋은 모듈을 재공하고있음!!! 반복자 생성에 최적화된 모듈임!

def permute_itertools(nums: List[int]) -> List[List[int]]:
    return list(map(list, itertools.permutations(nums)))


print(permute_itertools([1,2,3,]))