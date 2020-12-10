sam = list(map(int, input().split(' ')))

a = 0
b = 0
for i in range(len(sam) - 1):
    if sam[i] < sam[i + 1]:
        a += 1
    elif sam[i] > sam[i + 1]:
        b += 1

if a == len(sam) - 1:
    print("acending")
elif b == len(sam) - 1:
    print("decending")
elif a or b != len(sam):
    print("mixed")