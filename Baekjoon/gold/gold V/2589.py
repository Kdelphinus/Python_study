import copy
import sys
from collections import deque

INPUT = sys.stdin.readline
DIRECTION = ((0, 1), (0, -1), (1, 0), (-1, 0))


def bfs(start: tuple, height: int, width: int, treasure: list) -> int:
    cnt = 0
    queue = deque([(start[0], start[1], cnt)])
    treasure[start[1]][start[0]] = "W"

    while queue:
        x, y, cnt = queue.popleft()

        for dx, dy in DIRECTION:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and treasure[ny][nx] == "L":
                treasure[ny][nx] = "W"
                queue.append((nx, ny, cnt + 1))

    return cnt


if __name__ == "__main__":
    ANS = 0
    HEIGHT, WIDTH = map(int, INPUT().split())
    TREASURE = [list(INPUT().rstrip().strip()) for _ in range(HEIGHT)]
    for Y, ROW in enumerate(TREASURE):
        for X, FACTOR in enumerate(ROW):
            if FACTOR == "L":
                ANS = max(ANS, bfs((X, Y), HEIGHT, WIDTH, copy.deepcopy(TREASURE)))
    print(ANS)
