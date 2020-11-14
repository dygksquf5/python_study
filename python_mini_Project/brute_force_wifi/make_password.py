with(open("expect_password.txt", "w", encoding="utf8")) as text:
    a = "twosome"
    b = range(0,1000)
    for i in b:
        text.write("{0}{1} \n".format(a, i))
