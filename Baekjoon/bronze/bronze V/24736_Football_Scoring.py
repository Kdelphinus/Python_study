scoring = [6, 3, 2, 1, 2]
a = [scoring[i] * n for i, n in enumerate(list(map(int, input().split())))]
b = [scoring[i] * n for i, n in enumerate(list(map(int, input().split())))]
print(f"{sum(a)} {sum(b)}")
