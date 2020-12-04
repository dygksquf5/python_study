# # 이건 내 풀이 ...  런타임 뜬당 ㅠㅠㅠ
#
# import collections
#
#
# def solution(genres, plays):
#     answer = []
#     part = collections.Counter(genres)
#     num = []
#     tem = [0] * len(list(part))
#
#     for i in range(len(genres)):
#         num.append(i)
#
#     genre = list(zip(num, genres))
#     play = list(zip(plays, num))
#
#     for p in range(len(list(part))):
#         for i in num:
#             if genre[i][1] == list(part)[p]:
#                 tem[p] += play[i][0]
#
#     big = list(zip(tem, list(part)))
#
#     big.sort(reverse=True)
#     for i in range(len(big)):
#         tem = []
#         for v in range(len(genre)):
#             if big[i][1] == genre[v][1]:
#                 tem.append(play[v])
#                 tem.sort(reverse=True)
#         for n in range(0, 2):
#             answer.append(tem[n][1])
#
#     return answer



genre = ["classic", "pop", "classic", "classic", "pop"]
play = [500, 600, 150, 800, 2500]

# 밑에 람다식 쉽게 이해할 수 있게 연습해봤당 !
testtest = [[1,100],[2,100],[3,100],[4,100]]
a = list(map(lambda y: y[0], testtest))
b = sum(map(lambda y: y[0], testtest))
print(a)


def solution(genres, plays):
    answer = []
    d = {e: [] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1], e[2]])

    genre_sort = sorted(list(d.keys()), key=lambda x: sum(map(lambda y: y[0], d[x])), reverse=True)
    for g in genre_sort:
        temp = [e[1] for e in sorted(d[g], key=lambda x: (x[0], -x[1]), reverse=True)]
        answer += temp[:min(len(temp), 2)]
    return answer


print(solution(genre, play))