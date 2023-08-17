from collections import deque


def people(n: int, m: int, board: list) -> str or int:
    direction = ((0, 1), (0, -1), (1, 0), (-1, 0))
    cnt, queue = 0, deque()
    queue.append(PLAYER)

    while queue:
        y, x = queue.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if board[ny][nx] == "X":
                    continue
                if board[ny][nx] == "P":
                    cnt += 1
                board[ny][nx] = "X"
                queue.append((ny, nx))
    return cnt if cnt else "TT"


if __name__ == "__main__":
    N, M = map(int, input().split())
    BOARD = []
    for i in range(N):
        tmp = input()
        if "I" in tmp:
            PLAYER = (i, tmp.index("I"))
        BOARD.append(list(tmp))
    print(people(N, M, BOARD))
