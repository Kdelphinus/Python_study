# 링크: https://cijbest.tistory.com/21

MOD = 10007


def tiling(n: int):
    if n == 1:
        return n

    prev, curr = 1, 3
    for _ in range(n - 2):
        prev, curr = curr, (curr + prev * 2) % MOD
    return curr % MOD


if __name__ == "__main__":
    n = int(input())
    print(tiling(n))
