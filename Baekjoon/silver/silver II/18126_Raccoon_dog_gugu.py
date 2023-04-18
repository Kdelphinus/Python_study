import sys
from collections import deque


INPUT = sys.stdin.readline


def hide_ice_cream(n: int, s: int, road: list) -> int:
    queue = deque()
    queue.append(s)
    visited = [False for _ in range(n + 1)]
    dp = [0 for _ in range(n + 1)]
    while queue:
        curr = queue.popleft()
        visited[curr] = True
        for e, d in road[curr]:
            if not visited[e] and dp[e] < dp[curr] + d:
                dp[e] = dp[curr] + d
                queue.append(e)
    return max(dp)


if __name__ == "__main__":
    N = int(INPUT())
    ROAD = [list() for _ in range(N + 1)]
    for _ in range(N - 1):
        start, end, dist = map(int, INPUT().split())
        ROAD[start].append((end, dist))
        ROAD[end].append((start, dist))
    print(hide_ice_cream(N, 1, ROAD))
