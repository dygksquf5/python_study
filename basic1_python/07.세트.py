#세트 set 
#중복이 안되고, 순서가 없음 (집합)

my_set = {1,2,3,3,3,}
print(my_set) # 1,2,3 만 출력됨

java = {"유재석", "김태호", "양세형"}
python = set(["유재석","박명수"])

# #교집합 출력 (java와 phthon 모두 할 수 있는사람)

print(java & python)
print(java.intersection(python))

#합집합 (javq 도 할 수있거나, python 할 수 있는 개발자 )
print(java | python)
print(java.union(python))

# #차집합 (java 는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

#python 할 줄 아는 사람 늘어남
python.add("김태호")
print(python)

#java를 잊었어용
java.remove("김태호")
print(java)
