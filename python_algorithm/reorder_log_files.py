# 로그를 재 정렬 하기!
from typing import List

# 입력값
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# 최종 출력값!
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]


def reorder_log_files(logs: List[str]) -> None:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
 
    return letters + digits


print(reorder_log_files(logs))
