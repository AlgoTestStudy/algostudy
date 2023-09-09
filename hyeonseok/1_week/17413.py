import sys
s = sys.stdin.readline().strip() + ' '
stack = [] # 스택
result = '' # 결과물 출력
cnt = 0 # 괄호 여부

for i in s:
    if i == '<':
        cnt = 1
        for _ in range(len(stack)):
            result += stack.pop()
    stack.append(i)

    if i == '>':
        cnt  = 0

        for _ in range(len(stack)):
            result += stack.pop(0)

    if i == ' ' and cnt == 0:
        stack.pop()
        for _ in range(len(stack)):
            result += stack.pop()
        result += ' '

print(result)