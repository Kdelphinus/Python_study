MOD = 10007


def tiling(n: int):
    if n <= 3:
        return n

    prev, curr = 2, 3
    for _ in range(n - 3):
        prev, curr = curr, (curr + prev) % MOD
    return curr


if __name__ == "__main__":
    n = int(input())
    print(tiling(n))
