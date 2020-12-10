def solution(candidates, target):
    result = []

    def dfs(csum, index, path):
        if csum < 0:
            return
        if csum == 0:
            result.append(path)
            return

        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])
            print(path)

    dfs(target, 0, [])
    return result


a = [2, 3, 6, 7]
print(solution(a, 7))



