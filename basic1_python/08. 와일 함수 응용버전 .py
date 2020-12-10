# 원하는 손님이 올 때 까지 while 반복 써서 반복해보기!! 

customer = "토르"
person = "unknown"

while person != customer:
    print("주문하신 커피가 나왔습니당")
    person = input("성함이 어떻게 되세요?  : ")
    if person == customer:
        print("네 여기있습니다 '{0}' 고객님".format(person))
    else:
        print("죄송합니다 '{0}' 고객님, 아직 준비가 덜 되 었습니다.".format(person))

