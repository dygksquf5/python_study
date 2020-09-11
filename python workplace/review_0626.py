# 사전! dic.
# key : value
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3]) #1 번째 방법
print(cabinet.get(3))#2번째 방법
#이렇게 딕셔너리 불러오는건 두가지 방법. 하지만 두개가 다른 실행방식을 지님 

#1번째 방법 
# print(cabinet[5])
# print("Hi") 이렇게 하면, keyError  남 !! hi 출력도 안됨
#2번째 방법
print(cabinet.get(5)) #이렇게 했을 땐, none 값으로 반환 & hi 출력 
print("Hi")

# 여기 get 으로 가져올 때 ,5는 사전에 없어서 none 값 나오는데, none 대신 원하는 출력값 입력가능
print(cabinet.get(5, "사용가능"))

print(3 in cabinet) # True
print(5 in cabinet) #False 
# in 이용해서 키가 사전안에 있는지 확인

#사전 키값은 꼭 정수가 아니어도 됨 .. 
cabinet2 = {"A-3":"유재석", "B-3":"김태호"}
print(cabinet2["A-3"])
print(cabinet2["B-3"])

#새로운 값 추가 ! 
cabinet2["A-3"] = "김종국" #기존 키값에 replace 하게 됨
cabinet2["C-2"] = "조세호" # 딕셔너리에 새로운 값 추가 

print(cabinet2)

del cabinet2["A-3"] # 딕셔너리 안에 값 삭제 
print(cabinet2)

#key들만 출력 , value 들만 출력
print(cabinet2.keys())
print(cabinet2.values())
print(cabinet2.items())
print(cabinet2)

#딕셔너리 값 완전 삭제 
cabinet.clear()
print(cabinet)


#------------------튜플! 수정 변경등 불가! but 실행속도 빠름------

menu = ("돈까스", "치즈돈까스")
print(menu[0])
print(menu[1])

# 튜플 장점은! 한번에 값 선언 가능! 예를들면 

(name, age, hobby) = ("김종국", 20 ,"코딩")
print(name, age, hobby)

#----------------- 세트 (set)_ 집합 ------------
# 중복불가, 순서도 없음 

my_set= {1,2,3,4,4,4,4,4} #중복 값 무시! 
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석","박명수"])

#교집합 출력해보기 ( java 와 python 모두 가능한 사람으로)
print(java & python)
print(java.intersection(python))
#합집합! 둘중하나만 가능하더라도 ㅇㅋ 
print (java| python)
print(java.union(python))

#차집합! java는 할수 있지만, python 은 할 줄 모르는 사람 
print(java-python)
print(java.difference(python))

#추가하기! 
python.add("김태호")
print(python)

#빼기 ! 
java.remove("김태호")
print(java )


#---------------------자료구조의 변경 --------
menu = {"커피","우유","쥬스"}
print(menu)


#---------------------