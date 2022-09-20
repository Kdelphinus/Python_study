"""
큐 두 개를 이용해 푸는 방법으로 접근은 성공했으나 양쪽 힙에서 허수를 빼주는 과정을 실패
각 값마다 플래그를 세우는 방법으로 해결해야 함
https://neomindstd.github.io/%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4/boj7662/

다른 답안에 허수를 체크하는 과정을 dict을 이용하여 속도를 줄이는 방법도 있음
"""

import sys
import heapq


input = sys.stdin.readline


def dpq():
    n = int(input())
    max_heap, min_heap = [], []
    visited = [False] * n
    for i in range(n):
        order, num = input().split()
        if order == "I":
            heapq.heappush(max_heap, (-int(num), i))
            heapq.heappush(min_heap, (int(num), i))
            visited[i] = True
        elif int(num) == -1:
            while min_heap and not visited[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:
                visited[min_heap[0][1]] = False
                heapq.heappop(min_heap)
        else:
            while max_heap and not visited[max_heap[0][1]]:
                heapq.heappop(max_heap)
            if max_heap:
                visited[max_heap[0][1]] = False
                heapq.heappop(max_heap)

    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    print(f"{-max_heap[0][0]} {min_heap[0][0]}" if max_heap and min_heap else "EMPTY")


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        dpq()
