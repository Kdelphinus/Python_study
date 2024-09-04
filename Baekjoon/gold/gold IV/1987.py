# https://define-me.tistory.com/78
import sys

INPUT = sys.stdin.readline
DIRECTION = ((0, 1), (1, 0), (0, -1), (-1, 0))


def dfs(x: int, y: int, cnt: int) -> None:
    global MAX_CNT

    MAX_CNT = max(cnt, MAX_CNT)
    for dy, dx in DIRECTION:
        nx, ny = x + dx, y + dy
        if 0 <= ny < R and 0 <= nx < C and VISITED[ord(BOARD[ny][nx]) - A] == 0:
            VISITED[ord(BOARD[ny][nx]) - A] = 1
            dfs(nx, ny, cnt + 1)
            VISITED[ord(BOARD[ny][nx]) - A] = 0


if __name__ == "__main__":
    R, C = map(int, INPUT().split())
    A = ord("A")
    BOARD = [INPUT().rstrip() for _ in range(R)]
    VISITED = [0] * 26
    VISITED[ord(BOARD[0][0]) - A] = 1
    MAX_CNT = 0
    dfs(0, 0, 1)
    print(MAX_CNT)
