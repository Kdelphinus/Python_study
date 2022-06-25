import sys

INPUT = sys.stdin.readline


def sail(n: int, islands: list):
    y_coor = []
    for x, y in islands:
        y_coor.append(y)
    dp = [0] * n
    for ei, ey in enumerate(y_coor):
        for si, sy in enumerate(y_coor[:ei]):
            if sy >= ey:
                dp[si] += 1
    return sum(dp)


def main():
    t = int(INPUT())
    for _ in range(t):
        n = int(INPUT())
        islands = [tuple(map(int, INPUT().split())) for i in range(n)]
        islands.sort(key=lambda x: (x[0], -x[1]))
        print(sail(n, islands))


if __name__ == "__main__":
    main()
