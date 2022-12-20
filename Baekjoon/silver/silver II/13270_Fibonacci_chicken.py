def init(n: int) -> None:
    for _ in range(n - 2):
        FIBO.append((FIBO[-1][0] + FIBO[-2][0], FIBO[-1][0]))


def chicken(n: int) -> tuple:
    return (1, 1)


if __name__ == "__main__":
    N = int(input())
    FIBO = [(1, 0), (2, 1)]
    init(N)
    print(*chicken(N))
