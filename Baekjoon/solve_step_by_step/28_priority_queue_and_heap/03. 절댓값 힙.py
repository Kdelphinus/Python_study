"""11286 절댓값 힙"""
import heapq
import sys

input = sys.stdin.readline
num = int(input())
heap = []

for _ in range(num):
    order = int(input())

    if order == 0:
        if heap:
            print(heapq.heappop(heap)[1])  # 최소 절댓값 중 최소 원본값을 제거 및 출력
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(order), order))  # (절댓값, 원본값)을 한 쌍으로 힙에 저장
