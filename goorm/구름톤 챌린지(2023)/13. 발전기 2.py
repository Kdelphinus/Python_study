import sys
from collections import deque


INPUT = sys.stdin.readline


def find_block(y, x):
    cnt, status, queue = 1, TOWN[y][x], deque([(y, x)])
    TOWN[y][x] = 0

    while queue:
        y, x = queue.popleft()

        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and TOWN[ny][nx] == status:
                cnt += 1
                TOWN[ny][nx] = 0
                queue.append((ny, nx))

    return cnt


if __name__ == "__main__":
    N, K = map(int, INPUT().split())
    TOWN = [list(map(int, INPUT().split())) for _ in range(N)]
    BLOCKS = [[0, i] for i in range(31)]
    for Y in range(N):
        for X in range(N):
            if TOWN[Y][X]:
                status, cnt = TOWN[Y][X], find_block(Y, X)
                if cnt >= K:
                    BLOCKS[status][0] += 1
    BLOCKS.sort(key=lambda x: (-x[0], -x[1]))
    print(BLOCKS[0][1])
