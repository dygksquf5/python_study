from typing import List


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        # linked list 뒤집기!
        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    def toList(self, node: ListNode) -> ListNode:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    # 다시 연결리스트로 바꿔주는데, 이방식으로 하면 뒤집힌 연결리스트가 나온다!, 만약 다시 원래대로 돌리고싶으면 다시 reverse 해주기!
    def toReverseLinkedList(self, result: ListNode) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 먼저 연결리스트를 reverse 로 뒤집고! 그다음 toList 로 파이썬리스트로 변경!
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        # 제일먼저 for 문으로 a,b 의 리스트들을 str 형식으로 바꾸고 join
        # 써서 하나로 뭉치기! 그다음 다시 int로 묶어서 숫자형태로 내오기, 그리고 더하기!

        resultStr = int("".join(str(e) for e in a)) + \
                    int("".join(str(e) for e in b))
        # 마지막으로 이걸 다시 연결리스트 형태로 변환해서 return 하기!
        return self.toReverseLinkedList(resultStr)