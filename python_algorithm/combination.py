

def combine(n, k):
    result = []

    def dfs(elements, start, k):
        if k == 0:
            result.append(elements[:])

        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, start + 1, k - 1)
            elements.pop()

    dfs([], 1, k)
    return result


print(combine(4, 2))

