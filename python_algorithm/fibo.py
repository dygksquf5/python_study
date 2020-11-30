import time


def fibo(x):
    # 기본 설정! 1번째나 2번째는 1 이라는 수가 주어졌을 때 !
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

# 결국 재귀함수는 제일 마지막값까지 내려가서 거기서부터 리턴을 해 오기 시작하니까!!!
# 제일 마지막 내려가서 1+1 , 즉 1번째 2번째 더하고 ! 거기서부터 리턴값을 받아서 하나씩 올라오기!
# 하지만 단순 재귀를 하면! 이미 구한 값도 또 구하게 되니까, 시간복잡도가 어마어마어마어마함 .... 늘어날 수록 ..

print(fibo(4))

# 그렇기때문에 dp 즉 다이나믹 프로그래밍 방법으로 사용을 해보겠음

# 먼저 DP 테이블을 구현하자
# 재귀를 이용한 탑다운 형식

# 메모이제이션!
d = [0] * 100


def fibo(x):
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = fibo(x - 1) + fibo( x - 2)
    print(d)
    return d[x]


# print(fibo(99))


# 반복문을 이용한 바텀업 형식

d_button = [0] * 100
d_button[1] = 1
d_button[2] = 1
number = 99

for i in range(3, number + 1):
    d_button[i] = d_button[i - 1] + d_button[i - 2]


print(d_button[99])

