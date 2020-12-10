# 파일을 만들기! 파일이름과, w 써서 쓰기타입으로 지정하고, 한글사용 가능하게 utf8 인코딩 해주기

# score_file = open("score.txt", "w", encoding="utf8")
# print("수학: 0", file=score_file)
# print("영어: 50", file=score_file)
# score_file.close()

# 위와같이 해도 되지만, 다른 방법으로도 !
# "w" 를 하면 덮어쓰기가 되어버림 (이미 생성 된 경우! ), 이를 방지하기 위해 "a" append 써서 추가해줘야 함

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학: 80")
# score_file.write("\n코딩: 100") # print 가 아니기때문에 \n 으로 줄바꿈 해주기!
# score_file.close() # 닫기 까먹지말기!


# 파일 한번에 전부 다 읽어오기!

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

# 파일 한줄 씩 읽어오기!

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # readline 은 한줄을 읽고나서 바로 다음줄로 커서가 자동 이동 됨! ,
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

print("------------------")

# 근데 만약 다른사람의 파일을 우리가 열어보려 할 때, 몇줄인지 알 수 없으니 그럴때 라인별로 출력 하려면 이렇게!

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    else:
        print(line, end="")
score_file.close()

print("\n-------------------")

# 저 방법도 번거로우면! 파일 전체를 list 에 넣고 for 문으로 뽑아낼 수도 있음
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 로 line 전부 다 저장
for line in lines:
    print(line, end=" ")

score_file.close()