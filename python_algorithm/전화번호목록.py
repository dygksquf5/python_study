# 내가한거
def solution(phone_book):
    phone = sorted(phone_book, key=len)
    length = len(phone[0])
    phone[1][0:length]
    answer = []
    for i in range(1, len(phone)):
        if phone[0] == phone[i][0:length]:
            return False

    return True


# 다른사람

def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer



def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True