def equation() -> tuple:
    a, b, c, d, e, f = map(int, input().split())
    for y in range(-999, 1000):
        for x in range(-999, 1000):
            if a * x + b * y == c and d * x + e * y == f:
                return x, y
    return float("inf"), float("inf")


if __name__ == "__main__":
    print(*equation())
