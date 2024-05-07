# 참고: https://bgspro.tistory.com/70

import sys
from collections import deque

INPUT = sys.stdin.readline
DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))


def bfs():
    queue = deque([(RED[0], RED[1], BLUE[0], BLUE[1], 0)])
    VISITED.append((RED[0], RED[1], BLUE[0], BLUE[1]))

    while queue:
        red_y, red_x, blue_y, blue_x, cnt = queue.popleft()

        for dy, dx in DIRECTIONS:
            # 파랑색 구슬 이동
            n_blue_y, n_blue_x = blue_y, blue_x
            while True:
                n_blue_y += dy
                n_blue_x += dx
                # 벽에 도달하면 뒤로 한 칸
                if BOARD[n_blue_y][n_blue_x] == "#":
                    n_blue_y -= dy
                    n_blue_x -= dx
                    break
                # 탈출하면 break
                elif BOARD[n_blue_y][n_blue_x] == "O":
                    break

            # 빨강색 구슬 이동
            n_red_y, n_red_x = red_y, red_x
            while True:
                n_red_y += dy
                n_red_x += dx
                # 벽에 도달하면 뒤로 한 칸
                if BOARD[n_red_y][n_red_x] == "#":
                    n_red_y -= dy
                    n_red_x -= dx
                    break
                # 탈출하면 break
                elif BOARD[n_red_y][n_red_x] == "O":
                    break

            # 파랑색 구슬이 들어갔다면 넘어감
            if BOARD[n_blue_y][n_blue_x] == "O":
                continue

            # 두 구슬이 같다면 나중에 온 구슬이 한 칸 뒤로 감
            if n_blue_x == n_red_x and n_blue_y == n_red_y:
                if abs(n_red_y - red_y) + abs(n_red_x - red_x) > abs(
                    n_blue_y - blue_y
                ) + abs(n_blue_x - blue_x):
                    n_red_y -= dy
                    n_red_x -= dx
                else:
                    n_blue_y -= dy
                    n_blue_x -= dx

            if BOARD[n_red_y][n_red_x] == "O":
                return cnt + 1

            if (n_red_y, n_red_x, n_blue_y, n_blue_x) not in VISITED and cnt + 1 < 10:
                queue.append((n_red_y, n_red_x, n_blue_y, n_blue_x, cnt + 1))
                VISITED.append((n_red_y, n_red_x, n_blue_y, n_blue_x))

    return -1


if __name__ == "__main__":
    N, M = map(int, INPUT().split())
    BOARD = []
    BLUE, RED, HOLE = (-1, -1), (-1, -1), (-1, -1)
    VISITED = []
    for y in range(N):
        line = list(INPUT().rstrip())
        for x, l in enumerate(line):
            if l == "B":
                BLUE = (y, x)
            elif l == "R":
                RED = (y, x)
        BOARD.append(line)

    print(bfs())
