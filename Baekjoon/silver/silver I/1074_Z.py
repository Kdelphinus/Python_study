import sys

sys.setrecursionlimit(10 ** 8)


def find_position(n: int, r: int, c: int, start: int):
    if n == 1:
        if r % 2 == 0 and c % 2 == 0:
            return start
        elif r % 2 == 0:
            return start + 1
        elif c % 2 == 0:
            return start + 2
        else:
            return start + 3

    side = 2 ** n // 2
    if side > r and side > c:
        return find_position(n - 1, r % side, c % side, start)
    elif side > r:
        return find_position(n - 1, r % side, c % side, start + side ** 2)
    elif side > c:
        return find_position(n - 1, r % side, c % side, start + side ** 2 * 2)
    else:
        return find_position(n - 1, r % side, c % side, start + side ** 2 * 3)


if __name__ == "__main__":
    n, r, c = map(int, input().split())
    print(find_position(n, r, c, 0))
