from typing import List


class Solution:
    def Temperature(self, T: List) -> List:
        answer = [0] * len(T)
        stack = []

        for i, cur in enumerate(T):
            # 현재 온도가 스택 값보다 높다면 정답처리
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer


t = Solution()
print(t.Temperature([73,74,75,71,69,72,76,73]))