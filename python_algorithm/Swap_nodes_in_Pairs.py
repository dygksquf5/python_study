


class Solution:
    # 변칙적이지만 간편한 풀이 1
    def swapPairs_1(self, head: ListNode) -> ListNode:
        cur = head

        while cur and cur.val:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next

        return head

    # 노드가 직접 바뀌긴 하지만, 반복구조로 스왑하여 푸는 형식... ( 좀더 이해가 필요함 ㅠㅠ )
    def swapPairs_2(self, head : ListNode) -> ListNode:



    # 재귀 구조로 스왑! (처음 헷갈리겠지만, 기억안나면 다시 그림 그려보면서 잘 생각해보기!  )

    def swapPairs_3(self, head : ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            head.next = self.swapPairs_3(p.next)
            p.next = head
            return p
        return head
