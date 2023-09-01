def flag(n, k, board):
    cnt = 0
    directions = ((1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1))

    for y in range(n):
        for x in range(n):
            if board[y][x]:
                continue
            tmp = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and board[ny][nx]:
                    tmp += 1
            if tmp == k:
                cnt += 1

    return cnt


if __name__ == "__main__":
    N, K = map(int, input().split())
    BOARD = [list(map(int, input().split())) for _ in range(N)]
    print(flag(N, K, BOARD))
