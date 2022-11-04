"""11054 가장 긴 바이토닉 부분 수열"""

n = int(input())
sequence = list(map(int, input().split()))
increase = [0 for _ in range(n)]
decrease = [0 for _ in range(n)]
dp = [0 for _ in range(n)]

# 증가 수열의 최대 길이를 구한다
for i in range(n):
    for j in range(i):
        if sequence[i] > sequence[j] and increase[i] < increase[j]:
            increase[i] = increase[j]
    increase[i] += 1

# 뒤에서부터 시작하는 증가 수열의 최대 길이를 구한다
# 결국 해당 인덱스부터 시작하는 감소 수열의 길이를 구하는 것과 같다
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if sequence[i] > sequence[j] and decrease[i] < decrease[j]:
            decrease[i] = decrease[j]
    decrease[i] += 1

# 증가 수열과 감소 수열을 더하여 1을 빼면(현 인덱스 중복 방지)
# 현 인덱스를 최댓값으로 하는 바이토닉 수열의 길이가 나온다
for i in range(n):
    dp[i] = increase[i] + decrease[i] - 1

print(max(dp))

# ----------------------------------------------------------------------------------------
"""2021.08.06, c++을 풀어보고 풀어보는 풀이"""
# 걸리는 시간은 비슷하다, 허나 더 간단하고 보기 편하다
import sys

input = sys.stdin.readline


def lbs(num, arr):
    incre = [1] * num
    decre = [1] * num

    for i in range(1, num):
        for j in range(i):
            if arr[i] > arr[j]:
                incre[i] = max(incre[i], incre[j] + 1)
            elif arr[i] < arr[j]:
                decre[i] = max(decre[i], decre[j] + 1, incre[j] + 1)

    return max(max(incre), max(decre))


num = int(input())
arr = list(map(int, input().split()))
print(lbs(num, arr))
