import collections


# 해시테이블 이용한 풀이!!

def newJewelsInStones(J: str, S: str) -> int:
    freqs = {}
    count = 0

    for char in S:
        if char not in freqs:
            freqs[char] = 1
        else:
            freqs[char] += 1

    for char in J:
        if char in freqs:
            count += freqs[char]

    return count


print(newJewelsInStones("aA", "aAAbbb"))


# collections 에 있는 defaultdict 사용해서 if 문으로 키값이 있나없나 여부 확인 하는걸 줄일 수 있음!

def newJewelsInStones_2(J: str, S: str) -> int:
    freqs = collections.defaultdict(int)
    count = 0

    for char in S:
        freqs[char] += 1

    for char in J:
        count += freqs[char]

    return count


print("difaultdict 사용하기 ! : ", newJewelsInStones_2("aA", "aAAbbb"))


# counter 로 각 개수 계산하는 부분까지 자동으로 처리하기 !

def newJewelsInStones_3(J: str, S: str) -> int:
    freqs = collections.Counter(S) # S 를 받자마자 바로 카운터로 계산하기!!
    count = 0

    for char in J:
        count += freqs[char]

    return count


print("Counter 사용한 코드! : ", newJewelsInStones_2("aA", "aAAbbb"))


# 가장 파이썬다운 방식! pythonic way !

# bool 값으로 S 를 가지고 있는 s 가 J 안에 있나없나를 봐서 출력되는 T/F 값에서 True 만 sum 함수로 개수 연산  후 리턴 .
def newJewelsInStones_4(J: str, S: str) -> int:
    return sum([s in J for s in S])


print("파이썬 다운 방식으로 한줄 표현! : ",newJewelsInStones_4("aA", "aAAbbb"))


