#자료구조의 변경 (중괄호{}는 집합, 즉 셋트)
menu ={"커피","우유","쥬스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))
# 즉 set = {}, list =[],  tuple=()

menu = set(menu)
print(menu, type(menu))
