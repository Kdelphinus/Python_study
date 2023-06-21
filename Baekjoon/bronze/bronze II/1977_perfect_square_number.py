m = int(input())
n = int(input())
start = int(m**0.5) if m == int(m**0.5) ** 2 else int(m**0.5) + 1
psn = []
while start <= n / start:
    psn.append(start**2)
    start += 1
if len(psn) == 0:
    print(-1)
else:
    print(sum(psn))
    print(psn[0])
