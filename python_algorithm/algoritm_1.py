from dataclasses import dataclass


@dataclass
class Rectangle:
    width: int
    height: int

    def area(self):
        return self.width, self.height


getAverage = Rectangle(11, 10)
a, b = getAverage.area()
print(a)
print(b)


# lambda 지린다 !!! 함수 안만들어도 댄다 이렇게 써버리자 한줄로 줄여지넹 ... 와우


a = list(map(lambda x: x + 20, [1, 5, 8]))
print(a)


# 리스트 컴프리헨션,, 이것도 미쳤따.. 한줄로 줄여버리네, 대신 리스트로 이루어져야 되기 때문에 이 모든걸 [] 대괄호로 묶어
# 해석을 해 보면, n *2 를 for 문 돌리면서 하는데 (1~10 까지), 언제? 만약 나머지가 1, 즉 홀수일 때! )
a = [n * 2 for n in range(1, 10+1) if n % 2 == 1]
print(a)
print(type(a))


# dictionary Comprehension

school = {1: "김요한", 2: "이신애", 3: "신은혜", 4: "이보선 "}
# 원하는 부분 사전 새롭게 정의하면서 없앨 수 도 있꼬!
# school = {value:key for key, value in school.items() if key != 2}
# 그냥 이렇게 재정의 하기만 할 수도 있음! comprehension 은 이런식으로 ! 문법이 동일함 !
school = {value:key for key, value in school.items()}
print(school)
