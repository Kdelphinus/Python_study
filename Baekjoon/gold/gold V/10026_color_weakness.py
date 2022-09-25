from collections import deque


def normal(n: int, board: list, visit: list, start: tuple):
    queue = deque()
    queue.append(start)
    color = board[start[0]][start[1]]
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        y, x = queue.popleft()

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if (
                0 <= nx < n
                and 0 <= ny < n
                and not visit[ny][nx]
                and board[ny][nx] == color
            ):
                queue.append((ny, nx))
                visit[ny][nx] = 1


def color_week(n: int, board: list, visit: list, start: tuple):
    queue = deque()
    queue.append(start)
    color = board[start[0]][start[1]]
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        y, x = queue.popleft()

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if (
                0 <= nx < n
                and 0 <= ny < n
                and not visit[ny][nx]
                and board[ny][nx] == color
            ):
                queue.append((ny, nx))
                visit[ny][nx] = 1


if __name__ == "__main__":
    n = int(input())
    cnt = 0
    board = [input() for _ in range(n)]
    visit = [[0] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if not visit[y][x]:
                cnt += 1
                visit[y][x] = 1
                normal(n, board, visit, (y, x))
    print(cnt, end=" ")
    cnt = 0
    visit = [[0] * n for _ in range(n)]
    color_week_board = []
    for b in board:
        color_week_board.append(b.replace("R", "G"))
    for y in range(n):
        for x in range(n):
            if not visit[y][x]:
                cnt += 1
                visit[y][x] = 1
                color_week(n, color_week_board, visit, (y, x))
    print(cnt)
