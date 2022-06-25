"""11780 플로이드"""
import sys

INF = float("inf")
input = sys.stdin.readline


def floyd():
    # 같은 도시로 이동하는 비용은 0
    for i in range(1, city + 1):
        dp[i][i] = 0

    # 직행이 있는 루트는 직행 비용으로 초기화
    for start in range(1, city + 1):
        for price, end in routes[start]:
            if dp[start][end] > price:
                dp[start][end] = price
                visite[start][end] = [start, end]  # 루트 저장

    # 모든 루트를 돌며
    for way_p in range(1, city + 1):
        for start in range(1, city + 1):
            for end in range(1, city + 1):
                if dp[start][end] > dp[start][way_p] + dp[way_p][end]:
                    dp[start][end] = dp[start][way_p] + dp[way_p][end]
                    # 루트 최신화, 합칠 때 way_p가 중복되지 않도록 합치기
                    visite[start][end] = visite[start][way_p] + visite[way_p][end][1:]


city = int(input())  # 도시의 개수
buses = int(input())  # 버스의 개수
routes = [[] for _ in range(city + 1)]  # 버스 루트를 저장할 리스트
visite = [[[] for i in range(city + 1)] for _ in range(city + 1)]  # 방문한 도시를 저장할 리스트
dp = [[INF] * (city + 1) for _ in range(city + 1)]  # dp[s][e]: s에서 e까지 가는 최소비용
for _ in range(buses):
    start, end, price = map(int, input().split())
    routes[start].append([price, end])

floyd()

# 각 도시로 가는 최소 비용 출력
for i in range(1, city + 1):
    for j in range(1, city + 1):
        print(dp[i][j] if dp[i][j] < INF else 0, end=" ")
    print()

# 각 도시에서 다른 도시로 갈 때, 지나는 도시(출발, 도착 도시 포함)의 개수와 루트
for i in range(1, city + 1):
    for j in range(1, city + 1):
        if dp[i][j] == 0 or dp[i][j] == INF:
            print(0)
        else:
            print(len(visite[i][j]), *visite[i][j])
