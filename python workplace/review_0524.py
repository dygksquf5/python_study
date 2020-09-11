print(abs(-5)) #절댓값 구하기. 
print(pow(2, 4)) # 제곱값 구하기 2^4 = 
print(max(5, 12)) #가장 큰 값 
print(min(5 ,12 ))# 가장 작은 값 
print (round(3.14)) #반올림
print ( round (3.99)) # 반올림

from math import* #math 에 있는거 * 이걸로 다~ 쓴다는 표시 
print (floor(4.99)) #바닥, 즉 소숫점이하 다 버림
print (ceil(3.14)) #소숫점 다 올림
print (sqrt(16)) #제곱근 구하는 공식, 즉 4 가 나오게 됨 4*4=16


# ================ random 함수 ================

from random import *

print (random()) 
print (random() * 10)  # 10까지 소수 포함해서 랜덤!  
print (int(random() * 45)) # 이렇게 하면 45까이고 소수표시없이 int 로 정수, 0부터 45까지
print (int(random() *45 +1)) #이렇게하면 0 이 안나오고 1~45임

# -- 이걸 더 좋은 방법으로 표현은 
print (randrange (1,46)) # 이건 1~45 까지, 즉 46 미만까지임 
# -- 또는 46 미만으로 하는게 헷갈릴때는 밑에처럼
print (randint (1,45 )) # 1부터45까지 



from random import *
x = randint(4,28)
print ("오프라인 스터디 모임 날짜는 매월 " + str(x) + "일로 선정되었습니다")
# 숫자를 문자열로 표현해줄 때, 꼭 앞에 str  써주기! (하지만 문자열 사이를 , 따옴표로 구분지을땐)
# str 이나 int 를 넣지 않아도 인식 가능, 하지만 따옴표를 넣으면 문자사이의 띄어쓰기가 되버림

# =================문자열 ======================
# 만약 문자열을 여러줄에 나누어 쓰고싶을 때 ! 
sentence = """
나는 김요한 입니다, 
나는 파이썬을 배우고 있습니다.
파이썬을 배우는 일은 너무나 즐겁습니다.
"""
print(sentence) 

#=============== 슬라이딩 ======================
jumin = ("940128-1709515")
print ("성별 :" + jumin[7]) # 즉 index 로, 7번째 있는 숫자를 출력 
print ("출생년도 : " + jumin[0:2]) # 2의 이전 값까지 , : 은 ~부터 ~까지라는 뜻으로 사용
print ("뒷자리 (뒤에서부터! )" + jumin[-7 :]) #즉 뒤에서부터 7번째, -7번째 부터~ 끝까지

# ====================문자열 함수====================
python =  "Python is Amazing"
print (python.lower()) #소문자 출력
print (python.upper())
print (python[0].isupper()) # index 0번째 문자가 대문지인지 알려주는 것
print (len(python)) # 변수의 문자열 길이를 알려즘 
print(python.replace("Python", "JaVa"))

index = python.index("n") # python 이라는 변수속에서 'n'위치의 index 값을 보여줌
print(index)
index = python.index("n", index + 1) # python이라는 변수 속에서 'n'위치에서 +1, 즉 첫번째 'n' 이후에 나오는 'n'의  index 값을 보여줌
print(index)
# ---- 비슷한 방법으론 
print (python.find ("n")) # 이러면 똑같이 5 를 반환하지만
print(python.find("JAVA")) # 이럴때, 문장에 JAVA 라는 글이 없으면, -1 을 반환함
#하지만 만약 print(pyton.index("JAVA")) 를 하게 되면 -1 이 아닌, 오류가 나버리게 됨

print(python.count("n")) #pyton 변수 안에서 n 이 총 몇번 등장하는지 출력하는 함수

