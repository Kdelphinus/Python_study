def cupcake() -> int:
    n = int(input())
    m = int(input())
    return n * 8 + m * 3


if __name__ == "__main__":
    total = cupcake()
    print(total - 28 if total >= 28 else 0)
