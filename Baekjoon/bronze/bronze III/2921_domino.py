n = int(input())
result = 3
up, down = 1, 1

for i in range(2, n + 1):
    up, down = up + i, i
    result += up + down * (i + 1)

print(result)
