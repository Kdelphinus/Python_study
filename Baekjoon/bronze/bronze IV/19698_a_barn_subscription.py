N, W, H, L = map(int, input().split())
max_n = (W // L) * (H // L)
print(min(N, max_n))
