import sys

input = sys.stdin.readline


n1, n2 = input().split()
result = 0
for i in n1:
    for j in n2:
        result += int(i) * int(j)
print(result)
