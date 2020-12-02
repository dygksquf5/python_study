import collections
from functools import reduce

list = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]


def solution(c):
    cnt = collections.Counter([b for a, b in c])
    return reduce(lambda x, y: x*(y + 1), cnt.values(), 1) - 1


print(solution(list))

testtest = [2,1]
print(reduce(lambda x, y: x * (y + 1), testtest, 1) - 1)

# 모자 2, 바지 1 , 신발1 일때
# 경우의 수 계산 해 보자,
# 문제에선ㄴ 하나씩만 입는것도 되고, 두개 또는 세개를 입어도 된다
# 그러면 모자는 2개의 선택지와 쓰지 않을 선택지까지 해서 총 3개의 선택지
# 나머지도 똑같이 신거나 입지 않을 선택지가 1 플러스 되니까
# 결국에는 이러한 경우 경우의 수는
# (2+1) * (1+1) * (1+1) 이다, 하지만
# 모두 벗는것은 안된다고 했으니까 여기서 모두 벗게되는 경우의 수 -1 을 해주면 된다
# 코드에서는 그렇기에 y + 1 을해주고, 연산을 위해 기본값으로 1 을 지정해서 넣어준다 !

# 사실 이 설명대로라면
import collections
from functools import reduce


def solution(c):                   # 여기처럼 처음에 아예 values 넣을 때 1을 더한다!
    return reduce(lambda x,y:x*y,[a+1 for a in collections.Counter([x[1] for x in c]).values()])-1

# 이렇게 짜는 코드가 좀더 이ㅎㅐ하기 쉬운 코드라고 볼 수 있다.
