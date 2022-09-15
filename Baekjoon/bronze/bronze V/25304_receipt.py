prices = int(input())
n = int(input())
ans = 0
for _ in range(n):
    a, b = map(int, input().split())
    ans += a * b
print("Yes" if ans == prices else "No")
