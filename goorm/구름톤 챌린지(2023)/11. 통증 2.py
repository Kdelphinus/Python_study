def painkiller(n, a, b):
    dp = [float("inf") for _ in range(n + 1)]
    dp[0] = 0
    for i in range(n + 1):
        if i - a >= 0:
            dp[i] = min(dp[i], dp[i - a] + 1)
        if i - b >= 0:
            dp[i] = min(dp[i], dp[i - b] + 1)

    return -1 if dp[n] == float("inf") else dp[n]


if __name__ == "__main__":
    N = int(input())
    A, B = map(int, input().split())
    print(painkiller(N, A, B))