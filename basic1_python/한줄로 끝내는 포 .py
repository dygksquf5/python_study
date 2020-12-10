# 출석번호가 1,2,3,4,5 있는데, 거기에 100을 붙여서 번호 부르기
 
students = range(5)
students = [i + 100 for i in students]
print(students)


#학생이름을 길이로 변환

students_name = ["Thor", "Iron Man","I am grooooot"]
students_name = [len(i) for i in students_name]
print(students_name)

#학생 이름을 대문자로 변환

students_up = ["Thor", "Iron Man","I am grooooot"]
students_up = [i.upper() for i in students_up]  # upper 옆에 () 실행 써주기! 
print(students_up)