#표준체중 구하는 프로그램 만들기!

# 남자는 키 x 키 x 22
# 여자는 키 x 키 x 21
# 키는 (m) 단위로! /100 해주기!

def std_weight(height, gender):
    height = height/100
    if gender == "남":
        avarage = round(height * height * 22, 2)
        print("당신의 키는 {0}이며, 표준체중은 {1}입니다. ". format(height, avarage))
    elif gender == "여":
        avarage = round(height * height * 21, 2)
        print("당신의 키는 {0}이며, 표준체중은 {1}입니다. ". format(height, avarage))
    else:
        print("성별을 '남', 또는 '여', 둘중 하나로 입력 해 주세요")


std_weight(178, "남")