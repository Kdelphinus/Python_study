def change(money: int) -> list:
    c = [0, 0, 0, 0]
    for i, m in enumerate((25, 10, 5, 1)):
        c[i] = money // m
        money %= m
    return c


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(*change(int(input())))
