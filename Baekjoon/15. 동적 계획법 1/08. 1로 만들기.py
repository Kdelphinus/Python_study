"""1463 1로 만들기"""

num = int(input())  # 숫자를 받는다
dp = [0 for _ in range(num + 1)]  # 받은 숫자 크기만큼 0을 갖는 리스트를 만든다

# 2부터 주어진 숫자까지 횟수를 구한다
for i in range(2, num + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1

    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1

print(dp[num])
