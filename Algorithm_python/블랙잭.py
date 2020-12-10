n, m = 5, 21

data = [5, 6, 7, 8, 9]

result = 0
length = len(data)

count = 0
for i in range(0, length):
    for j in range(i + 1, length):
        for k in range(i + 1, length):
            sum_value = data[i] + data[j] + data[k]
            if sum_value <= m:
                result = max(result, sum_value)

print(result)