max_v = -1
position = [0, 0]
for i in range(9):
    tmp = list(map(int, input().split()))
    if max_v < max(tmp):
        max_v = max(tmp)
        position = [i + 1, tmp.index(max_v) + 1]
print(max_v)
print(*position)
