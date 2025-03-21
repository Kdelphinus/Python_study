import sys, heapq

INF = float("inf")
INPUT = sys.stdin.readline


def shortest_path(start: int, n: int) -> list[float]:
    heap = []
    dp = [INF] * (n + 1)
    dp[start] = 0
    heapq.heappush(heap, (0, start))  # weight, node

    while heap:
        weight, now = heapq.heappop(heap)

        if dp[now] < weight:
            continue

        for next_node, next_weight in GRAPH[now]:
            next_weight += weight
            if next_weight < dp[next_node]:
                dp[next_node] = next_weight
                heapq.heappush(heap, (next_weight, next_node))

    return dp


if __name__ == "__main__":
    N, M = map(int, INPUT().split())
    GRAPH = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B, C = map(int, INPUT().split())
        GRAPH[A].append((B, C))
        GRAPH[B].append((A, C))
    DP = shortest_path(1, N)
    print(DP[N])
