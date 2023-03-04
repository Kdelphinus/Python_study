import sys

INF = float("inf")
INPUT = sys.stdin.readline


def min_coin(dp: list, i: int) -> int:
    min_cnt = INF
    for j in (1, 2, 5, 7):
        min_cnt = min(min_cnt, 1 + dp[i - j])
    return min_cnt


def coin_cnt(n: int) -> int:
    if n == 0:
        return 0
    dp = [INF for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i] = 1 if i in (1, 2, 5, 7) else min_coin(dp, i)
    return int(dp[n])


if __name__ == "__main__":
    print(coin_cnt(int(input())))
