import collections


class MyStack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)
        # 요소 삽입 후 맨 앞에 두는 상태로 재 정렬!
        print(self.q)
        for _ in range(len(self.q) - 1):
            # 제일 왼쪽에 있는 애를 pop 한다음 그걸 다시 append 하는거!!! 즉 큐를 이용하지만 스택을 구현하게 되는거지!
            self.q.append(self.q.popleft())
            print(self.q)

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        # 만약 이 조건이 맞으면 True 아니면 False
        return len(self.q) == 0


t = MyStack()
t.push(1)
t.push(2)
print(t.top())
