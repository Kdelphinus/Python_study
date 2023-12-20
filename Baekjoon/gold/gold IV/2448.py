import sys

INPUT = sys.stdin.readline
sys.setrecursionlimit(10**8)
STAR_LIST = ["  *  ", " * * ", "*****"]


def dot_star():
    matrix = []
    base_line = len(STAR_LIST) * 2 - 1
    blank = base_line // 2 + 1
    for star in STAR_LIST:
        matrix.append(" " * blank + star + " " * blank)
    for star in STAR_LIST:
        matrix.append(star + " " + star)

    return matrix


if __name__ == "__main__":
    N = int(INPUT())
    K = 0

    while N != 3:
        N //= 2
        K += 1

    for _ in range(K):
        STAR_LIST = dot_star()

    for STAR in STAR_LIST:
        print(STAR)
