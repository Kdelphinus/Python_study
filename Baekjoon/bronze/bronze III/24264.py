def men_of_passion(lst: list, n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            total = total + lst[i] * lst[j]
    return total


n = int(input())
print(n ** 2)
print(2)