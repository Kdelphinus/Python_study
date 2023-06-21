"""2164 카드2"""
import sys
from collections import deque

num = int(sys.stdin.readline().rstrip())  # 카드 개수
queue = [x for x in range(1, num + 1)]  # 카드 초기화
queue = deque(queue)  # 남은 카드를 저장할 큐

while len(queue) > 1:  # 1장이 남을 때까지 반복
    queue.popleft()  # 처음은 버리고
    queue.append(queue.popleft())  # 두 번째는 맨 밑으로 내린다

print(queue[0])
