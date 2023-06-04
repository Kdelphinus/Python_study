N, M = map(int, input().split())
basket = [i for i in range(1, N + 1)]
for _ in range(M):
    i, j = map(int, input().split())
    basket = basket[: i - 1] + list(reversed(basket[i - 1 : j])) + basket[j:]
print(*basket)
