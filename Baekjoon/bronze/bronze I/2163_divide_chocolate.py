n, m = map(int, input().split())
print(min(m - 1 + (n - 1) * m, n - 1 + (m - 1) * n))
