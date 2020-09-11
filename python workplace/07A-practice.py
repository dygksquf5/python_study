#방법 1 
print ("나는 %d살 입니다" % 20) #d는 항상 정수

print ("나는%s을 좋아해요 " %"파이썬") #s는 'str 문자 '
print ("Apple은 %c로 시작해요"%"A") # c 는 캐릭터, 즉 한 글자만 받겠다는 이야기

# %s 는 정수 글자 다 표시가능

#방법 2
print("나는{}살 입니다." .format(20))
print("나는{}색과 {}색을 좋아해요" .format("파란","빨간"))
print("나는{0}색과 {1}색을 좋아해요" .format("파란","빨간"))
print("나는{1}색과 {0}색을 좋아해요" .format("파란","빨간"))

#방법3

age = 20
color = "빨간"
print(f"나는 {age}살 이고, {color}색을 좋아합니다.")




# \n 은 줄바꿈 

print ("저는 \"나도코딩\" 입니다")

# \\ : 문장안에서는 \ 로바뀜

print("dlkslkd\\adlkjaf\\asdlkjalf\\")

#\r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")