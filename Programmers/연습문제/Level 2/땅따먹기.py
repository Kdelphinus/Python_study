"""연습문제"""


def solution(land):
    dp = [[0] * 4 for _ in range(len(land))]
    for i in range(4):
        dp[0][i] = land[0][i]

    for i in range(1, len(land)):
        dp[i][0] = land[i][0] + max(dp[i - 1][1], dp[i - 1][2], dp[i - 1][3])
        dp[i][1] = land[i][1] + max(dp[i - 1][0], dp[i - 1][2], dp[i - 1][3])
        dp[i][2] = land[i][2] + max(dp[i - 1][1], dp[i - 1][0], dp[i - 1][3])
        dp[i][3] = land[i][3] + max(dp[i - 1][1], dp[i - 1][2], dp[i - 1][0])

    return max(dp[-1])


print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))  # 16

# -----------------------------------------------------------------------------------------
"""슬라이싱을 통하여 간단하게"""


def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i - 1][:j] + land[i - 1][j + 1 :]) + land[i][j]

    return max(land[-1])
