def deposit(blance, money):
    print("입금이 완료되었습니다. 입금하신 금액은{0} 원 이며, 잔액은 {1}원 입니다.".format(money, blance+money))
    return blance+money

def withdraw(blance, money):
    if money > blance:
        print("출금 가능 금액이 부족합니다. 현재 잔액은 {0}원 입니다.".format(blance))
        return blance
    elif money <= blance:
        print("출금이 완료되었습니다! 현재 잔액은 {0}원입니다.".format(blance - money))
        return blance - money

def withdraw_night(blance, money):
    commision = 100
    if money+commision > blance:
        print("출금 가능 금액이 부족합니다. 현재 잔액은 {0}원 입니다.".format(blance))
        return blance
    elif money+commision <= blance:
        print("출금이 완료되었습니다! 현재 잔액은 {0}원입니다.".format(blance - money - commision))
        return blance - money - commision







blance = 0
blance = deposit(blance, 3000)
blance = withdraw(blance, 50000)

blance = withdraw_night(blance, 700)

print(blance)


