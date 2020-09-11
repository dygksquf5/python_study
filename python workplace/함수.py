#함수 

# def open_account():
#     print("계좌가 열림니당당당")


# open_account()



def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance + money))
    return(balance + money)
def withdraw(balance, moeny):
    if balance > moeny:
        print ( "출금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance - moeny))
        return balance - moeny
    else:
        print (" 출금이 불가능합니다. 현재 잔액은 {0} 입니다.".format(balance))
        return balance

def withdraw_night (balance, money):
    if balance > money:
        commission = 100
        print("출금이 완료되었습니다. 수수료는 {0}원, 잔액은 {1} 원입니다.".format(commission, balance - money - commission ))
        return commission, balance - money - commission
    else:
        print ( "출금 할 수가 없습니다. 잔액은 {0} 원 입니다.".format(balance))
        return balance






balance = 0
balance = deposit(balance, 5000)
print(balance)

# balance = withdraw(balance, 3760)
# print (balance)

# balance = withdraw(balance, 4000)
# print(balance)

commission, balance = withdraw_night(balance, 200)
print (balance)

commission, balance = withdraw_night(balance, 2000)
print(balance)