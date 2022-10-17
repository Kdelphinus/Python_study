# minkj1992의 풀이: https://www.acmicpc.net/source/14400838
# 위의 풀이로 시간 단축

import sys

input = sys.stdin.readline


def update(y: int, x: int):
    global shark

    _, _, size, level = shark
    board[y][x] = 0
    shark = [y, x, size + 1, size + 1] if level == 1 else [y, x, size, level - 1]


def baby_shark(n: int):
    global shark

    cnt = 0
    sy, sx, size, _ = shark
    queue = [(sy, sx)]
    directions = (1, 0), (-1, 0), (0, 1), (0, -1)
    visit = [[0] * n for _ in range(n)]
    visit[sy][sx] = 1
    while queue:
        cnt += 1
        can_eat = []
        len_q = len(queue)
        for _ in range(len_q):
            y, x = queue.pop(0)
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if (
                    0 <= ny < n
                    and 0 <= nx < n
                    and not visit[ny][nx]
                    and board[ny][nx] <= size
                ):
                    visit[ny][nx] = 1
                    if 0 < board[ny][nx] < size:
                        can_eat.append((ny, nx))
                    else:
                        queue.append((ny, nx))
        if can_eat:
            fish = sorted(can_eat)[0]
            update(*fish)
            return cnt
    return 0


if __name__ == "__main__":
    n = int(input())
    fishes, board, flag = [], [], False
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j, t in enumerate(tmp):
            if 0 < t < 9:
                flag = t < 2
            elif t == 9:
                shark = [i, j, 2, 2]
                tmp[j] = 0
        board.append(tmp)
    total = 0
    while True:
        tmp = baby_shark(n)
        if not tmp:
            break
        total += tmp
    print(total)
