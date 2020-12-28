

def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]


# parent = [i for i in range(5)]
parent = dict()
number = dict()
#
# union(1, 4)
# union(2, 4)

# for i in range(1, len(parent)):
#     print(find(i), end='')


x, y  = input().split(' ')
if x not in parent:
    parent[x] = x
    number[x] = 1
if y not in parent:
    parent[y] = y
    number[y] = 1

union(x, y)

print(number[find(x)])

