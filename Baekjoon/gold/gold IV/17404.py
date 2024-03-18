import sys
from typing import List

INPUT = sys.stdin.readline
INF = float("inf")


def paint_house(n: int, rgb: List[List[int]]) -> int:
    ans = INF
    for i in range(3):
        dp = [[INF, INF, INF] for _ in range(n)]
        dp[0][i] = rgb[0][i]

        # RGB 색칠 최솟값 구하기
        for j in range(n - 1):
            dp[j + 1][0] = min(dp[j][1], dp[j][2]) + rgb[j + 1][0]
            dp[j + 1][1] = min(dp[j][0], dp[j][2]) + rgb[j + 1][1]
            dp[j + 1][2] = min(dp[j][1], dp[j][0]) + rgb[j + 1][2]

        # 첫 번째 집과 겹치지 않는 색에서 최솟값 구하기
        for k in range(3):
            if i == k:
                continue
            ans = min(ans, dp[-1][k])

    return ans


if __name__ == "__main__":
    N, RGB = int(INPUT()), list()
    for _ in range(N):
        RGB.append(list(map(int, INPUT().split())))
    print(paint_house(N, RGB))
