"""1956 운동"""
# 플로이드 와셜을 이용, PyPy3을 이용해야 함
# 링크: https://pacific-ocean.tistory.com/280

INF = float("inf")


def floyd_warshall(town_num, road_num):
    """floyd_warshall 다시 출발지점으로 돌아가는 가장 짧은 거리를 구하는 함수

    Args:
        town_num (int): 마을의 개수
        road_num (int): 거리의 개수

    Returns:
        (int): 다시 출발지점으로 돌아가는 가장 짧은 거리 or 불가할 땐 -1
    """
    roads = [[INF] * town_num for _ in range(town_num)]
    for _ in range(road_num):
        start, end, dist = map(int, input().split())
        roads[start - 1][end - 1] = dist

    for way_p in range(town_num):  # 경유지
        for start in range(town_num):  # 출발지점
            for end in range(town_num):  # 도착지점
                # 현재 도착지점까지 가는 거리보다 경유지를 들려서 가는 것이 더 짧을 때
                if roads[start][end] > roads[start][way_p] + roads[way_p][end]:
                    roads[start][end] = roads[start][way_p] + roads[way_p][end]

    # 다시 출발지점으로 돌아가는 거리 중 가장 짧은 것을 구한다
    answer = INF
    for i in range(town_num):
        answer = min(answer, roads[i][i])

    return -1 if answer == INF else answer


town_num, road_num = map(int, input().split())
print(floyd_warshall(town_num, road_num))
