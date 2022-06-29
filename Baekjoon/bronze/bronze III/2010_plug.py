import sys

input = sys.stdin.readline

n = int(input())
sum = 0
for _ in range(n - 1):
    sum += int(input()) - 1
sum += int(input())
print(sum)
