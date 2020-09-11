print ("a" + "b")
print ("a","b")

# 방법 2 

print ("나는 %d 살 입니다. " %20)
print ("나는 %s를 좋아해요 " % "파이썬")
print ("Apple는 %c로 시작해요" %"A")
#  d 는 정수, s 는 스트링 , c 는 캐릭터(한글자만) 인데, s 를 사용하면 사실 전부 다 사용가능.

print ("나는 %s 색과 %s 를 좋아합니다." %("빨간", 2))
# 대신 %s 로 여러개를 묶을땐 괄호로 한번 더 엮어주기 .

#방법 3

print ("나는 {}색을 좋아하고, {}을 좋아해요.".format("빨간",4 ))
print ("나는 {1}색을 좋아하고, {0}을 좋아해요.".format("빨간",4 ))
# 인덱스를 안넣으면 순서대로 출력, 인덱스 넣어주면 인덱스 위치 값을 출력

print ("나는 {age}살 이며, {colour}색을 좋아해요".format(age = 14, colour = "빨간"))

age = 16
colour = "노란색"
print(f"나는 {age} 살 이며 {colour}을 좋아합니다.")

# ----------------------탈출문장 -------------------------

# print ("나는 "파이썬" 입니다." )
# 이건 오류가 남. 
print ("나는 '파이썬'입니다. ") #or
print ("나는 \"파이썬\"입니다.") # 이런식으로 
 #그렇기때문에 역슬레쉬 쓸 일이 있을땐 \\ 두개를 써야 함
print ("dygks\\quf\\5\\12\\13")
#\r 커서를 제일 앞으로
print ("Red Apple\rPine")
#\b 백스페이스 (한글자 삭제)
print ("Redd\b Apple ")
#\t 탭 
print ("Red\tApple")

# ---------------------- 퀴즈  -------------------------


password = input("이메일을 입력 해 주세요   : ")
# password1 = password[8:13]
password1 = password.replace("http//:","")
password1 = password1[0:password1.index(".")]
result = password1[0:3] + str(len(password1)) + str(password1.count("e")) + "!"
print ( " 비밀번호는  : "+ result + "입니다.")
# http:// 이부분을 replace 로 없애도 됨!!! 이걸로 다시 코딩 ㄱ ㄱ 







































