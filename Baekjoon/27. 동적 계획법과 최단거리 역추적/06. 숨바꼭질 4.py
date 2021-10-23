"""13913 숨바꼭질 4"""
from collections import deque


def BFS(start, goal):
    if start == goal:
        return

    queue = deque()
    queue.append(start)
    dp[start] = [start]

    while queue:
        size = len(queue)

        for _ in range(size):
            current = queue.popleft()
            if current + 1 <= 100000:
                if dp[current + 1] and len(dp[current + 1]) > len(dp[current]) + 1:
                    dp[current + 1] = dp[current] + [current + 1]
                    queue.append(current + 1)
                elif len(dp[current + 1]) == 0:
                    dp[current + 1] = dp[current] + [current + 1]
                    queue.append(current + 1)
            if 0 <= current - 1:
                if dp[current - 1] and len(dp[current - 1]) > len(dp[current]) + 1:
                    dp[current - 1] = dp[current] + [current - 1]
                    queue.append(current - 1)
                elif len(dp[current - 1]) == 0:
                    dp[current - 1] = dp[current] + [current - 1]
                    queue.append(current - 1)
            if current * 2 <= 100000:
                if dp[current * 2] and len(dp[current * 2]) > len(dp[current]) + 1:
                    dp[current * 2] = dp[current] + [current * 2]
                    queue.append(current * 2)
                elif len(dp[current * 2]) == 0:
                    dp[current * 2] = dp[current] + [current * 2]
                    queue.append(current * 2)
        dp[current].clear()

        if goal in queue:
            return


start, goal = map(int, input().split())
dp = [[] for _ in range(100001)]
BFS(start, goal)
print(len(dp[goal]) - 1)
print(*dp[goal])
