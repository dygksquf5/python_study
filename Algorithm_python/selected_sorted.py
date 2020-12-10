array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

print(sorted(array))

# 만약 sort 사용 못할 때

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)

# 요렇게 해줘도 되징! 스와핑으로