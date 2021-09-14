"""1021 회전하는 큐"""
import sys
from collections import deque

size, num = map(int, sys.stdin.readline().split())  # 덱에 들어갈 정수와 뽑고 싶은 수의 개수
numbers = deque(list(map(int, sys.stdin.readline().split())))  # 뽑고 싶은 수
my_deque = deque([x for x in range(1, size + 1)])  # 주어진 덱
cnt = 0  # 연산 횟수

while numbers:
    if my_deque[0] == numbers[0]:  # 뽑고 싶은 수일 때
        my_deque.popleft()
        numbers.popleft()
    else:
        find_index = my_deque.index(numbers[0])
        if find_index > len(my_deque) // 2:  # 뽑고 싶은 수가 오른쪽 방향으로 더 가까울 때
            temp = my_deque.pop()
            my_deque.appendleft(temp)
            cnt += 1
        else:  # 뽑고 싶은 수가 왼쪽 방향으로 더 가까울 때
            temp = my_deque.popleft()
            my_deque.append(temp)
            cnt += 1

print(cnt)
