

test_case = int(input())

for _ in range(test_case):
    n, m = list(map(int, input().split(' ')))
    q = list(map(int, input().split(' ')))
    q = [(i, idx) for idx , i in enumerate(q)]

    count = 0

    while True:
        if q[0][0] == max(q, key=lambda x: x[0])[0]:
            count += 1
            if q[0][1] == m:
                print(count)
                break
            else:
                q.pop(0)
        else:
            q.append(q.pop(0))



