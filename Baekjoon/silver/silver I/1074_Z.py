import sys

sys.setrecursionlimit(10 ** 8)


def find_position(N: int, r: int, c: int, start: int):
    if N == 1:
        if r % 2 == 0 and c % 2 == 0:
            print(start)
        elif r % 2 == 0:
            print(start + 1)
        elif c % 2 == 0:
            print(start + 2)
        else:
            print(start + 3)

    side = (2 ** N) / 2
    if side > r and side > c:
        find_position(N - 1, r % side, c % side, start)
    elif side > r:
        find_position(N - 1, r % side, c % side, start + side ** 2)
    elif side > c:
        find_position(N - 1, r % side, c % side, start + (side ** 2) * 2)
    else:
        find_position(N - 1, r % side, c % side, start + (side ** 2) * 3)


if __name__ == "__main__":
    N, r, c = map(int, input().split())
    find_position(N, r, c, 0)
