t = int(input())
for _ in range(t):
    idx, string = input().split()
    print(string[: int(idx) - 1] + string[int(idx) :])
