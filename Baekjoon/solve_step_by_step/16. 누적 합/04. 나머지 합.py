"""10986 나머지 합"""
import sys

input = sys.stdin.readline

num, divide = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
cnt = 0

for number in numbers:
    prefix_sum.append(number + prefix_sum[-1])

for i in range(num + 1):
    for j in range(i + 1, num + 1):
        if (prefix_sum[j] - prefix_sum[i]) % divide == 0:
            cnt += 1

print(cnt)
