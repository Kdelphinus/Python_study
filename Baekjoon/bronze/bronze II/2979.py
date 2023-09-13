import sys

INPUT = sys.stdin.readline

prices = [0] + list(map(int, INPUT().split()))
times = [0] * 101

for _ in range(3):
    s, e = map(int, INPUT().split())
    for i in range(s, e):
        times[i] += 1

ans = 0
for t in times:
    if t == 0:
        continue
    ans += prices[t] * t

print(ans)
