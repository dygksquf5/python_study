# 공부가 더 필요 ㅠㅠ !

import heapq
from typing import List


class ListNode(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = ListNode(None)
        self.size = 0
        # 이렇게 해더랑 테일 주면 원형 연결 리스트 됨!
        # self.head = ListNode("dummy")
        # self.tail = ListNode("dummy")
        # self.head.next = self.tail

    def list_size(self):
        return self.size

    def is_empty(self):
        if self.size != 0:
            return False
        return True

    def select_node(self, idx):
        if idx >= self.size:
            print(" Index Error ")
            return None
        elif idx == 0:
            return self.head
        else:
            target = self.head
            for cnt in range(idx):
                target = target.next
                return target

    def append_left(self, value):
        if self.is_empty():
            self.head = ListNode(value)
        else:
            self.head = ListNode(value, self.head)
        self.size += 1

    def append(self, value):
        if self.is_empty():
            self.head = ListNode(value)
            self.size += 1
        else:
            target = self.head
            while target.next is not None:
                target = target.next
            new_tail = ListNode(value)
            target.next = new_tail
            self.size += 1

    def insert(self, value, idx):
        if self.is_empty():
            self.head = ListNode(value)
            self.size += 1
        elif idx == 0:
            self.head = ListNode(value, self.head)
            self.size += 1
        else:
            target = self.select_node(idx - 1)
            if target is None:
                return
            new_Node = ListNode(value)
            tmp = target.next
            target.next = new_Node
            new_Node.next = tmp
            self.size += 1

    def delete(self, idx):
        if self.is_empty():
            print('Underflow: Empty Linked List Error')
            return
        elif idx >= self.size:
            print('Overflow: Index Error')
            return
        elif idx == 0:
            target = self.head
            self.head = target.next
            del target
            self.size -= 1
        else:
            target = self.selectNode(idx - 1)
            del_target = target.next
            target.next = target.next.next
            del del_target
            self.size -= 1

    def print_list(self):
        target = self.head
        while target:
            if target.next is not None:
                print(target.data, '-> ', end='')
                target = target.next
            else:
                print(target.data)
                target = target.next

    def mergeKLists(self, lists : List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].data, i, lists[i]))

        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.data, idx, result.next))

        return root.next


t = LinkedList()
t.mergeKLists([[1, 4, 5], [1, 3, 4], [2, 6]]) # ?? 흠 ?






