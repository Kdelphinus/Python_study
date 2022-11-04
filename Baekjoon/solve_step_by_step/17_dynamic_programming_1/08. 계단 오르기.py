"""2579 계단 오르기"""

n = int(input())  # 계단의 개수
scores = []  # 점수들을 담을 리스트
for _ in range(n):
    temp = int(input())
    scores.append(temp)

if n <= 2:  # 계단이 2개 이하면 다 밟는 것이 최댓값
    print(sum(scores))
else:
    dp = [scores[0], scores[1] + scores[0]]  # 인덱스 위치 계단까지 올라갔을 때, 가지는 최댓값
    dp.append(max(scores[2] + scores[1], dp[0] + scores[2]))

    for i in range(3, n):
        # max(직전 계단을 밟고 i - 3번째에 가지는 최댓값 더하기, 직전 계단을 밟지 않고 i - 2번째에 가지는 최댓값 더하기)
        dp.append(max(scores[i] + scores[i - 1] + dp[i - 3], scores[i] + dp[i - 2]))

    print(dp[n - 1])
