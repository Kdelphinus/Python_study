"""10866 덱"""
import sys
from collections import deque


def push_front(x):
    """정수 x를 맨 앞에 넣는 함수"""
    my_deque.appendleft(x)


def push_back(x):
    """정수 x를 맨 뒤에 넣는 함수"""
    my_deque.append(x)


def pop_front():
    """덱의 가장 앞 수를 뺴고 그 수를 출력하는 함수"""
    return my_deque.popleft() if my_deque else -1


def pop_back():
    """덱의 가장 뒤의 수를 빼고 그 수를 출력하는 함수"""
    return my_deque.pop() if my_deque else -1


def size():
    """덱에 들어있는 정수 개수를 출력하는 함수"""
    return len(my_deque)


def empty():
    """덱이 비어있는지 확인하는 함수"""
    return 0 if my_deque else 1


def front():
    """덱의 가장 앞 정수를 출력하는 함수"""
    return my_deque[0] if my_deque else -1


def back():
    """덱의 가장 뒤의 정수를 출력하는 함수"""
    return my_deque[-1] if my_deque else -1


num = int(sys.stdin.readline())
my_deque = deque()

for _ in range(num):
    orders = sys.stdin.readline().split()
    order = orders[0]

    if order == "push_back":
        push_back(orders[1])
    elif order == "push_front":
        push_front(orders[1])
    elif order == "pop_back":
        print(pop_back())
    elif order == "pop_front":
        print(pop_front())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    elif order == "front":
        print(front())
    elif order == "back":
        print(back())
    else:
        print("잘못된 명령어 입니다")
