"""나의 풀이 / 백준 23-3 문제 참고"""
import sys

sys.setrecursionlimit(10**8)


def solution(m, n, puddles):
    maps = [[True] * m for _ in range(n)]
    dp = [[-1] * m for _ in range(n)]
    dp[n - 1][m - 1] = 1
    for x, y in puddles:
        maps[y - 1][x - 1] = False

    dxy = [[1, 0], [0, 1]]

    def __find_route(x, y):
        if dp[y][x] != -1:
            return dp[y][x]

        possible = 0
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == True:
                possible += __find_route(nx, ny)
        dp[y][x] = possible

        return dp[y][x]

    return __find_route(0, 0) % 1000000007


# ------------------------------------------------------------------------------------------------------

"""다른 풀이"""


def solution(m, n, puddles):
    grid = [[0] * (m + 1) for i in range(n + 1)]  # 왼쪽, 위로 한줄씩 만들어서 IndexError 방지
    if puddles != [[]]:  # 물이 잠긴 지역이 0일 수 있음
        for a, b in puddles:
            grid[b][a] = -1  # 미리 -1로 체크
    grid[1][1] = 1
    for j in range(1, n + 1):
        for k in range(1, m + 1):
            if j == k == 1:  # (1,1)은 1로 만들어두고, 0이 되지 않도록
                continue
            if grid[j][k] == -1:  # 웅덩이는 0으로 만들어 다음 덧셈 때 영향끼치지 않게
                grid[j][k] = 0
                continue
            grid[j][k] = (
                grid[j][k - 1] + grid[j - 1][k]
            ) % 1000000007  # [a,b] = [a-1,b] + [a,b-1] 공식

    return grid[n][m]
