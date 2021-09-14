"""10844 쉬운 계단 수"""

num = int(input())
dp = [[0] * 10 for i in range(num)]

for i in range(1, 10):
    dp[0][i] = 1

# i: 자리 수 - 1, j: 앞에 오는 숫자
for i in range(1, num):
    for j in range(10):
        if j == 9:  # 10은 뒤에 들어갈 수 없다
            dp[i][j] = dp[i - 1][j - 1]
        elif j == 0:  # -1은 뒤에 들어갈 수 없다
            dp[i][j] = dp[i - 1][j + 1]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[num - 1]) % 1000000000)
