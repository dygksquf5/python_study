try:
    print("나누기 전용 계산기입니다. ")
    # num1 = int(input("첫번째 숫자를 입력 하세요 ! : "))
    # num2 = int(input("두번째 숫자를 입력 하세요 ! : "))
    num = []
    num.append(int(input("첫번째 숫자를 입력하세요 ! :")))
    num.append(int(input("두번째 숫자를 입력하세요 ! :")))
    # num.append(int(num[0]/int(num[1]))) # 나머지 전부 다 ~ 예외 처리 에러!
    print("{0} 나누기 {1} 은 {2} 입니다.".format(num[0], num[1], num[2]))

    # print("{0} 나누기 {1} 은 {2} 입니다.".format(num1, num2, int(num1/num2)))
except ValueError:
    print("에러! 잘못된 값을 입력하셨습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생했습니다! ")
    print(err)