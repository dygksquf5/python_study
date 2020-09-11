#지하철 칸별로 10명 20명 30명 

subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석","조세호","박명수"]
print(subway)

print(subway.index("조세호"))

#하하씨가 추가 됨!!! 

subway.append("하하")
print(subway)


subway.insert(1, "정형돈")
print(subway)

#pop 해서 맨 뒤에 있는 애 부터 꺼내 출력하기! 내장함수 
print(subway.pop())

subway.append("유재석")
print(subway)
print(subway.count("유재석"))
#카운트로 vlaue 가 몇번나오는지 ! 

