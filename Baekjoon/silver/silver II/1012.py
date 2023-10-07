import sys
from collections import deque

INPUT = sys.stdin.readline
DIR = ((0, 1), (0, -1), (1, 0), (-1, 0))


def bfs(n: int, m: int, cabbage: list, ground: list) -> int:
    ans = 0
    for cx, cy in cabbage:
        if not ground[cy][cx]:
            continue
        queue = deque([(cx, cy)])
        ans += 1
        while queue:
            x, y = queue.popleft()
            for dx, dy in DIR:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and ground[ny][nx]:
                    ground[ny][nx] = 0
                    queue.append((nx, ny))
    return ans


if __name__ == "__main__":
    T = int(INPUT())
    for _ in range(T):
        M, N, K = map(int, INPUT().split())
        GROUND, CABBAGE = [[0 for _ in range(M)] for _ in range(N)], []
        for i in range(K):
            CABBAGE.append(tuple(map(int, INPUT().split())))
            GROUND[CABBAGE[-1][1]][CABBAGE[-1][0]] = 1
        print(bfs(N, M, CABBAGE, GROUND))
