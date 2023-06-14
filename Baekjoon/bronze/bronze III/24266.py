def men_of_passion(lst: list, n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                total = total + lst[i] * lst[j] * lst[k]
    return total


n = int(input())
print(n ** 3)
print(3)
