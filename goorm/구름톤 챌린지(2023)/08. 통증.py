n = int(input())
cnt = 0
for i in (14, 7, 1):
    if n == 0:
        break
    cnt += n // i
    n %= i
print(cnt)
