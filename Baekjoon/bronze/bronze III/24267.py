def men_of_passion(lst: list, n: int) -> int:
    total = 0
    for i in range(1, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                total = total + lst[i] * lst[j] * lst[k]
    return total


n = int(input())
print(n * (n - 1) * (n - 2) // 6)  # https://www.acmicpc.net/board/view/112232
print(3)
