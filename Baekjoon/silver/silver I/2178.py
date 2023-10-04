import sys
from collections import deque

INPUT = sys.stdin.readline


def bfs(n: int, m: int, maze: list):
    queue = deque([(0, 0, 1)])
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    maze[0][0] = "0"

    while queue:
        y, x, cnt = queue.popleft()
        if y == n - 1 and x == m - 1:
            return cnt
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and maze[ny][nx] == "1":
                maze[ny][nx] = "0"
                queue.append((ny, nx, cnt + 1))
    return float("inf")


if __name__ == "__main__":
    N, M = map(int, INPUT().rstrip().split())
    MAZE = [list(input().strip()) for _ in range(N)]
    print(bfs(N, M, MAZE))
