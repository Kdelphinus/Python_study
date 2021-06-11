"""1520 내리막 길"""
import sys

sys.setrecursionlimit(10 ** 8)  # 파이썬 재귀 깊이 제한을 10 ** 8로 설정
input = sys.stdin.readline

n, m = map(int, input().split())  # n x m
trip_map = [list(map(int, input().split())) for _ in range(n)]  # 지도

dp = [[-1] * m for _ in range(n)]
dp[n - 1][m - 1] = 1  # 도착지점
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 오른쪽, 왼쪽, 위, 아래


def find_downhill(x, y, trip_map, dp):
    """도착지점에서 출발지점으로 가는 길을 찾는 방식으로 작동하는 함수"""
    if dp[y][x] != -1:  # 이미 지나갔던 길이면 그 길에서 도착지점까지 갈 수 있는 수를 리턴
        return dp[y][x]

    tmp = 0
    for d in dxy:
        nx, ny = x + d[0], y + d[1]
        # nx, ny가 인덱스 범위 내에 있고 전에 있던 계단보다 낮을 때
        if 0 <= nx < m and 0 <= ny < n and trip_map[y][x] > trip_map[ny][nx]:
            # trip_map[y][x]를 지나 도착지점까지 갈 수 있는 길의 개수를 세줌
            tmp += find_downhill(nx, ny, trip_map, dp)
    dp[y][x] = tmp

    return dp[y][x]


print(find_downhill(0, 0, trip_map, dp))
