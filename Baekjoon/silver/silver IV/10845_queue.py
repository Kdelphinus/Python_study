import sys
from collections import deque


queue = deque()
num = int(input())
for _ in range(num):
    orders = sys.stdin.readline().rstrip.split()
    order = orders[0]

    if order == "push":
        queue.append(int(orders[1]))
    elif order == "pop":
        print(queue.popleft() if len(queue) else -1)
    elif order == "size":
        print(len(queue))
    elif order == "empty":
        print(0 if len(queue) else 1)
    elif order == "front":
        print(queue[0] if len(queue) else -1)
    elif order == "back":
        print(queue[-1] if len(queue) else -1)
    else:
        print("wrong order")
