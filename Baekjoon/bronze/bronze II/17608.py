import sys
INPUT = sys.stdin.readline


stack = []
for _ in range(int(INPUT())):
    num = int(INPUT())
    while stack and stack[-1] <= num:
        stack.pop()
    stack.append(num)
print(len(stack))
