"""11866 요세푸스 문제 0"""
import sys
from collections import deque

num, k = map(int, sys.stdin.readline().split())  # 인원 수와 사람을 빼는 순서를 받는다
queue = deque([x for x in range(1, num + 1)])  # 사람이 저장된 큐
anw = []  # 빠지는 순서가 저장되는 리스트

while queue:  # 큐에 사람이 남아있다면
    for _ in range(k - 1):  # k번째 전까진 맨 뒤에 다시 저장
        queue.append(queue.popleft())

    anw.append(queue.popleft())  # k번째 사람은 빼고 답에 저장

# 예제 출력을 위한 코드
print("<", end="")
for i in range(num):
    if i == num - 1:
        print(anw[i], end="")
    else:
        print(f"{anw[i]},", end=" ")
print(">")