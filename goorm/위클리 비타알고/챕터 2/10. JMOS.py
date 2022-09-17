# LIS문제
num = int(input())
process = list(map(int, input().split()))
dp = [1 for _ in range(num)]

for i in range(1, num):
    for j in range(i):
        if process[i] > process[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(num - max(dp))
