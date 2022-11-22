import sys
from collections import deque

input = sys.stdin.readline


def bfs(h: int, w: int, start: tuple) -> int:
    t_a = 1
    dxy = ((1, 0), (-1, 0), (0, 1), (0, -1))
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = 1
    while queue:
        y, x = queue.popleft()
        for dy, dx in dxy:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx] and paper[ny][nx]:
                visited[ny][nx] = 1
                queue.append((ny, nx))
                t_a += 1
    return t_a


def painting_size(h: int, w: int) -> tuple:
    c, a = 0, 0
    for y in range(h):
        for x in range(w):
            if not visited[y][x] and paper[y][x]:
                a = max(a, bfs(h, w, (y, x)))
                c += 1
    return (c, a)


if __name__ == "__main__":
    height, width = map(int, input().split())
    paper = [list(map(int, input().split())) for _ in range(height)]
    print(paper)
    visited = [[0] * width for _ in range(height)]
    cnt, area = painting_size(height, width)
    print(cnt)
    print(area)
