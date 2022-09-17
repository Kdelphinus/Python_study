from collections import deque


def game_over(n: int, sy: int, sx: int, board: list) -> int:
    """
    function to determine if game is over
    Args:
        n: board size
        sy: row position
        sx: column position
        board: game board

    Returns:
        1: game is over
        0: game is not over
    """
    if sy < 0 or sy >= n or sx < 0 or sx >= n:
        return 1
    if board[sy][sx] == 1:
        return 1
    return 0


def change_direction(idx: int, turn_num: int) -> int:
    """
    function to change direction
    Args:
        idx: index of previous direction
        turn_num: direction from current time

    Returns:
        index of current direction
    """
    if turn_num == "D":  # rotate clockwise
        return idx + 1 if idx < 3 else 0
    if turn_num == "L":  # rotate counterclockwise
        return idx - 1 if idx > 0 else 3
    return idx


def game_playing(n: int, board: list, turnabout: list) -> int:
    """
    function to check game progress
    Args:
        n: board size
        board: game board
        turnabout: list of turns per time

    Returns:
        time the game was played
    """
    time = 0
    sy, sx = 0, 0
    idx = 0
    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    route = deque([[0, 0]])
    board[0][0] = 1

    while True:
        time += 1
        sy += dxy[idx][0]
        sx += dxy[idx][1]
        route.append([sy, sx])
        if game_over(n, sy, sx, board):
            return time
        if board[sy][sx] == 0:
            ty, tx = route.popleft()
            board[ty][tx] = 0
        board[sy][sx] = 1
        idx = change_direction(idx, turnabout[time])


def main():
    n = int(input())
    board = [[0] * n for _ in range(n)]

    apple_num = int(input())
    for _ in range(apple_num):
        ay, ax = map(int, input().split())
        board[ay - 1][ax - 1] = 2

    turnabout_num = int(input())
    turnabout = [0] * 10001
    for _ in range(turnabout_num):
        t, d = input().split()
        turnabout[int(t)] = d

    print(game_playing(n, board, turnabout))


if __name__ == "__main__":
    main()
