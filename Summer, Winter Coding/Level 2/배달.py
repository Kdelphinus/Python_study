"""Summer, Winter Coding(~2018)"""
import heapq

INF = float("inf")


def solution(N, roads, K):
    answer = 0
    heap = []
    dp = [INF for _ in range(N + 1)]
    graph = [[] for _ in range(N + 1)]
    for road in roads:
        graph[road[0]].append([road[1], road[2]])
        graph[road[1]].append([road[0], road[2]])

    def dijkstra(start_town):
        dp[start_town] = 0
        heapq.heappush(heap, [start_town, 0])

        while heap:
            now, weight = heapq.heappop(heap)

            if dp[now] > weight:
                continue

            for next_town, next_weight in graph[now]:
                next_weight += weight
                if next_weight < dp[next_town]:
                    dp[next_town] = next_weight
                    heapq.heappush(heap, [next_town, next_weight])

    dijkstra(1)
    for i in dp:
        if i <= K:
            answer += 1

    return answer


print(
    solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3)
)  # 4
print(
    solution(
        6,
        [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]],
        4,
    )
)  # 4
