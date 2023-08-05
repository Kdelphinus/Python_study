"""11279 최대 힙"""
import heapq
import sys

input = sys.stdin.readline

num = int(input())
heap = []
for _ in range(num):
    order = int(input())

    if order == 0:
        if heap:
            print(heapq.heappop(heap)[1])  # 원래 값만 출력한다
        else:
            print(0)  # 값이 없으면 0을 출력
    else:
        heapq.heappush(heap, (-order, order))  # 주어진 숫자를 (음수변환, 원래값)으로 힙에 저장
