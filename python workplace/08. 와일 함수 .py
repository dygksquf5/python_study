customer = "토르"
index = 5

while index >= 1:
    print ("커피가 준비되었습니다 '{0}'고객님, {1}번째 호출.".format(customer, index))
    index = index - 1 # index -= 1 
    if index == 0:
        print ("손님 커피 가져가지마세요 안줘안줘 ")

customer = "아이언맨일걸"
index = 0
while True:
    print ("{0} 님아 커피 나옴 가저가삼 ", "{1}째 호출중".format(customer, index))
    index += 1
 #멈추는법은 컨트롤 + 씨 ! 
 #무한루트에 빠짐 크크크 
