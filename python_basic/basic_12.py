# with 로 간단하게 파일을 읽을수 있음! 그리고 with 사용하면 매번 파일을 close 해줄 필요가 없음! 자동으로 해줌!

# with 로 pickle 읽기!

# import pickle
#
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with로 일반파일 읽고 쓰기

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬 공부를 하고있습니다!")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

