n, k = map(int, input().split())
factors = []
for i in range(1, n + 1):
    if n % i == 0:
        factors.append(i)
print(factors[k - 1] if len(factors) >= k else 0)
