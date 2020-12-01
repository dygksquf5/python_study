# LIS 이용하여 문제 풀기!!

# 주어진 군대의 수
n = 7
# 주어진 군인별 전투력 !
array = [15, 11, 4, 8, 5, 2, 4]

# 문제에서 전투력을 내림차순으로 정렬하라고 했으니까
array.reverse()
# 이렇게 리벌스 한다음 LIS 사용해서 문제풀겠음


# dp 테이블 리셋하기
d = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            d[i] = max(d[i], d[j] +1)

# 그러면 LIS 로 인해서 가장긴증가하는 부분수열 찾았으니까, 처음 주어진 총 군인 길이 n 에서 d 의 max 값을 빼면 됨 !
print(n - max(d))