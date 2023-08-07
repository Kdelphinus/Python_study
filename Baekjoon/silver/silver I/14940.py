import sys
from collections import deque

INPUT = sys.stdin.readline
DIRECTION = ((0, 1), (1, 0), (0, -1), (-1, 0))


def bfs(x: int, y: int) -> None:
    queue = deque()
    queue.append([x, y, 0])
    DIST[y][x] = 1
    while queue:
        px, py, cnt = queue.popleft()
        for dx, dy in DIRECTION:
            nx, ny = px + dx, py + dy
            if 0 <= nx < M and 0 <= ny < N:
                if DIST[ny][nx] == -1 and MAP[ny][nx] != 0:
                    queue.append([nx, ny, cnt + 1])
                    DIST[ny][nx] = cnt + 1


def find_goal() -> tuple:
    for y in range(N):
        for x in range(M):
            if MAP[y][x] == 2:
                return x, y


def fill_zero_and_goal() -> None:
    for y in range(N):
        for x in range(M):
            if MAP[y][x] == 0 or MAP[y][x] == 2:
                DIST[y][x] = 0


if __name__ == "__main__":
    N, M = map(int, INPUT().split())
    MAP = [list(map(int, INPUT().split())) for _ in range(N)]
    gx, gy = find_goal()
    DIST = [[-1 for _ in range(M)] for _ in range(N)]
    bfs(gx, gy)
    fill_zero_and_goal()
    for ROW in DIST:
        print(*ROW)
