def center_move(n: int) -> int:
    d, a = 2, 1
    for _ in range(n):
        d += a
        a *= 2
    return d**2


if __name__ == "__main__":
    print(center_move(int(input())))
