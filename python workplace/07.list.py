print(1+1)

subway =[10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)
print(subway.index("조세호"))
subway.append("하하") #중요 ! 추가하는것 append
print(subway)

subway.insert(1, "정현돈")
print(subway)

#pop은 뒤에서부터 하나씩 꺼냄

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)


#같은 이름의 사람이 몇명 있는지 확인하기
subway.append("유재석")
print(subway)
print("---->",subway.count("유재석"))

#정렬도 가능
num_list = [5,2,4,3,]
num_list.sort()
print(num_list)

#순서뒤집집기
num_list.reverse()
print(num_list)

#모두 지우고싶을때

num_list.clear()
print(num_list)

#다양한 자료형 함께 사용// 즉 불리언값, 인트, 스트링 상관없이! 
mix_list = ["조세호", 20, True]
print(mix_list)
# 리스트 확장
num_list=[5,4,3,5,6,]
num_list.extend(mix_list)
print(num_list)


