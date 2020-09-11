cabinet = {3: "유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

# print(cabinet.get(5, "사용가능"))
# print(cabinet[5])
print("hi")
print(cabinet.get(5, "사용가능"))

print(3 in cabinet)
print(5 in cabinet)

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
 
 #새손님
print(cabinet)
cabinet["A-3"] = "조세호"
cabinet["ㅊ-4"] = "김요한"
print(cabinet)

#간 손님
del cabinet["A-3"]
print(cabinet)

#key 들만 출력

print(cabinet.keys())

#value 들만 출력
print(cabinet.values())

#key, value 쌍으로 출력
print(cabinet.items())

#목욕탕 폐점
cabinet.clera()
print(cabinet)
