curr = list(map(int, input().split()))
chess = [1, 1, 2, 2, 2, 8]
ans = [a - b for a, b in zip(chess, curr)]
print(*ans)
