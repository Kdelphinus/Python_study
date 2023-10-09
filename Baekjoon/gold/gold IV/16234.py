import sys

INPUT = sys.stdin.readline
DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))


def check_border_line(n: int, nations: list, left: int, right: int) -> (bool, list):
    flag, border_line = False, [[0 for _ in range(n)]]
    for y in range(n):
        for x in range(n):
            if y + 1 < n and left <= abs(nations[y + 1][x] - nations[y][x]) <= right:
                flag = True
                border_line[y][x] = 1
                border_line[y + 1][x] = 1
            if x + 1 < n and left <= abs(nations[y][x + 1] - nations[y][x]) <= right:
                flag = True
                border_line[y][x] = 1
                border_line[y][x + 1] = 1
    return flag, border_line


def bfs() -> None:
    pass


def immigration(n: int, nations: list, left: int, right: int) -> int:
    cnt = 0
    flag, boarder_line = check_border_line(n, nations, left, right)
    if not flag:
        return cnt


if __name__ == "__main__":
    N, L, R = map(int, INPUT().split())
    NATIONS = [list(map(int, INPUT().split())) for _ in range(N)]
    print(immigration(N, NATIONS, L, R))
