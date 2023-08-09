"""2485 가로수"""
import sys

INPUT = sys.stdin.readline


def gcd(a: int, b: int) -> int:
    return gcd(b, a % b) if b else a


def planting_tree(n: int, street_tree: list) -> int:
    gcd_t = street_tree[1] - street_tree[0]
    for i in range(2, n):
        gcd_t = gcd(gcd_t, street_tree[i] - street_tree[i - 1])
    return (street_tree[-1] - street_tree[0]) // gcd_t - n + 1


if __name__ == "__main__":
    N = int(INPUT())
    STREET_TREE = sorted([int(INPUT()) for _ in range(N)])
    print(planting_tree(N, STREET_TREE))
