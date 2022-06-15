"""10773 제로"""
import sys

count = int(sys.stdin.readline().rstrip())  # 입력받을 횟수
stack = []

for _ in range(count):
    num = int(sys.stdin.readline().rstrip())

    if num == 0:  # 0이면 가장 최근 값을 뺌
        stack.pop()
    else:  # 아니면 추가
        stack.append(num)

print(sum(stack))