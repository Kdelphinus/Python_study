import sys
from collections import deque

INPUT = sys.stdin.readline
DICT = {"M": "O", "O": "B", "B": "I", "I": "S"}
DIRECTION = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))


def bfs(sy: int, sx: int):
    global CNT

    queue = deque()
    for dy, dx in DIRECTION:
        ny, nx = sy + dy, sx + dx
        if 0 <= ny < N and 0 <= nx < N and "O" == BOARD[ny][nx]:
            queue.append((ny, nx, "O", dy, dx))

    while queue:
        cy, cx, alpha, dy, dx = queue.popleft()
        ny, nx = cy + dy, cx + dx
        try:
            if 0 <= ny < N and 0 <= nx < N and DICT[alpha] == BOARD[ny][nx]:
                if alpha == "I":
                    CNT += 1
                else:
                    queue.append((ny, nx, DICT[alpha], dy, dx))
        except KeyError:
            continue


N = int(input())
CNT = 0
START = []
BOARD = []
for y in range(N):
    tmp = INPUT().rstrip()
    for x, c in enumerate(tmp):
        if c == "M":
            START.append((y, x))
    BOARD.append(tmp)

for y, x in START:
    bfs(y, x)

print(CNT)
