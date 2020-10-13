def profile (age, name, *languages):
    print("이름 : {0}\t 나이 : {1}\t ".format(name, age), end=" ")
    for lang in languages:
        print("사용 가능한 언어 : {0}".format(lang))


print(29, "김요한", "Javascript", "Python", "Swift")


