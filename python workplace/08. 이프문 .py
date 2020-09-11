
# if 조건:
#     실행명령문
weather = input("오늘날씨는 어떤가요?")
if weather == "비" or weather == "눈":
    print("우산을 챙기세용!")
elif weather == "미세먼지":
    print("마스크를 챙기세용!!")
else:
    print("준비물이 암것도 노 필 요 합 니 댱! ")


temp = int(input("오늘 기온은 어떤가요?"))
if 30 <= temp:
    print("너무 더워용ㅠㅠㅠㅠ")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨입니당")
elif 0 <= temp < 10: # and 를 넣어도 되고, and 없이도 표현 가능 지금처럼
    print("외투를 챙기세용! ")
else:
    print("너무 추워요유ㅠㅠ나가지마세용가리치킨")


