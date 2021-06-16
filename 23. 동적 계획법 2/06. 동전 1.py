"""2293 동전 1"""
""" 
목표를 달성할 수 있는 경우의 수 = 현재 코인을 쓰지 않고 목표를 달성한 경우의 수 + 현재 코인만 쓰면 목표를 달성한 경우의 수
여기서 메모리를 절약하기 위해 1차원 리스트에 덮어씌워 계산을 이어감
해답: https://pacific-ocean.tistory.com/200"""
import sys

input = sys.stdin.readline


def coin(k, coins):
    """coin

    Args:
        k (int): 동전을 조합하여 만들 금액
        coins (list): 동전의 종류가 담긴 리스트
        dp (list): 동전을 조합하여 index를 만들 경우의 수가 담긴 리스트
    """
    for coin in coins:  # 동전 하나씩 계산
        for j in range(1, k + 1):  # 1부터 원하는 값까지
            if j - coin >= 0:  # 원하는 값이 코인보다 같거나 커야 만들 가능성이 있다
                dp[j] += dp[j - coin]  # 현 코인을 더하면 값이 만들어지는 경우의 수와 일치


n, k = map(int, input().split())  # 동전의 개수, 만들고자 하는 가격
dp = [0 for _ in range(k + 1)]  # dp[i]: i를 만들 수 있는 경우의 수
dp[0] = 1  # 0원과 더하는 경우(동전 하나로 금액을 달성하는 경우)를 위하여
coins = []
for _ in range(n):
    coins.append(int(input()))

coin(k, coins)
print(dp[k])
