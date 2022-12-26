from collections import deque


def init(h: int) -> tuple:
    sharks, sea = [], []
    for i in range(h):
        tmp = list(map(int, input().split()))
        for j, t in enumerate(tmp):
            if t == 1:
                sharks.append((i, j))
        sea.append(tmp)
    return sharks, sea


def max_dist(sea: list) -> int:
    ans = 0
    for s in sea:
        ans = max(max(s), ans)
    return ans - 1


def safe_dist(h: int, w: int) -> int:
    sharks, sea = init(h)
    sharks = deque(sharks)
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    while sharks:
        y, x = sharks.popleft()

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w:
                if sea[ny][nx] == 0 or sea[ny][nx] > sea[y][x] + 1:
                    sea[ny][nx] = sea[y][x] + 1
                    sharks.append((ny, nx))

    return max_dist(sea)


if __name__ == "__main__":
    N, M = map(int, input().split())
    print(safe_dist(N, M))
