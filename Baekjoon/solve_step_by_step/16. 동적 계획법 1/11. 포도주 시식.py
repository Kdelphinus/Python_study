"""2156 포도주 시식"""

n = int(input())

wine = []
for _ in range(n):
    wine.append(int(input()))

if n < 3:
    print(sum(wine))
else:
    dp = [wine[0], wine[0] + wine[1]]  # 초기값
    dp.append(
        max(wine[0] + wine[1], wine[1] + wine[2], wine[2] + wine[0])
    )  # 세번째 잔에서 최댓값, 여기서도 이번 잔을 안 마신 것을 고려해야 함

    # 현재 있는 잔을 마실 때 최댓값을 리스트에 저장
    for i in range(3, n):
        dp.append(
            max(
                wine[i] + wine[i - 1] + dp[i - 3],  # 이번 잔 + 전 잔
                wine[i] + dp[i - 2],  # 이번 잔 + 전전 잔
                dp[i - 1],  # 전 잔
            )
        )

    print(dp[n - 1])
