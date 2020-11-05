# generator 부분인데! 이부분 좀더 생각 해 봐 !!
import sys


def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n


g = get_natural_number()

for i in range(0, 5):
    print(next(g))


# generator 처럼 range 도 미리 생성해서 메모리를  차지하는것이 아닌, 생성조건만 생성 해놓을 수 있다 !

a = [n for n in range(1000000)] # 이건 이미 생성해서 a 에 갖고있음, 메모리 차지 올라감!!!
b = range(1000000) # 이건 range 로 조건만 둔 상태, 생성ㅇ전!

print(sys.getsizeof(a)) # 사이즈를 보삼! 메모리 겁나 차지함
print(sys.getsizeof(b))



