import sys

input = sys.stdin.readline

n = int(input())
total = 0
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort()
start, end = lines[0][0], lines[0][1]
for s, e in lines[1:]:
    if end >= s and end < e:
        end = e
    elif end < s:
        total += abs(end - start)
        start, end = s, e
total += abs(end - start)
print(total)
