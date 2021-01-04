# # 이진트리의 최대 깊이
#
# import collections
#
#
# tree = [3, 9, 20, None, None, 15, 7]
#
#
# def maxDepth(root):
#     if root is None:
#         return 0
#     root = collections.deque(root)
#
#     queue = collections.deque()
#     queue.append(root.popleft())
#
#     depth = 0
#
#     while root:
#         depth += 1
#         # 큐 연산 추출 노드의 자식 노드 삽입
#         for _ in range(len(queue)):
#             cur_root = queue.popleft()
#
#             if root[0] is not None and root[1] is not None:
#                 queue.append(root.popleft()) # 자식노드 1 넣기
#                 queue.append(root.popleft())
#                 print(queue)
#             elif root[0] is not None and root[1] is None:
#                 queue.append(root.popleft())
#                 root.popleft() # None 은 제거
#                 print(queue)
#             elif root[0] is None and root[1] is not None:
#                 root.popleft() # None 제거
#                 queue.append(root.popleft())
#                 print(queue)
#             elif root[0] is None and root[1] is None:
#                 root.popleft()
#                 root.popleft()
#
#     # BFS 반복횟수 == 깊이
#     return depth
#
#
# print(maxDepth(tree))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
from idlelib.tree import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ans = 0
        deq = deque()
        if root:
            deq.append((root, 1))

        while deq:
            (n, h) = deq.pop()
            ans = max(ans, h)
            if n.left is not None:
                deq.append((n.left, h + 1))
            if n.right is not None:
                deq.append((n.right, h + 1))

        return ans