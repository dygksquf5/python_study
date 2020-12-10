# 홀짝 연결리스트 !!

class Solution:
    def oddEvenList(self, head : ListNode) -> ListNode:
        # 예외처리
        if head is None:
            return None

        odd = head
        even = head.next
        # 마지막에 even 의 초기값, 즉 head.next 를 주기위해 변수로 남겨놓기!!!
        even_head = head.next

        #반복해서 홀짝 노드 처리!!
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        # 홀수 마지막 값과 짝수의 첫번째 값을 연결해주기!
        odd.next = even_head
        return head