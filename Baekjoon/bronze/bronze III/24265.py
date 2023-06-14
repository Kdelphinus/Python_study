def man_of_passion(lst: list, n: int) -> int:
    total = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            total = total + lst[i] * lst[j]
    return total


n = int(input())
ans = 0
for i in range(1, n):
    ans += i
print(ans)
print(2)
