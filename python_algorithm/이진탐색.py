def binary_serach(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_serach(array, target, start, mid - 1)
    else:
        return binary_serach(array, target, mid + 1, end)


list_num = [0, 2, 4, 5, 7, 8, 14, 16, 17, 18, 22, 44, 66, 88, 99, 198]
print(binary_serach(list_num, 22, 0, len(list_num) - 1))



