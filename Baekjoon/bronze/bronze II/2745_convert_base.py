N, B = input().split()
ans = 0
for n in N:
    ans *= int(B)
    ans += int(n) if n.isdigit() else ord(n) - ord("A") + 10
print(ans)
