t = int(input())
print("Gnomes:")
for _ in range(t):
    height = list(map(int, input().split()))
    up, down = sorted(height), sorted(height, reverse=True)
    if height == up or height == down:
        print("Ordered")
    else:
        print("Unordered")
