#정렬하기

num_list = [1,2,3,4,6,9,56]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

num_list.clear()
print(num_list)

# dictionary

cabinet = {3:"유재석",100:"김태호"}
print(cabinet[100])
print(cabinet.get(3))
print(cabinet.get(6),"사용가능한 key")
print(3 in cabinet) #true
print(7 in cabinet) #false
