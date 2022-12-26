def printing(n: int, orders: str) -> None:
    board = [[[0, 0] for _ in range(n)] for __ in range(n)]
    now = [0, 0]
    move = {"U": [0, -1], "D": [0, 1], "R": [1, 0], "L": [-1, 0]}
    for order in orders:
        x, y = now
        dx, dy = move[order]
        if 0 <= x + dx < n and 0 <= y + dy < n:
            if dx == 0:
                board[y][x][1] = 1
                board[y + dy][x + dx][1] = 1
            else:
                board[y][x][0] = 1
                board[y + dy][x + dx][0] = 1
            now = [x + dx, y + dy]
    for b in board:
        for d in b:
            if d[0] == 1 and d[1] == 1:
                print("+", end="")
            elif d[0] == 1:
                print("-", end="")
            elif d[1] == 1:
                print("|", end="")
            else:
                print(".", end="")
        print()


if __name__ == "__main__":
    N = int(input())
    O = input()
    printing(N, O)
