"""28278 스택 2"""
import sys

INPUT = sys.stdin.readline


# 연습 목적으로 객체 생성
class Stack:
    def __init__(self):
        self.__lst = list()

    def push(self, n: int) -> None:
        self.__lst.append(n)

    def pop(self) -> int:
        return self.__lst.pop() if self.__lst else -1

    def size(self) -> int:
        return len(self.__lst)

    def empty(self) -> int:
        return 0 if self.__lst else 1

    def top(self) -> int:
        return self.__lst[-1] if self.__lst else -1


N = int(INPUT())
stack = Stack()
for _ in range(N):
    order = list(map(int, INPUT().split()))
    if order[0] == 1:
        stack.push(order[1])
    elif order[0] == 2:
        print(stack.pop())
    elif order[0] == 3:
        print(stack.size())
    elif order[0] == 4:
        print(stack.empty())
    elif order[0] == 5:
        print(stack.top())
    else:
        print("Wrong command!")
