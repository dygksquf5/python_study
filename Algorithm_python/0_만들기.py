import copy
import itertools

# 재귀함수로 구현해도 되지만 간단하게 모듈 사용해서 이렇게 구현해도 같은 경우의 수를 도출해낸다.
tem = [' ', '+', '-']
print(len(list(itertools.product(tem,repeat=6)))) # 729 개 ! 사실 같음


def recursive(array, n):
    if len(array) == n:
        operator_list.append(copy.deepcopy(array))
        return
    array.append(' ')
    recursive(array, n)
    array.pop()

    array.append('+')
    recursive(array, n)
    array.pop()

    array.append('-')
    recursive(array, n)
    array.pop()




operator_list = []
n = 7

recursive([], n -1 )

integers = [i for i in range(1, n+1)]
print(len(operator_list))

for operator in operator_list:
    string = ''
    for i in range(n - 1):
        string += str(integers[i]) + operator[i]
    string += str(integers[-1])
    if eval(string.replace(" ",'')) == 0:
        print(string)
