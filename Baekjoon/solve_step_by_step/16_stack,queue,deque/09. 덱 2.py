"""28279 덱 2"""
import sys
from collections import deque

INPUT = sys.stdin.readline

deq = deque()
n = int(INPUT())
for _ in range(n):
    order = list(map(int, INPUT().split()))
    if order[0] == 1:
        deq.appendleft(order[1])
    elif order[0] == 2:
        deq.append(order[1])
    elif order[0] == 3:
        print(deq.popleft() if deq else -1)
    elif order[0] == 4:
        print(deq.pop() if deq else -1)
    elif order[0] == 5:
        print(len(deq))
    elif order[0] == 6:
        print(0 if deq else 1)
    elif order[0] == 7:
        print(deq[0] if deq else -1)
    elif order[0] == 8:
        print(deq[-1] if deq else -1)
    else:
        print("order error")
