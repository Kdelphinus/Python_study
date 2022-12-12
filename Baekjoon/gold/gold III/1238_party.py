import sys
from collections import deque

INF = float("inf")
INPUT = sys.stdin.readline


def dijkstra(s: int, num: int) -> list:
    queue = deque([(s, 0)])
    dp = [INF for _ in range(num + 1)]
    dp[s] = 0
    while queue:
        n, t = queue.popleft()

        if dp[n] < t:
            continue

        for e, t in GRAPH[n]:
            if dp[n] + t < dp[e]:
                dp[e] = dp[n] + t
                queue.append((e, t))

    return dp


if __name__ == "__main__":
    N, M, X = map(int, INPUT().split())
    GRAPH = [list() for _ in range(N + 1)]
    for _ in range(M):
        start, end, time = map(int, INPUT().split())
        GRAPH[start].append((end, time))

    go_home = dijkstra(X, N)
    for p in range(1, N + 1):
        if p == X:
            continue
        go_home[p] += dijkstra(p, N)[X]

    print(max(go_home[1:]))
