"""연습문제 / 백준 23-6번 문제와 동일"""


def solution(n, money):
    dp = [0 for _ in range(n + 1)]  # dp[idx]: idx를 만들 경우의 수
    dp[0] = 1  # 동전 하나로 만들 수 있는 경우의 수를 위한 초기값

    for m in money:
        for i in range(1, n + 1):
            if m <= i:  # 동전보다 만들고자 하는 값이 같거나 커야 값을 만들 수 있다
                dp[i] += dp[i - m]  # 현재 동전을 뺀 가격을 만드는 경우의 수만큼 경우의 수 추가

    return dp[n]
