import sys
from collections import deque

INPUT = sys.stdin.readline
DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))


def bfs(n: int, start: tuple, nations: list, key: int, left: int, right: int) -> int:
    cnt, total, queue = (
        1,
        nations[start[1]][start[0]],
        deque([(start[0], start[1], nations[start[1]][start[0]])]),
    )
    origin = nations[start[1]][start[0]]
    nations[start[1]][start[0]] = key

    while queue:
        x, y, v = queue.popleft()

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < n
                and 0 <= ny < n
                and nations[ny][nx] >= 0
                and left <= abs(v - nations[ny][nx]) <= right
            ):
                queue.append((nx, ny, nations[ny][nx]))
                total += nations[ny][nx]
                nations[ny][nx] = key
                cnt += 1
    if cnt == 1:
        nations[start[1]][start[0]] = origin
    return -1 if cnt == 1 else total // cnt


def immigration(n: int, nations: list, left: int, right: int) -> int:
    cnt = 0

    while True:
        key, population = -1, dict()
        for y, row in enumerate(nations):
            for x, i in enumerate(row):
                if i >= 0:
                    value = bfs(n, (x, y), nations, key, left, right)
                    if value == -1:
                        continue
                    population[key] = value
                    key -= 1
        if key == -1:
            return cnt
        for y, row in enumerate(nations):
            for x, i in enumerate(row):
                if i < 0:
                    nations[y][x] = population[i]
        cnt += 1


if __name__ == "__main__":
    N, L, R = map(int, INPUT().split())
    NATIONS = [list(map(int, INPUT().split())) for _ in range(N)]
    print(immigration(N, NATIONS, L, R))
