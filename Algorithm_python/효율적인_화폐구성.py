# n 은 화폐 갯수
# m 은 액수

n = 3
m = 7

# 주어진 화폐 단위
array = [2, 3, 5]

# 테이블을 만들어야 하니까, 주어진 액수 갯수만큼 테이블 만들어놓기 !
# 그리고 만약 주어진 액수를 만들 수 없을 때는 -1을 출력해야 하기때문에, 일단 디폴트값으로 최대 액수인 10001 원을 입력 해 놓기 !
d = [10001] * (m + 1)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)
        print(d)


if d[m] == 10001:
    print(-1)
else:
    print(d[m])




