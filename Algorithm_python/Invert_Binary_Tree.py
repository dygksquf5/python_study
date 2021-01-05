from idlelib.tree import TreeNode
import collections


# 재귀방식으로 풀기
def invertTree(root: TreeNode):
    if root:
        root.left, root.right = \
            invertTree(root.right), invertTree(root.left)
        return root
    return None  # 사실 파이썬에선 이거 생략해도 오류를 안내지만, 좀더 정석적인 코드를 위해!


# 반복구조로 BFS
def invertTree(root: TreeNode):
    queue = collections.deque([root])

    while queue:
        node = queue.popleft()
        # 부모 노드부터 하향식 스왑
        if node:
            node.left, node.right = node.right, node.left

            queue.append(node.left)
            queue.append(node.right)

    return root


# 반복구조로 DFS
def invertTree(root: TreeNode):
    stack = collections.deque([root])

    while stack:
        node = stack.pop()
        # 부모 노드부터 하향식 스왑
        if node:
            node.left, node.right = node.right, node.left

            stack.append(node.left)
            stack.append(node.right)

    return root

