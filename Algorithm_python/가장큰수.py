import itertools
import functools


def solution(numbers):
    answer = ''

    a = list(map(lambda x: "{}".format(x), numbers))
    a.sort(key=lambda x: int(x[0]), reverse=True)

    # 이게 아님, 경우의 수 만드는걸로 접근 해야 됨
    nums = [["".join(i)] for i in itertools.permutations(a)]
    answer += "".join(max(nums))
    return answer


# 이건 근데 시간초과가 된다ㅏㅏ 그럴거라 예상은 했지만 .. 입력값의 길이가 커지면 커질수록 ... ㅜ

# 다른사람이 푼거
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))


# 아니 이게 진짜 미친 풀이인데 ... 진짜 어떻게 이런생각을 했는지 경이롭다
# 일단 뭐 다 재끼고, lambda식쪽이 진짜 경이로운데
# 이게 일단 입력값이 만약 [6, 10, 2] 일 경우
# 람다로 x*3 을한다면, 얘네를 지금 스트링으로 바꿨기때문에
# [666 ,101010, 222 ] 이렇게 되고, 여기서 스트링이기때문에 일단 제일 앞 인덱스인 [0] 번째의
# 각각 아스키코드 값으로 비교를 한다.  만약[0] 이 같다면 [1] 로 아스키코드 구분한다
# *3 을 하는 이유는 결과적으로 최대 1000 까지가 각 원소로 주어지기때문에 !


# 또 다른사람 답변
def comparator(a, b):
    t1 = a + b
    t2 = b + a
    return (int(t1) > int(t2)) - (int(t1) < int(t2))  # 이게 진짜 어마어마한듯 .. 우아하다 정말


print(comparator(1, 0))



# 이런 예제 참고해보기 !
l = ['d', 'a', 't', 'a']


def comparator(x, y):
    return ord(x) - ord(y)


l = sorted(l, key=functools.cmp_to_key(comparator))
print(l)  # ['a', 'a', 'd', 't']

l = sorted(l, key=functools.cmp_to_key(comparator), reverse=True)
print(l)  # ['t', 'd', 'a', 'a']
