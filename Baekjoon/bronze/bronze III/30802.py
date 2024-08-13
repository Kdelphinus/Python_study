n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())
total = 0
for s in size:
    if s % t == 0:
        total += s // t
    else:
        total += s // t + 1

print(total)
print(n // p, n % p)
