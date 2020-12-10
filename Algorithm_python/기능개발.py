import math


def solution(pro, spd):
    #     answer = []

    # tem = [math.ceil((100-i)/j) for i,j in zip(pro, spd)]
    # print(tem)
    #     index = []

    #     for i in range(len(pro) - 1):
    #         if tem[i] < tem[i+1]:
    #             index.append(tem.pop(i))
    #             answer.append(len(index))
    #             index = []
    # #         elif tem[i] >= tem[i+1]:
    # #             index.append(tem.pop(i))

    # #         if len(tem) == 1:
    # #             index.append(tem[0])
    # #             answer.append(len(tem))


    # 나는 메스를 써서 ceil 하려고 했는데.. 그리고 결국 난 못품, 근데
    # 이사람 코드 진짜 간결하고 완벽함 ... 일단 math 모듈안쓰려고 음수 나누기를 한다음 다시 한번 음수로 묶어서
    # 양수로 바꿈, (음수로 나누기 한다음 몫만 내놓은건 가우스 법칙으로 인한 .. )
    # 다음 값이 현재값보다 작거나 같으면 +1  해주기.
    Q = []
    for p, s in zip(pro, spd):
        if len(Q) == 0 or Q[-1][0] < -((p - 100) // s):
            Q.append([-((p - 100) // s), 1])
        else:
            Q[-1][1] += 1
    return [q[1] for q in Q]