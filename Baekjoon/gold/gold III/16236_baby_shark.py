import sys
from collections import deque

input = sys.stdin.readline


def what_time(i: int, j: int, n: int, baby: int, queue: deque):
    directions = (1, 0), (-1, 0), (0, 1), (0, -1)
    visit = [[0] * n for _ in range(n)]
    visit[queue[0][0]][queue[0][1]] = 1
    while queue:
        y, x, cnt = queue.popleft()

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if (
                0 <= ny < n
                and 0 <= nx < n
                and not visit[ny][nx]
                and board[ny][nx] <= baby
            ):
                if ny == i and nx == j:
                    return cnt + 1
                visit[ny][nx] = 1
                queue.append([ny, nx, cnt + 1])
    return -1


def baby_shark(n: int, baby: int, shark: list):
    survive, eat = 0, 0
    while fishes:
        during = [float("inf")] * 4
        for idx, (i, j, t) in enumerate(fishes):
            if t < baby:
                tmp = what_time(i, j, n, baby, deque([shark]))
                if 0 < tmp < during[0]:
                    during = [tmp, idx, i, j]
        if during[0] == float("inf"):
            return survive
        del fishes[during[1]]
        eat += 1
        if eat == baby:
            baby += 1
            eat = 0
        survive += during[0]
        board[shark[0]][shark[1]] = 0
        shark = during[2:] + [0]
    return survive


if __name__ == "__main__":
    n = int(input())
    fishes, board = [], []
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j, t in enumerate(tmp):
            if 0 < t < 9:
                fishes.append((i, j, t))
            elif t == 9:
                shark = [i, j, 0]
                tmp[j] = 0
        board.append(tmp)
    print(baby_shark(n, 2, shark))
