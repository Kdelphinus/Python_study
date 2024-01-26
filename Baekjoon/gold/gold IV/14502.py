# Python은 느려서 PyPy를 사용해야 함

import sys
from collections import deque
from copy import deepcopy

INPUT = sys.stdin.readline
SAFE_AREA = 0
DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def cal_safe_area(board: list[list[int]]) -> None:
    """
    바이러스가 침입하지 못한 공간의 크기를 구하는 함수
    Args:
        board: 바이러스가 모두 침투한 후
    """
    global SAFE_AREA

    area = 0
    for b in board:
        area += b.count("0")
    SAFE_AREA = max(SAFE_AREA, area)


def bfs() -> None:
    """
    바이러스가 갈 수 있는 모든 공간을 찾는 함수
    """
    board = deepcopy(BOARD)
    queue = deque([v for v in VIRUS])
    while queue:
        y, x = queue.popleft()
        for dy, dx in DIRECTIONS:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == "0":
                queue.append((ny, nx))
                board[ny][nx] = "2"
    cal_safe_area(board)


def build_wall(cnt: int) -> None:
    """
    세울 수 있는 모든 경우의 수에 벽을 세우고 안전 공간을 계산하는 함수
    Args:
        cnt: 세운 벽의 개수
    """
    if cnt == 3:
        bfs()
        return

    for y in range(N):
        for x in range(M):
            if BOARD[y][x] == "0":
                BOARD[y][x] = "1"
                build_wall(cnt + 1)
                BOARD[y][x] = "0"


if __name__ == "__main__":
    N, M = map(int, INPUT().split())
    VIRUS, BOARD = [], []
    for i in range(N):
        tmp = list(INPUT().rstrip().split())
        for j, e in enumerate(tmp):
            if e == "2":
                VIRUS.append((i, j))
        BOARD.append(tmp)
    build_wall(0)
    print(SAFE_AREA)
