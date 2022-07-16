n = int(input())
total, flag = 0, 0
result = list(map(int, input().split()))
for r in result:
    if r == 1:
        flag += 1
        total += flag
    else:
        flag = 0
print(total)
