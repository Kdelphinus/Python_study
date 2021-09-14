"""18258 큐 2"""
import sys
from collections import deque


def push(n):
    """정수 n을 큐에 넣는 함수"""
    queue.append(n)


def pop():
    """큐 맨 앞에 있는 정수를 빼고 출력하는 함수"""
    return queue.popleft() if queue else -1


def size():
    """큐에 들어있는 정수의 개수를 출력하는 함수"""
    return len(queue)


def empty():
    """큐가 비어있는지 확인하는 함수"""
    return 0 if queue else 1


def front():
    """큐의 가장 앞자리 정수를 출력"""
    return queue[0] if queue else -1


def back():
    """큐의 가장 뒷자리 정수를 출력"""
    return queue[-1] if queue else -1


num = int(sys.stdin.readline().rstrip())
queue = deque()

for _ in range(num):
    orders = sys.stdin.readline().rstrip().split()
    order = orders[0]

    if order == "push":
        push(orders[1])
    elif order == "pop":
        print(pop())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    elif order == "front":
        print(front())
    elif order == "back":
        print(back())
    else:
        print("잘못된 명령어입니다.")