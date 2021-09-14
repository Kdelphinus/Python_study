"""11053 가장 긴 증가하는 부분 수열"""

n = int(input())
sequence = list(map(int, input().split()))

# 현재 위치한 인덱스 값을 가질 때 만들 수 있는 최대 길이
dp = [1]  # 처음은 무조건 1

for i in range(1, n):
    max_dp = 0

    # 현재 위치 이전에 현재 값보다 작은 것이 있는 지 확인한다
    for j in range(i):
        if sequence[j] < sequence[i] and dp[j] > max_dp:
            max_dp = dp[j]  # 작은 것 중 리스트를 가장 많이 가질 수 있는 것을 추린다
    dp.append(max_dp + 1)

print(max(dp))  # 맨 마지막이 무조건 가장 큰 배열을 가지진 않으므로 최댓값을 뽑아준다


"""같은 방법, 다른 표기"""
# n = int(input())
# a = list(map(int, input().split()))
# dp = [0 for i in range(n)]
# for i in range(n):
#     for j in range(i):
#         if a[i] > a[j] and dp[i] < dp[j]:
#             dp[i] = dp[j]
#     dp[i] += 1
# print(max(dp))