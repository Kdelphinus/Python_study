def find_password(n, m):
    if 2 ** (m - 1) > n:
        return 0

    dp = [[0] * (n + 1) for _ in range(m)]
    for i in range(m):
        for j in range(2 ** i, n + 1):
            dp[i][j] = (
                1
                if j == 2 ** i
                else dp[i][j - 1] + (1 if i == 0 else dp[i - 1][j // 2])
            )
            dp[i][j] %= 1000000007

    return dp[m - 1][n]


n, m = map(int, input().split())
print(find_password(n, m))
