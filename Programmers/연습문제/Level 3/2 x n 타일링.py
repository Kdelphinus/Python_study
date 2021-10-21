"""연습문제"""
import sys

sys.setrecursionlimit(10 ** 8)
MOD = 1000000007


def solution(n):
    memo = [-1 for _ in range(n + 1)]

    def dp(n):
        if memo[n] != -1:
            return memo[n]

        if n <= 1:
            return 1

        # 가로 길이가 n일 때 = n - 1일 때 + n - 2일 때
        memo[n] = (dp(n - 1) + dp(n - 2)) % MOD

        return memo[n]

    return dp(n)


# ----------------------------------------------------------------
"""재귀를 쓰지 않고 메모라이제이션"""
MOD = 1000000007


def solution(n):
    a, b = 1, 1
    for i in range(1, n):
        a, b = b, (a + b) % MOD
    return b
