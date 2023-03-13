def putting_the_ball(n: int, m: int) -> tuple:
    baskets = [0 for _ in range(n)]
    for _ in range(m):
        s, e, b = map(int, input().split())
        for i in range(s, e + 1):
            baskets[i - 1] = b
    return tuple(baskets)


if __name__ == "__main__":
    N, M = map(int, input().split())
    print(*putting_the_ball(N, M))
