"""10828 스택"""
# 제한 시간이 짧기 때문에 sys를 이용해야 함
import sys


def push(x):
    """정수 x를 스택에 넣는 함수"""
    stack.append(x)


def pop():
    """가장 위에 있는 정수를 빼고 그 수를 출력하는 함수"""
    if not stack:
        return -1

    return stack.pop()


def size():
    """스택에 들어있는 정수의 개수를 출력하는 함수"""
    return len(stack)


def empty():
    """스택이 비어있는지 확인하는 함수"""
    if len(stack) == 0:
        return 1
    else:
        return 0

    # comprehension 이용
    # return 0 if stack else 1


def top():
    """가장 위에 있는 정수를 출력하는 함수"""
    if len(stack) == 0:
        return -1

    return stack[-1]

    # comprehension 이용
    # return stack[-1] if stack else -1


num = int(sys.stdin.readline().rstrip())  # 명령의 수
stack = []

for _ in range(num):
    orders = sys.stdin.readline().rstrip().split()  # 입력값은 여러 개인데 받는 변수가 하나면 리스트로 저장
    order = orders[0]

    if order == "push":
        push(orders[1])
    elif order == "pop":
        print(pop())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    elif order == "top":
        print(top())
    else:
        print("잘못된 명령어입니다")
