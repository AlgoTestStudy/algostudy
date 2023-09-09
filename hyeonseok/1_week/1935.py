import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

stack = []
num_list = []

for i in range(n):
    num_list.append(int(sys.stdin.readline()))

# A+B*C-D/E
# ABC*+DE/-
for i in s:
    if 'A' <= i <= 'Z':
        stack.append(num_list[ord(i) - ord('A')])
    else:
        n2 = float(stack.pop())
        n1 = float(stack.pop())

        if i == '+':
            stack.append(n1+n2)
        if i == '-':
            stack.append(n1 - n2)
        if i == '*':
            stack.append(n1 * n2)
        if i == '/':
            stack.append(n1 / n2)

print('{:.2f}'.format(stack[0]))