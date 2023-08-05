"""2559 수열"""
import sys

input = sys.stdin.readline

total_day, days = map(int, input().split())
temperature = list(map(int, input().split()))
prefix_sum = [0]
max_temp = -float("inf")  # 무조건 0이 최소값은 아니다

for temp in temperature:
    prefix_sum.append(temp + prefix_sum[-1])

for i in range(days, total_day + 1):
    max_temp = max(prefix_sum[i] - prefix_sum[i - days], max_temp)

print(max_temp)
