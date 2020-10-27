# class 에 꼭 Exception 줘야 사용자 정의 Exception 이 가능함!! Exception 내장 클래스를 상속하게 되는 부분같음!

class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    print("한자릿수 나누기 계산기입니다. ")
    num1 = int(input("첫번째 숫자를 입력 하세요 ! : "))
    num2 = int(input("두번째 숫자를 입력 하세요 ! : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} 나누기 {1} 은 {2} 입니다.".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하셨습니다! ")
except BigNumberError as err:
    print("사용자 정의 예외처리 하기!! ")
    print(err)
