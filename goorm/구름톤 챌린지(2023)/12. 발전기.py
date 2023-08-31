from collections import deque


def find_generator(y, x):
    queue = deque([(y, x)])
    TOWN[y][x] = 0
    while queue:
        y, x = queue.popleft()

        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and TOWN[ny][nx]:
                queue.append((ny, nx))
                TOWN[ny][nx] = 0


if __name__ == "__main__":
    N, CNT = int(input()), 0
    TOWN = [list(map(int, input().split())) for _ in range(N)]
    for Y in range(N):
        for X in range(N):
            if TOWN[Y][X]:
                find_generator(Y, X)
                CNT += 1
    print(CNT)
