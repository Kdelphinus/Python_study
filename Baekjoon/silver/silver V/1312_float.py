def print_float(u: int, d: int, n: int) -> int:
    if u % d == 0:
        return 0

    for _ in range(n):
        u = u % d * 10

    return u // d


if __name__ == "__main__":
    A, B, N = map(int, input().split())
    print(print_float(A, B, N))
