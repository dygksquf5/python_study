def isValid(s: str) -> bool:
    stack = []
    table = {
        ")": "(",
        "}": "{",
        "]": "[",
    }

    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
        # 비어있는지도 확인해서 비어있을 때, true 최종적으로 뽑아내게 하기
    return len(stack) == 0


print(isValid(["(", ")", "{", "}", "[", "]"]))
