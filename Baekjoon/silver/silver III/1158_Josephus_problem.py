from collections import deque

solution = "<"
n, k = map(int, input().split())
circle = deque([i for i in range(1, n + 1)])
while circle:
    for _ in range(k - 1):
        tmp = circle.popleft()
        circle.append(tmp)
    tmp = circle.popleft()
    if circle:
        solution += str(tmp) + ", "
    else:
        solution += str(tmp) + ">"
print(solution)
