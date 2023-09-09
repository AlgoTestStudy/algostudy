s = input().split()
stack = []


for i in s:
    if i[-1] in '<':
        print(i)
    if i[-1] in '>':
        print(i)
    else:
        rs = i[::-1]
        stack.append(rs)


# print(stack)
print(' '.join(stack))