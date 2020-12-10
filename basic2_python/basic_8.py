
scores = {"수학" : 0, "영어" : 50, "과학" : 100}

for subject, score in scores.items():
    print(subject.ljust(5), str(score).rjust(4), sep=" : ")


print()
print()


for num in range(1,21):
    print("대기번호 {0}번 ".format(str(num).zfill(3)))