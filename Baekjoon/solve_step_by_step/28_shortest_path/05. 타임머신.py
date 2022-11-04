"""11657 타임머신"""

import sys

input = sys.stdin.readline
INF = float("inf")  # '무한 - 실수'는 무한이나 sys.maxsize로 구한 INF는 실수이므로 float('inf')를 사용해야함


def bellman_ford(start):
    """bellman_ford 음수 가중치가 있어도 최단 거리를 구할 수 있는 함수

    Args:
        start (int): 출발하는 도시

    Returns:
        -1 (int): 음수 사이클(반복할수록 거리가 짧아지는 경우)일 경우 무한 루프 방지를 위해 -1 출력
        dp (list): start에서 각 도시로 가는 최단 거리가 저장된 리스트
    """
    dp = [INF for _ in range(city_num + 1)]
    dp[start] = 0  # 출발 지점 거리는 0

    for _ in range(city_num - 1):  # 각 노드 간 최단 거리는 '도시 개수 - 1'만큼  나올 수 있다
        for waypoint in range(1, city_num + 1):  # 각 도시에서 갈 수 있는 도시까지의 최단 거리를 구하기 위해
            for end, time in bus_routes[waypoint]:  # waypoint에서 갈 수 있는 도시와 걸리는 시간
                if dp[end] > dp[waypoint] + time:  # 만약 저장된 시간보다 더 빨리 도착할 수 있는 루트가 있다면
                    dp[end] = dp[waypoint] + time  # 최단 거리 최신화

    # 음수 사이클이 있는지 확인
    # 음수 사이클이 있으면 최단 거리를 찾는 계산을 반복할수록 최단 거리가 작아지는 무한 루프 발생
    for waypoint in range(1, city_num + 1):
        for end, time in bus_routes[waypoint]:
            # 출발 도시에서 가지 못하는 도시는 inf이므로 시간을 더하거나 빼도 그대로 inf
            if dp[end] > dp[waypoint] + time:
                return False

    return dp


city_num, bus_route_num = map(int, input().split())
bus_routes = [[] for _ in range(city_num + 1)]
start_city = 1
for _ in range(bus_route_num):
    start, end, time = map(int, input().split())
    bus_routes[start].append([end, time])

dist = bellman_ford(start_city)
if dist == False:  # 음수 사이클이 존재할 때
    print(-1)
else:  # 음수 사이클이 존재하지 않을 때
    for i in range(1, city_num + 1):
        if i != start_city:  # 출발 도시는 출력하지 않음
            print(dist[i] if dist[i] < INF else -1)
