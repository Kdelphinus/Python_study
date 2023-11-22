import sys
from collections import deque

INPUT = sys.stdin.readline
DIRECTION = ((0, 1), (0, -1), (1, 0), (-1, 0))


def find_route(wolf: tuple) -> None:
    """
    늑대가 갈 수 있는 곳을 찾는 함수
    Args:
        wolf: 늑대가 시작하는 위치
    """
    queue = deque([wolf])
    VISITED[wolf[1]][wolf[0]] = True
    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTION:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < M
                and 0 <= ny < N
                and not VISITED[ny][nx]
                and BOARD[ny][nx] != "#"
            ):
                while 0 <= nx < M and 0 <= ny < N and BOARD[ny][nx] == "+":
                    nx += dx
                    ny += dy
                if BOARD[ny][nx] == "#":
                    VISITED[ny][nx] = True
                    nx -= dx
                    ny -= dy
                if not VISITED[ny][nx]:
                    VISITED[ny][nx] = True
                    queue.append((nx, ny))


if __name__ == "__main__":
    N, M = map(int, INPUT().split())
    GRASSLAND, BOARD = [], []
    VISITED = [[False for _ in range(M)] for __ in range(N)]
    WOLVES = []
    for Y in range(N):
        tmp = list(INPUT().strip())
        for X in range(M):
            if tmp[X] == "W":
                WOLVES.append((X, Y))
            elif tmp[X] == ".":
                GRASSLAND.append((X, Y))
        BOARD.append(tmp)
    for WOLF in WOLVES:
        find_route(WOLF)
    for Y in range(N):
        for X in range(M):
            if not VISITED[Y][X] and BOARD[Y][X] == ".":
                BOARD[Y][X] = "P"

    for B in BOARD:
        print("".join(B))
