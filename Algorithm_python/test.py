
# 신용카드 유효성 검사 문제!
# 1) 주어진 신용카드는 16자리, 중간에 - 가 있어도 되고 없어도 됨, 숫자가 총 16자리여야지 유효
# 2) 만약 - 가 있는 경우 - 가 4개가 없이 잘못된형태로 제출 되면 옳바르지 않은 카드번호
# 3) 숫자가 16자리 이하여도 유효하지않음!
# 4) 만약 유효한 신용카드 값을 받았으면 이 숫자가 정말 옳바르게 생성되었는지 알아보는 과정필요 !
#       - 먼저 가장 오른쪽 부터 인덱스 1 로 시작하여 왼쪽으로 갈 수록 인덱스느 ㄴ늘어남. 즉 제일 왼쪽자리는 인덱스 16
#       - 짝수 인덱스는 각 숫자마다 *2 를 한다음, 만약 *2를 한 숫자가 10의자리가 나올 경우 10의 자리의 첫번째 숫자와 두번째 숫자를 더하기
#       -  ex) 6 * 2 = 12 이면, 이 숫자를 더하면 = 3 이 나옴!
#       -  이렇게 더한 짝수를 (1) 이라고 가정
#       -  이제 홀수 인덱스들은 홀수 인덱스끼리 모두 더하기, 그리고 이 결과값을 (2) 라고 가정
#       -  마지막으로 (1) + (2) 가 10 으로 딱 맞게 나누어질 때, 해당 카드번호는 유효한 카드번호라고 할 수 있음
#       -  처음 입력받은 파라미터의 갯수만큼 return 이 [0,0,0,0,0 ] 이런식으로 표시되는데, 만약 이 순서중 유효하다고
#           판단된 카드번호가 있으면, 해당 인덱스 자리에 [1,1,0,0,0 ] 이런식으로 1 이 추가가 됨!
#       -  이 결과값을 최종적으로 return 하기!



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
    tem_odd = collections.deque()
    for o in cheking:
        for i in range(1, len(o) + 1):
            rev = list(reversed(o))
            if i % 2 != 0:
                tem_odd.appendleft(int(rev[i -1]))
                if len(tem_odd) == 8:
                    odd.append(sum(tem_odd))
                    tem_odd.clear()

    # print(odd)

    # 짝수 곱하기
    # 임시로 값 풀어서 곱셈 넣어놓기
    tem = collections.deque()
    for d in cheking:
        # 인덱스를 1 부터 16 까지 하라 했기때문에, 1-16까지 range 하고 짝수 걸러내기 위해 2 나눠서 걸러주고, 실제 값 넣을땐 -1 해서 원래인덱스 넣어주기
        for i in range(1 , len(d) + 1 ):
            rev = list(reversed(d))
            if i % 2 == 0:
                # 리벌스로 뒤집어주자! 문제가 제일 오른쪽이 인덱스 1, 즉 제일 왼쪽이 인덱스 16인데 그냥 리스트 뒤집어서 1 부터 주자
                # 그리고 뒤집혀 있는 애들을 다시 왼쪽부터 채워서 넣어주자! 원래 카드번호 순서대로 바껴야되니까 !
                tem.appendleft(int(rev[i -1]) * 2)


    # tem 값에다 10의자리 있는 수부터는 더하기 해서 다시 리스트 뽑아내기 !

    a = []
    # index = 0
    print(tem)
    for i, v in enumerate(tem):
        # dic_answer = list(for_answer_index.keys())
        b = i % 8
        if v < 10:
            a.append(v)
            if b + 1 == 8:
                # sum으로 구한 값을 모두 더해서 짝수 리스트에 넣어놓기 !
                even.append(sum(a))
                # for_answer_index[dic_answer[index]].append(even[index])
                a = []
                # index += 1
        elif v >= 10:
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



