# 연결 리스트를 이용한 스택 ADT 구현

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.last = None

    def push(self, data):
        self.last = Node(data, self.last)
        return self.last

    def pop(self):
        data = self.last.data
        self.last = self.last.next
        return data


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.pop())
print(stack.pop())
print(stack.pop())
