"""12789 도키도키 간식드리미"""

from collections import deque


def solution(people: deque) -> str:
    stack, check = [], 0
    while people:
        if check + 1 == people[0]:
            check += 1
            people.popleft()
        elif stack and check + 1 == stack[-1]:
            check += 1
            stack.pop()
        elif not stack or (stack and stack[-1] > people[0]):
            stack.append(people.popleft())
        else:
            return "Sad"
    while stack and stack.pop() == check + 1:
        check += 1
    return "Sad" if stack else "Nice"


if __name__ == "__main__":
    N = int(input())
    print(solution(deque(list(map(int, input().split())))))
