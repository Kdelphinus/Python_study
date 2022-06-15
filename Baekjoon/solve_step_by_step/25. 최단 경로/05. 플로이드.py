"""11404 플로이드"""

import sys

INF = float("inf")
input = sys.stdin.readline


def floyd_warshall():
    """floyd_warshall

    Returns:
        prices[start][end]: start에서 end까지 가는 최소 비용
    """
    prices = [[INF] * city_num for _ in range(city_num)]  # 최소 가격을 담는 배열

    # prices 초기화
    for start in range(city_num):
        for end in range(city_num):
            if start == end:  # 출발, 도착지가 같으면 비용이 없다
                prices[start][end] = 0
            else:
                prices[start][end] = bus_route[start][end]

    # 최소 가격 구하기
    for way_p in range(city_num):  # 경유지
        for start in range(city_num):  # 출발 도시
            for end in range(city_num):  # 도착 도시
                # 현재 저장된 가격보다 경유지를 거쳐 가는 것이 더 저렴하면 가격을 바꾼다
                if prices[start][end] > prices[start][way_p] + prices[way_p][end]:
                    prices[start][end] = prices[start][way_p] + prices[way_p][end]

    return prices


city_num = int(input())  # 도시의 개수
bus_num = int(input())  # 버스의 개수

# bus_route[i][j]: i에서 j로 갈 때 드는 비용
bus_route = [[INF] * city_num for _ in range(city_num)]

# 출발, 도착지가 같은 버스도 있기에 더 적은 비용만 저장한다
for _ in range(bus_num):
    start, end, value = map(int, input().split())
    bus_route[start - 1][end - 1] = min(value, bus_route[start - 1][end - 1])

prices = floyd_warshall()

for price in prices:
    for i in price:
        if i < INF:  # 갈 수 있을 때
            print(i, end=" ")
        else:  # 못 갈 때
            print(0, end=" ")
    print()
