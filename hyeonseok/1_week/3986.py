import sys

n = int(sys.stdin.readline())

cnt = 0

# 이전 글자가 다르면 안됨
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    stack = []

    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if not stack:
        cnt += 1

print(cnt)


