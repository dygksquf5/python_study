import pprint

# 자료형에 인덱스 포함하여 출력할 때

# 보통은
a = ["김요한", "김예은", "아무개", 3, True]

for i in range(len(a)):
    print(i, a[i])

# 두번째

i = 0
for v in a:
    print(i, v)
    i += 1

# 위의 두방법은 불필요한 부분이 많다 ! 가장 깔끔한건 enumerate() 사용 !

for i, v in enumerate(a):
    print(i, v)

# 몫과 나머지 동시에 구할 때는 ??

print(divmod(5, 2))

my_status = [100, 5, 8]
for i in range(len(my_status)):
    if my_status[i] == 100:
        my_status[i] = "배"
    elif my_status[i] == 5:
        my_status[i] = "고"
    elif my_status[i] == 8:
        my_status[i] = "파"

print(' '.join(my_status))

# locals로 로컬 선언된 모든 변수조회함!!! 개 꿀 디버깅 !
pprint.pprint(locals())
