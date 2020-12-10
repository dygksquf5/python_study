from typing import List, Tuple, Any
import collections
import heapq


def topKFrequent(nums: List[int], k: int) -> List[int]:
    freqs = collections.Counter(nums)
    freqs_heap = []
    # 힙에 음수로 삽입!
    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))

    top_k = list()

    # k번 이상 등장하는 숫자만 추출해야됨,  최소 힙 이므로 가장 작은 음수 순으로 추출!

    for _ in range(k):
        # 빈도수 말고 가장 많았던 숫자만 뽑아내야되니까, 인덱스 0번째 있는 애들만 꺼내오기!
        top_k.append(heapq.heappop(freqs_heap)[1])

    return top_k


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))


# 하지만 가장 pythonic way 스러운 풀이가 있음! 내장함수 중에서 collections.Counter 에서 most_common 메소드를 제공함!
def topKFrequent_pythonic_way(nums: List[int], k: int) -> Tuple[Any, ...]:
    return list(zip(*collections.Counter(nums).most_common(k)))[0]


print(topKFrequent_pythonic_way([1, 1, 1, 2, 2, 3], 2))

# 언팩킹 * 는 활용도가 아주 많다! 예를들면

fruits = ["사과", "딸기", "바나나", "귤"]
print(fruits)  # 이대로는 그냥 리스트가 출력됨
print(fruits[0], fruits[1])  # 이렇게 하면 당연히 인덱스별로 출력되지!

for i in fruits:
    print(i, end=" ")  # 이렇게 하면 좀더 효율적이지!!!

print("\n ------------")
# 하지만 언펙킹을 쓴다면 !?
print(*fruits)  # 이렇게 다 풀어해치고 벨류 값만 쏵! 개꿀 !


# 함수에서 하나의 파라미터 받을 때, 팩킹 가능하다! (하나만 안넣어도 된다는 뜻 )
def f(*params):
    print(params)


f("사과", "딸기", "바나나", "귤")
