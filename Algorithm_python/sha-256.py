import hashlib


text = '안녕하세요! 제 이름은 김요한 이라고 합니다 오늘도 열공을 해 봅시당 ㅎㅎ '
encoded = text.encode()
result = hashlib.sha256(encoded).hexdigest()
print(result)



# 재미로 그냥 ... 느낌표 하나만 없어져도 완전 다른 해쉬값 나오고! 당연하지만 .. 그리고 겹치는 문자는 딱 4번뿐 ! 그냥 연관성이 1 도 없다는 느낌
# a = '9566d2a489692a554f1c5d301cb499ecabd3e9299cd2811e8d5ef954a24e4dfc'
# b =  '8a6ee158bff40f38a05fe8789751162fb0ec70d379df6589fce7fd1de6778d11'
#
# count = 0
# for i in range(len(a)):
#     if a[i] == b[i]:
#         count += 1
# print(count)
