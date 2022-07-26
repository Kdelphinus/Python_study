t = int(input())
for _ in range(t):
    n = int(input())
    market = sorted(list(map(int, input().split())))
    mean = round(sum(market) / n)
    print((mean - market[0] + market[-1] - mean) * 2)
