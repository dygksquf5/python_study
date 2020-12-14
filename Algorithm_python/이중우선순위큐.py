# 근데 사실 큐로 풀지는 않음 ..

def solution(operations):
    answer = []
    changed = [[x[0], x[2:]] for x in operations]
    number = list(map(int, [changed[x][1] for x in range(len(changed))]))

    for i in range(len(changed)):
        # hq.heapify(answer)
        if changed[i][0] == "I":
            answer.append(number[i])

        elif changed[i][0] == "D":
            if int(changed[i][1]) < 0 and len(answer) != 0:  # -1 이면

                answer.remove(min(answer))

            elif int(changed[i][1]) > 0 and len(answer) != 0:  # 1 이면
                answer.remove(max(answer))

    if len(answer) == 0:
        return [0, 0]
    else:
        last = [max(answer), min(answer)]
        return last









# input ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
# 기댓값 〉	[333, -45]


print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))