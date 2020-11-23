import re, collections


def get_num(numbers):
    answer = [0] * len(numbers)
    a = 0
    cheking = collections.deque()
    even = collections.deque()  # 짝수 곱한다음, 십의자리는 앞뒤로 더한 수!
    odd = collections.deque()  # 홀수 모두 더한 값!!
    for_answer_index = collections.defaultdict(list)  # 여기 들어온 인덱스 값들은 유효성 비교가 더 필요하기때문에, 최종검사가 끝나고 정말 유효한 애들을
    # 1로 바꿔주기 위해 위치기억용 인덱스임!

    for i, v in enumerate(numbers):
        for n, m in enumerate(v):
            if m == "-":
                a += 1
                if a == 3:
                    # tem = re.sub("[-]", "", numbers[i])
                    cheking.append(numbers[i])
                    # i 는 number를 받은 value 의 key(인덱스) 값이니까 ! 이걸 넣어놔서 내가 몇번째 인덱스를 가지고 유효성 검사하는지 기억하기위함
                    for_answer_index[i]
                    # answer.insert(i, 1)

            if len(numbers[i]) == 16 and numbers[i] not in cheking:
                cheking.append(numbers[i])
                for_answer_index[i]

                # answer.insert(i, 1)

    # 특수문자 제거
    for new in range(len(cheking)):
        a = cheking.popleft()
        cheking.appendleft(re.sub("[-]", "", a))

    # for new in for_answer_index.values():
    #     a = re.sub("[-]", "", *new)
    #     print(a)

    # testtest = list(for_answer_index.keys())
    # print(testtest)

    # print(cheking)

    # 홀수 모두 더하기 !
    tem_odd = []
    for num, o in enumerate(cheking):
        for i in range(len(o)):
            a = i + 1
            if a % 2 != 0:
                tem_odd.append(int(cheking[num][i]))
                if len(tem_odd) == 8:
                    odd.append(sum(tem_odd))
                    tem_odd = []

    # print(odd)

    # 짝수 곱하기
    # 임시로 값 풀어서 곱셈 넣어놓기
    tem = collections.deque()
    for d in cheking:
        for i in range(len(d)):
            i += 1
            if i % 2 == 0:
                i -= 1
                tem.append(int(d[i]) * 2)

    # tem 값에다 10의자리 있는 수부터는 더하기 해서 다시 리스트 뽑아내기 !

    a = []
    # index = 0
    for i, v in enumerate(tem):
        # dic_answer = list(for_answer_index.keys())
        b = i % 8
        if v <= 10:
            a.append(v)
            if b + 1 == 8:
                # sum으로 구한 값을 모두 더해서 짝수 리스트에 넣어놓기 !
                even.append(sum(a))
                # for_answer_index[dic_answer[index]].append(even[index])
                a = []
                # index += 1
        elif v > 10:
            # 두자릿수 숫자 앞자리 뒷자리 더하기
            a.append(int(str(v)[0]) + int(str(v)[1]))
            # 8 자리마다 끊어서 리스트 만들기!
            if b + 1 == 8:
                # a = [int(v) + int(a[i+1]) for i, v in enumerate(a) if i > 8]
                even.append(sum(a))
                # for_answer_index[dic_answer[index]].append(even[index])
                a = []
                # index += 1

    # print(even) # 짝수

    # 유효한 숫자인지 확인해보기!
    tem_answer = []
    for i in range(len(even)):
        dic_answer = list(for_answer_index.keys())
        for_answer_index[dic_answer[i]].append(int(even[i]) + int(odd[i]))
        if int(*for_answer_index[dic_answer[i]]) % 10 == 0:
            answer.insert(dic_answer[i], 1)

    return answer


num = ["3285-3764-9934-2453", "3285376499342453", "3285-3764-99342453",
       "328537649934245", "3285376499342459", "3285-3764-9934-2452"]
print(get_num(num))



