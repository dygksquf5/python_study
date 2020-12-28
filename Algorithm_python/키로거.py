

test_case = 2


d = '<<BP<A>>Cd-','ThIsIsS3Cr3t'

for n in range(test_case):

    left_stack = []
    right_stack = []
    data = d[n]

    for i in data:
        if i == '-':
            if left_stack:
                left_stack.pop()
        elif i == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(i)

    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))