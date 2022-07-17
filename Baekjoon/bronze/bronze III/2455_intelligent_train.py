train = 0
max_train = 0
for _ in range(4):
    out_n, in_n = map(int, input().split())
    train -= out_n
    train += in_n
    max_train = max(max_train, train)
print(max_train)
