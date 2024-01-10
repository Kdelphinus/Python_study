import sys

INPUT = sys.stdin.readline
MAX_NUM = 1000001
MOD_NUM = 1000000009


def count_num() -> list[int]:
    dp = [0] * MAX_NUM
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, MAX_NUM):
        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD_NUM
    return dp


if __name__ == "__main__":
    N = int(INPUT())
    DP = count_num()
    for _ in range(N):
        NUM = int(INPUT())
        print(DP[NUM])
