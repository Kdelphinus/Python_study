"""1753 최단경로"""
# import sys
# import heapq
#
# INF = float("inf")  # 무한대
# input = sys.stdin.readline
#
#
# def dijkstra(start_node):
#     dp[start_node] = 0  # 시작 노드에서 시작 노드로 가는 길이는 0
#     heapq.heappush(heap, (0, start_node))  # 초기값 설정
#
#     while heap:  # heap이 빌 때까지 반복
#         weight, now = heapq.heappop(heap)  # 가중치와 현재 위치를 꺼낸다
#
#         if dp[now] < weight:  # 현재 가중치보다 더 크다면 바로 종료
#             continue
#
#         for w, next_node in graph[now]:  # 현재 위치와 연결된 노드들의 가중치와 연결 노드를 꺼낸다
#             next_weight = w + weight  # 시작 노드부터 다음 노드까지 가중치를 구한다
#             if next_weight < dp[next_node]:  # 이미 구한 다음 노드까지 가는 가중치보다 지금 구한 것이 작다면
#                 dp[next_node] = next_weight  # 가중치를 최신화하고
#                 heapq.heappush(heap, (next_weight, next_node))  # 다음 노드에 대한 탐색도 한다
#
#
# node_num, linked_num = map(int, input().split())  # 노드의 개수, 간선의 개수
# start_node = int(input())  # 시작 노드
# dp = [INF for _ in range(node_num + 1)]  # 시작 노드에서 인덱스 노드까지 가는데 걸리는 가중치
# heap = []  # 탐색할 노드와 가중치를 저장할 힙
# graph = [[] for _ in range(node_num + 1)]  # 각 노드에 연결된 노드들과 가중치를 저장할 리스트
#
# for _ in range(linked_num):  # 각 노드와 연결된 노드들을 저장
#     start, end, weight = map(int, input().split())
#     graph[start].append((weight, end))
#
# dijkstra(start_node)
#
# for i in range(1, node_num + 1):
#     print("INF" if dp[i] == INF else dp[i])


"""2022.03.18"""
import heapq
import sys

input = sys.stdin.readline
INF = float("inf")


def dijkstra(start_node):
    dp[start_node] = 0
    heapq.heappush(heap, (0, start_node))

    while heap:
        weight, now = heapq.heappop(heap)

        if dp[now] < weight:
            continue

        for w, next in graph[now]:
            next_weight = w + weight
            if next_weight < dp[next]:
                dp[next] = next_weight
                heapq.heappush(heap, (next_weight, next))


node_num, linked_num = map(int, input().split())
start_node = int(input())
dp = [INF for _ in range(node_num + 1)]
heap = []
graph = [[] for _ in range(node_num + 1)]

for _ in range(linked_num):
    start, end, weight = map(int, input().split())
    graph[start].append((weight, end))

dijkstra(start_node)

for i in range(1, node_num + 1):
    print("INF" if dp[i] == INF else dp[i])
