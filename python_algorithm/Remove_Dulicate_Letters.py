# 추후 다시 공부하기!!!


class Solution:
    def removeDuplicateLetters(self, s: str)-> str:
        # 집합으로 먼저 정렬!
        for char in sorted(set(s)):
            # .index() 로 중복되는 인덱스는 제외하고 가장 먼저 있는 인덱스 값을 뽑아냄.
            suffix = s[s.index(char):]
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ""))
        return ""


a = Solution()
print(a.removeDuplicateLetters("cbacdcbc"))