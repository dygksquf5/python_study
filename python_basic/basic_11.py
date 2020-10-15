# pickle 을 사용할건데, 꼭 "rb" 처럼 뒤에 b 로 바이너리로 사용! , 그리고 utf8 필요없음

import pickle

# profile_file = open("profile.pickle", "wb")
# profile = ("이름 : 김요한 ", "나이 :", 20, "취미: ", ["축구", "독서", "음악감상"])
# pickle.dump(profile, profile_file) # profile 에 있는 정보를 profile_file 에 저장하겠다!
# print(profile)
# profile_file.close()

# pickle 정보 읽기!

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()

