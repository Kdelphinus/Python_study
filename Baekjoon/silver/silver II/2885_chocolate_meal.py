K = int(input())
choco, cnt = 1, 0
while choco < K:
    choco *= 2
print(choco, end=" ")
while K % choco / 2:
    choco /= 2
    cnt += 1
print(cnt)
