# http://naver.com

url = "http://naver.com"
my_str = url.replace("http://", "") #중요 즉 리플레이스로 (a 를 , b 로 바꾸겠다!!)
# print(my_str)
my_str = my_str[:my_str.index(".")]#중요..
# print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 사이트 비밀번호는 {1} 입니다.".format(url, password))



