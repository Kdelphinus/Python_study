t = int(input())
for _ in range(t):
    print(sorted(map(int, input().split()), reverse=True)[2])
