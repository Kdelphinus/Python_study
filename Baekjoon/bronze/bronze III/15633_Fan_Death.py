n = int(input())
ans = 0
for i in range(1, int(n**0.5) + 1):
    if n % i == 0 and i != n // i:
        ans += i + n // i
    elif n % i == 0 and i == n // i:
        ans += i
print(ans * 5 - 24)
