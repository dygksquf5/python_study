# 이해가 좀더 필요!!!!!! 문제 자체가 이해가 안가 일단....


def lengthOfLongestSubstring(s: str) -> int:
    used = {}
    max_length = start = 0
    for index, char in enumerate(s):
        # 이미 등장했던 문자라면 "start" 위치 갱친
        if char in used and start <= used[char]:
            start = used[char] + 1
        else: # 최대 부분 문자열 길이 갱신
            max_length = max(max_length, index - start + 1)

        # 현재 문자의 위치 삽입
        used[char] = index

    return max_length


print(lengthOfLongestSubstring("abcabcbb"))