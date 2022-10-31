a, b = map(int, input().split())
print(0) if a - a * (b / 100) >= 100 else print(1)
