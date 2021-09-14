"""2565 전깃줄"""

num = int(input())  # 두 전봇대 사이 전깃줄의 개수
wires = sorted(
    [(list(map(int, input().split()))) for _ in range(num)]
)  # 두 전봇대 사이 연결된 전깃줄 리스트, 시작점을 기준으로 오름차순 정렬
wires = [wires[i][1] for i in range(num)]  # 전깃줄이 도착하는 지점만 리스트에 저장

dp = [0 for _ in range(num)]

# 전깃줄이 도착하는 지점들로 가장 긴 증가하는 부분 수열의 길이를 구한다
for i in range(num):
    for j in range(i):
        if wires[i] > wires[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

# 가장 긴 증가하는 부분 수열이 최소 전깃줄만 제거한 결과이다
print(num - max(dp))
