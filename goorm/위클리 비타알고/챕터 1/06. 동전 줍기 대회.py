# 백준 15-15와 동일한 문제
num = int(input())
coins = list(map(int, input().split()))
dp = [0] * num
dp[0] = coins[0]

for idx, coin in enumerate(coins[1:], 1):
	dp[idx] = max(coin + dp[idx - 1], coin)

print(max(dp))
	