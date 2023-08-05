"""11659 구간 합 구하기 4"""

import sys

input = sys.stdin.readline

num, cnt = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]

for number in numbers:
    prefix_sum.append(prefix_sum[-1] + number)

for _ in range(cnt):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i - 1])
