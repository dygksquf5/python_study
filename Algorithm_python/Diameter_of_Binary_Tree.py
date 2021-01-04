# 이진트리의 직경

# 이진트리에서 두 노드간 가장 긴 경로의 길이를 출력하기

# 상태값 누적 트리 DFS
# 가장 긴 경로 ㅊ작는방법은 가장 말단, 리프노드까지 탐색한다음 부모로 거슬로 올라가며 거리계산 상태 업데이트 해가기
from idlelib.tree import TreeNode


class Solution:
    longest: int = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node : TreeNode) -> int:
            if not node:
                return -1
            # 왼쪽, 오른쪽의 각 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 가장 긴 경로
            self.longest = max(self.longest, left + right + 2)
            # 상태값
            return max(left, right) + 1

        dfs(root)
        return self.longest


