# 치킨집 웨이팅 퀴즈 풀기! 예외처리까지!

chicken = 10
waiting = 1


class SmallNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class SoldOutError(Exception):
    pass


while True:
    try:
        order = int(input("현재 주문가능 치킨 수 : [{0}] \n 치킨을 몇마리 주문하시겠습니까? :    ".format(chicken)))
        if order > chicken:
            print("재고가 충분하지 않습니다. 현재 주문 가능한 치킨 수는 {0} 마리 입니다.".format(chicken))
        elif order <= 0:
            raise SmallNumberError("입력갑 {0}".format(order))
        else:
            print("{0} 마리 주문이 완료되었습니다. 대기번호 [{1}] 번".format(order, waiting))
            chicken -= order
            waiting += 1
            if chicken == 0:
                raise SoldOutError
    except ValueError as err:
        print("잘못된 값을 입력하셨습니다. 숫자로 입력 해 주세요.")
        print(err)
    except SmallNumberError as err:
        print("0보다 작은 숫자는 주문이 불가능합니다.")
        print(err)
    except SoldOutError as err:
        print(" 주문 가능한 치킨이 없습니다. 재고소진으로 다음에 다시 방문 부탁드리겠습니다. ")
        break

    finally:
        print(" ------오늘도 저희 치킨집에 방문 해 주셔서 감사합니다.------")




