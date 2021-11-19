"""
* 구간합
sum[idx] : idx까지의 총 합
start ~ end까지의 합 : sum[end] - sum[start - 1]
"""

import sys
input = sys.stdin.readline

life, num = map(int, input().split())
account = list(map(int, input().split()))
dp = [0] * (life + 1)

for idx, money in enumerate(account, 1):
	dp[idx] = dp[idx - 1] + account[idx - 1]
	
for _ in range(num):
	start, end = map(int, input().split())
	print('+' + str(dp[end] - dp[start - 1]) if dp[end] - dp[start - 1] > 0 else str(dp[end] - dp[start - 1]))


# --------------------------------------------------------------------------------------------------

# 시간초과
life, num = map(int, input().split())
account = list(map(int, input().split()))

for _ in range(num):
	start, end = map(int, input().split())
	total = sum(account[start - 1:end])
	print('+' + str(total) if total > 0 else str(total))