import sys
from collections import deque

INPUT = sys.stdin.readline
DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))


def bfs() -> str | int:
    while QUEUE_FIRES:
        x, y = QUEUE_FIRES.popleft()

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy

            if 0 <= nx < C and 0 <= ny < R:
                if not VISIT_F[ny][nx] and MAZE[ny][nx] != "#":
                    VISIT_F[ny][nx] = VISIT_F[y][x] + 1
                    QUEUE_FIRES.append((nx, ny))

    while QUEUE_JIHOON:
        x, y = QUEUE_JIHOON.popleft()

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy

            if 0 <= nx < C and 0 <= ny < R:
                if MAZE[ny][nx] != "#" and not VISIT_J[ny][nx]:
                    if not VISIT_F[ny][nx] or VISIT_F[ny][nx] > VISIT_J[ny][nx] + 1:
                        VISIT_J[ny][nx] = VISIT_J[y][x] + 1
                        QUEUE_JIHOON.append((nx, ny))
            else:
                return VISIT_J[y][x]

    return "IMPOSSIBLE"


if __name__ == "__main__":
    R, C = map(int, INPUT().split())
    QUEUE_JIHOON, QUEUE_FIRES, MAZE = deque(), deque(), []
    VISIT_J = [[0 for _ in range(C)] for __ in range(R)]
    VISIT_F = [[0 for _ in range(C)] for __ in range(R)]
    for Y in range(R):
        tmp = list(INPUT().rstrip().strip())
        for X in range(C):
            if tmp[X] == "J":
                QUEUE_JIHOON.append((X, Y))
                VISIT_J[Y][X] = 1
            elif tmp[X] == "F":
                QUEUE_FIRES.append((X, Y))
                VISIT_F[Y][X] = 1
        MAZE.append(tmp)
    print(bfs())
