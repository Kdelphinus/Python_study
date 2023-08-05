"""1504 특정한 최단 경로"""
# import sys
# import heapq as hp
#
# input = sys.stdin.readline
# INF = float("inf")
#
#
# def dijkstra(start):
#     """최단경로를 구하는 함수"""
#     dp = [INF for _ in range(node_num + 1)]
#     dp[start] = 0
#     heap = []
#     hp.heappush(heap, [start, 0])
#
#     while heap:
#         now, weight = hp.heappop(heap)
#
#         if weight > dp[now]:  # 현재 저장한 것과 비교하여 now에 갈 수 있는 가중치보다 더 큰 가중치면 무시
#             continue
#
#         for next, next_weight in graph[now]:
#             next_weight += weight
#             if dp[next] > next_weight:
#                 dp[next] = next_weight
#                 hp.heappush(heap, [next, next_weight])
#
#     return dp
#
#
# node_num, linked_num = map(int, input().split())
# graph = [[] for _ in range(node_num + 1)]
# for _ in range(linked_num):  # 양방향 통행이 가능하기에 양쪽 다 넣어준다
#     start, end, weight = map(int, input().split())
#     graph[start].append([end, weight])
#     graph[end].append([start, weight])
#
# way1, way2 = map(int, input().split())
# one_dp = dijkstra(1)  # 1에서 출발할 때 최단거리가 담긴 리스트
# way1_dp = dijkstra(way1)  # way1에서 출발할 때 최단거리가 담긴 리스트
# way2_dp = dijkstra(way2)  # way2에서 출발할 때 최단거리가 담긴 리스트
#
# cnt = min(
#     one_dp[way1] + way1_dp[way2] + way2_dp[node_num],  # 1 -> way1 -> way2 -> n
#     one_dp[way2] + way2_dp[way1] + way1_dp[node_num],  # 1 -> way2 -> way1 -> n
# )
# print(cnt if cnt < INF else -1)  # INF보다 작으면 cnt 출력

#####################################################################################################
"""2022.03.18"""
import heapq
import sys

input = sys.stdin.readline
INF = float("inf")


def dijkstra(start_node):
    dp = [INF for _ in range(node_num + 1)]
    dp[start_node] = 0

    heap = []
    heapq.heappush(heap, (0, start_node))

    while heap:
        weight, now = heapq.heappop(heap)

        if dp[now] < weight:
            continue

        for w, next in graph[now]:
            next_weight = w + weight
            if dp[next] > next_weight:
                dp[next] = next_weight
                heapq.heappush(heap, (next_weight, next))

    return dp


node_num, linked_num = map(int, input().split())
graph = [[] for _ in range(node_num + 1)]
for _ in range(linked_num):
    start, end, weight = map(int, input().split())
    graph[start].append((weight, end))
    graph[end].append((weight, start))
way_p1, way_p2 = map(int, input().split())

start_path = dijkstra(1)
way_p1_path = dijkstra(way_p1)
way_p2_path = dijkstra(way_p2)

route1 = start_path[way_p1] + way_p1_path[way_p2] + way_p2_path[node_num]
route2 = start_path[way_p2] + way_p2_path[way_p1] + way_p1_path[node_num]

print(-1 if min(route1, route2) == INF else min(route1, route2))
