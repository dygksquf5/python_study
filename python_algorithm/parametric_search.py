array = [19, 15, 10, 17]

# 4개, 그리고 6cm 를 가져가고 싶어 함 !
n, m = 4, 6

start = 0
end = max(array)

result = 0

# 머리좀 잘 굴려라 .. 당 충전 하과 ... 시작이 end 보다 작거나 같을동안 계속 진행하는거다 요한아 ㅠ 생각좀 ㅠㅠ하
while start <= end:
    print(start," : " ,end )
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1


print(result)