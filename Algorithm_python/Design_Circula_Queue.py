class MyCircularQueue:
    def __init__(self, k : int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0  #front
        self.p2 = 0 # rear

        # enQueue(): 리어 포인터 이동
    def enQueue(self, value: int):
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            # 나머지만 남겨서 max 이상으로 p2가 안넘어가게 !!, 그리고 한칸 앞으로!
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            # None이 없으면, 즉 값이 가득 차 있으면!
            return False

    # deQueue(): 프론트 포인터 이동
    def deQueue(self) -> bool:
        if self.q[self.p1] is None:
            # 값이 없으니 뺄것도 없다 의 False
            return False
        else:
            # 값ㅅ이 있으면 빼자! !
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True

    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self) -> int:
        return -1 if self.q[self.p2 -1] is None else self.q[self.p2 -1]

    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None


q = MyCircularQueue(5)
print("비었냐 ? :", q.isEmpty())
print(q.enQueue(10))
print(q.enQueue(20))
print("비었냐 ? :", q.isEmpty())
print(q.enQueue(30))
print(q.enQueue(40))
print(q.enQueue(50))
print(" 가득 찼냐 ? :",q.isFull())
print(q.enQueue(10),"값이 가득차고 다시 리어가 0번째 인덱스 옴! 근데 값이 있어서 값을 못넣고 False 리턴! ")
print(q.deQueue()," 0번째 인덱스 값 지움 ! ")
print(q.enQueue(10),"0번째 인덱스에 값 넣음! ")

print(q.Front()) # 값을 뺄 때 마다 front =p1  앞으로 전진 한칸
print(q.Rear()) # 값을 넣을 ㄸㅐ 마다 rear (peek) =p2 앞으로 전진 !
