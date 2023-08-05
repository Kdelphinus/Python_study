"""9370 미확인 도착지"""

import heapq as hp
import sys

input = sys.stdin.readline
INF = float("inf")


def dijkstra(start, road_num, roads):
    """dijkstra 출발 지점부터 교차로를 가는데 걸리는 최단거리를 구하는 함수

    Args:
        start (int): 출발 지점
        road_num (int): 도로의 개수
        roads (2d_list): 교차로마다 연결된 도로와 거리를 저장한 리스트

    Returns:
        dp (list): 각 교차로로 가는데 걸리는 최단 거리를 저장한 리스트
    """
    dp = [INF for _ in range(crossroad_num + 1)]
    dp[start] = 0
    heap = []
    hp.heappush(heap, [start, 0])

    while heap:
        now, weight = hp.heappop(heap)

        if weight > dp[now]:  # 현재 저장한 것과 비교하여 now에 갈 수 있는 가중치보다 더 큰 가중치면 무시
            continue

        for next, next_weight in roads[now]:
            next_weight += weight
            if dp[next] > next_weight:
                dp[next] = next_weight
                hp.heappush(heap, [next, next_weight])

    return dp


def find_destination(crossroad_num, road_num, goal_num, start, waypoint1, waypoint2):
    """find_destination 하나의 도로를 반드시 지나갈 때 목적지로 도착하는 거리가 출발지에서 도착지로 바로가는 최단 거리와 같은 도착지를 찾는 함수

    Args:
        crossroad_num (int): 교차로의 개수
        road_num (int): 도로의 개수
        goal_num (int): 예비 목적지의 개수
        start (int): 출발 지점
        waypoint1 (int): 반드시 지나가야 할 교차로1
        waypoint2 (int): 반드시 지나가야 할 교차로2

    Returns:
        target_goals (list): 최단 거리와 교차로를 지났을 때 거리가 같은 목적지를 저장한 리스트
    """
    roads = [[] for _ in range(crossroad_num + 1)]  # 교차로마다 연결된 도로와 그 거리를 저장한 리스트
    goals = []  # 예비 목적지를 저장할 리스트
    for _ in range(road_num):  # 양방향 통행이 가능
        point1, point2, weight = map(int, input().split())
        roads[point1].append([point2, weight])
        roads[point2].append([point1, weight])
    for _ in range(goal_num):
        goals.append(int(input()))

    # 각 지점에서 각 교차로로 도착하는 최단 거리를 저장한 리스트
    start_dp = dijkstra(start, road_num, roads)
    waypoint1_dp = dijkstra(waypoint1, road_num, roads)
    waypoint2_dp = dijkstra(waypoint2, road_num, roads)

    target_goals = []  # 조건에 부합하는 목적지만 저장할 리스트
    for goal in goals:
        cnt = min(
            start_dp[waypoint1]
            + waypoint1_dp[waypoint2]
            + waypoint2_dp[goal],  # start -> waypoint1 -> wqypoint2 -> goal
            start_dp[waypoint2]
            + waypoint2_dp[waypoint1]
            + waypoint1_dp[goal],  # start -> waypoint2 -> wqypoint1 -> goal
        )
        # 경로가 연결되지 않은 후보지는 INF로 남아있기에 INF도 제외해야 함
        if (
            cnt == start_dp[goal] and cnt < INF
        ):  # 교차로를 거쳐 목적지에 도착한 거리와 출발지점에서 목적지까지 최단 거리가 같다면
            target_goals.append(goal)

    return target_goals


test = int(input())
for _ in range(test):
    crossroad_num, road_num, goal_num = map(int, input().split())
    start, waypoint1, waypoint2 = map(int, input().split())
    roads = [[] for i in range(road_num + 1)]
    target_goals = find_destination(
        crossroad_num, road_num, goal_num, start, waypoint1, waypoint2
    )
    target_goals.sort()  # 오름차순
    for target_goal in target_goals:
        print(target_goal, end=" ")
    print()
