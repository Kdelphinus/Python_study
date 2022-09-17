import heapq


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append([b, 1])
        graph[b].append([a, 1])

    heap = []
    heapq.heappush(heap, [1, 0])
    dp = [float("inf") for i in range(n + 1)]
    dp[0], dp[1] = 0, 0

    while heap:
        now, weight = heapq.heappop(heap)

        if dp[now] < weight:
            continue

        for next_node, next_weight in graph[now]:
            next_weight += weight
            if dp[next_node] > next_weight:
                dp[next_node] = next_weight
                heapq.heappush(heap, [next_node, next_weight])

    return dp.count(max(dp))
