from math import comb


def combi(n: int, m: int) -> int:
    m = min(n - m, m)
    ans = 1
    for i in range(m):
        ans *= (n - i) // (i + 1)
    return ans


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(comb(n, m))
    print(combi(n, m))
