a = [5, 2, 8, 9, 10, 33, 66, 3, 1]
answer = []


def sor(ans, a):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
    answer.append(a[-1])

    if len(a) == 1:
        return
    sor(answer, a[:-1])
    return list(reversed(answer))


print(sor(answer, a))
