import sys, copy

input = sys.stdin.readline


def stickers():
    n = int(input())
    score = [list(map(int, input().split())) for _ in range(2)]
    if n == 1:
        return max(max(score[0]), max(score[1]))
    dp = copy.deepcopy(score)
    dp[0][1] += score[1][0]
    dp[1][1] += score[0][0]
    if n == 2:
        return max(max(dp[0]), max(dp[1]))
    dp[0][2] += max(dp[1][1], dp[1][0])
    dp[1][2] += max(dp[0][1], dp[0][0])
    for i in range(3, n):
        dp[0][i] += max(
            score[1][i - 1] + dp[0][i - 2], dp[1][i - 2], score[1][i - 1] + dp[0][i - 3]
        )
        dp[1][i] += max(
            score[0][i - 1] + dp[1][i - 2], dp[0][i - 2], score[0][i - 1] + dp[1][i - 3]
        )
    return max(max(dp[0]), max(dp[1]))


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(stickers())
