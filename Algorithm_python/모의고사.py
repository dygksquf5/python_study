def solution(answers):
    student = list(map(list, [x for x in zip(range(1, 4), [0] * 3)]))

    student1 = [1, 2, 3, 4, 5] * len(answers)
    student2 = [2, 1, 2, 3, 2, 4, 2, 5] * len(answers)
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * len(answers)

    def compare(x):
        if x[0] == x[1]:
            return 1
        else:
            return 0

    student[0][1] = sum(list(map(compare, [[x, y] for x, y in zip(answers, student1)])))
    student[1][1] = sum(list(map(compare, [[x, y] for x, y in zip(answers, student2)])))
    student[2][1] = sum(list(map(compare, [[x, y] for x, y in zip(answers, student3)])))

    sums = [i[1] for i in student]  # 맞춘 합 들어있는 리스트
    last = sorted([i for i in student if i[1] > 0])  # 을 제외한 학생들 수 , 오름차순
    print(last)
    if len(set(sums)) == 1:  # 모두 맞춘 수가 같으면
        return [i[0] for i in student]
    else:
        return [i[0] for i in last]
        # return [max(student, key=lambda x: x[1])[0]]



# 난 일단 이렇게 풀긴 했는데.. 다 맞추지는 못하넹 흐음