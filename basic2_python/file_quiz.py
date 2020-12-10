# 매주 1 회 작성해야 되는 보고서가 있음!
# 1-50 까지 자동으로 보고서 만드는 프로그램 만들기!


number = range(1, 51)

# 이거 실행시키면 파일 50 개 만들어짐!

# with open("paper{0}.txt".format(testtest), "w", encoding="utf8") as paper_file:
#     paper_file.write("testtest")

# for i in number:
#     with open("paper{0}.txt".format(i), "w", encoding="utf8") as paper_file:
#         paper_file.write("- {0} 주차 주간보고 - "\
#                          "\n부서: 개발업무팀"\
#                          "\n이름: 김요한"\
#                          "\n업무요약: 프로그램 개발 ".format(i)\
#                          )

# 만들어진 파일 확인 한번 해보기!

with open("paper1.txt", "r", encoding="utf8") as paper_file:
    print(paper_file.read())




# 다른사름이 하는 방법, 이런식으로!
# for i in range(1, 51):
#     with open(str(i)+ "주차.txt", "w", encoding="utf8") as paper_file:

