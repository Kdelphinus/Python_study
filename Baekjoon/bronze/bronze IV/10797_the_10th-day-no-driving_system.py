cnt = 0
day = int(input())
car = list(map(int, input().split()))
for c in car:
    if c == day:
        cnt += 1
print(cnt)
