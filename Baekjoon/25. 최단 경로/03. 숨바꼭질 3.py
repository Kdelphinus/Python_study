"""13549 숨바꼭질 3"""
# 나중에 추가되어 문제 번호가 겹침
# 실마리: https://my-coding-notes.tistory.com/415
# 2배로 갈 수 있는 곳을 왜 한 번에 찾으려 했을까

import heapq

INF = float("inf")


def dijkstra(now):
    dp[now] = 0
    heapq.heappush(heap, (0, now))

    while heap:
        weight, curr = heapq.heappop(heap)

        if dp[curr] < weight:
            continue

        if curr * 2 <= 100000 and dp[curr * 2] > weight:
            dp[curr * 2] = weight
            heapq.heappush(heap, (weight, curr * 2))

        if curr + 1 <= 100000 and dp[curr + 1] > weight + 1:
            dp[curr + 1] = weight + 1
            heapq.heappush(heap, (weight + 1, curr + 1))

        if curr - 1 >= 0 and dp[curr - 1] > weight + 1:
            dp[curr - 1] = weight + 1
            heapq.heappush(heap, (weight + 1, curr - 1))


subin, sister = map(int, input().split())
dp = [INF] * 100001
heap = []

dijkstra(subin)
print(dp[sister])

###################################################################################

# queue를 사용한 풀이
# dijkstra보다 약간 더 빠르다
# https://velog.io/@aonee/%EB%B0%B1%EC%A4%80-boj-13549-%EC%88%A8%EB%B0%94%EA%BC%AD%EC%A7%883-%ED%8C%8C%EC%9D%B4%EC%8D%AC

from collections import deque


def bfs(now):
    queue = deque()
    queue.append(now)
    check[now] = 1
    dist[now] = 0

    while queue:
        curr = queue.popleft()
        if curr * 2 <= 100000 and check[curr * 2] == 0:
            queue.appendleft(curr * 2)
            check[curr * 2] = 1
            dist[curr * 2] = dist[curr]
        if curr + 1 <= 100000 and check[curr + 1] == 0:
            queue.append(curr + 1)
            check[curr + 1] = 1
            dist[curr + 1] = dist[curr] + 1
        if curr - 1 >= 0 and check[curr - 1] == 0:
            queue.append(curr - 1)
            check[curr - 1] = 1
            dist[curr - 1] = dist[curr] + 1


check = [0] * 100001
dist = [-1] * 100001

subin, sister = map(int, input().split())
bfs(subin)
print(dist[sister])
