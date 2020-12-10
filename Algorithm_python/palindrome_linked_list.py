# 팰린드롬 연결 리스트

# 파이썬의 리스트로 변환후 풀어보기
from typing import List, Deque

import collections


def is_palindrome(head):
    # 이렇게 리스트를 써도 괜찮지만! 시간복잡도 0(1) 이 되기 위해선 데크를 사용하는 게 더 좋은 방법 !
    # q: List = []
    # 이렇게 데크 이용하면! 양방향 리스트가 되니까ㅏㅏㅏ 개 꾸 울
    q : Deque = collections.deque()

    if not head:
        return True

    node = head

    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        # 데크를 써서! pop 부분을 변경 해주기! 이렇게 ! popleft 로 ! 제일 왼쪽 이라고 명칭 !
        if q.popleft() != q.pop():
            return False

        return True


