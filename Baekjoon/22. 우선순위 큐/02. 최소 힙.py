"""1927 최소 힙"""
import sys
import heapq

input = sys.stdin.readline
num = int(input())
heap = []

for _ in range(num):
    order = int(input())

    if order == 0:
        if heap:
            print(heapq.heappop(heap))  # 최솟값을 빼고 출력
        else:
            print(0)  # 값이 없다면 0출력
    else:
        heapq.heappush(heap, order)  # 힙 속성을 유지하며 입력
