"""1912 연속합"""

n = int(input())
n_list = list(map(int, input().split()))
dp = [0] * n
dp[0] = n_list[0]  # 길이가 1일 땐 그 값이 최댓값이 된다

for i in range(1, n):
    # 직전까지 최댓값 + 현재값과 현재값 중 큰 것을 값으로 가진다
    dp[i] = max(dp[i - 1] + n_list[i], n_list[i])

# 연속합 중 가장 큰 값을 출력
print(max(dp))
