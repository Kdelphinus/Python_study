# 제출한 답안 링크: https://aia1235.tistory.com/44
# 밑에 나의 답안과 무엇이 다른지 찾아봐야 함

import sys
import copy

INPUT = sys.stdin.readline


def move_up(board: list[list[int]]) -> (bool, list[list[int]]):
    flag = False
    checked = [[0 for _ in range(N)] for __ in range(N)]
    for y in range(1, N):
        for x in range(N):
            if board[y][x] == 0:
                continue

            i = 0
            while y - i - 1 >= 0 and board[y - i - 1][x] == 0:
                i += 1
            if (
                y - 1 - i >= 0
                and board[y][x] == board[y - 1 - i][x]
                and checked[y - 1 - i][x] == 0
            ):
                flag = True
                board[y - 1 - i][x] *= 2
                board[y][x] = 0
                checked[y - 1 - i][x] = 1
            elif i != 0:
                flag = True
                board[y - i][x] = board[y][x]
                board[y][x] = 0

    return flag, board


def move_down(board: list[list[int]]) -> (bool, list[list[int]]):
    flag = False
    checked = [[0 for _ in range(N)] for __ in range(N)]
    for y in range(N - 2, -1, -1):
        for x in range(N):
            if board[y][x] == 0:
                continue

            i = 0
            while y + 1 + i < N and board[y + 1 + i][x] == 0:
                i += 1
            if (
                y + 1 + i < N
                and board[y][x] == board[y + 1 + i][x]
                and checked[y + 1 + i][x] == 0
            ):
                flag = True
                board[y + 1 + i][x] *= 2
                board[y][x] = 0
                checked[y + 1 + i][x] = 1
            elif i != 0:
                flag = True
                board[y + i][x] = board[y][x]
                board[y][x] = 0

    return flag, board


def move_left(board: list[list[int]]) -> (bool, list[list[int]]):
    flag = False
    checked = [[0 for _ in range(N)] for __ in range(N)]
    for x in range(1, N):
        for y in range(N):
            if board[y][x] == 0:
                continue

            i = 0
            while x - 1 - i >= 0 and board[y][x - 1 - i] == 0:
                i += 1
            if (
                x - 1 - i >= 0
                and board[y][x] == board[y][x - 1 - i]
                and checked[y][x - 1 - i] == 0
            ):
                flag = True
                board[y][x - 1 - i] *= 2
                board[y][x] = 0
                checked[y][x - 1 - i] = 0
            elif i != 0:
                flag = True
                board[y][x - i] = board[y][x]
                board[y][x] = 0

    return flag, board


def move_right(board: list[list[int]]) -> (bool, list[list[int]]):
    flag = False
    checked = [[0 for _ in range(N)] for __ in range(N)]
    for x in range(N - 2, -1, -1):
        for y in range(N):
            if board[y][x] == 0:
                continue

            i = 0
            while x + 1 + i < N and board[y][x + 1 + i] == 0:
                i += 1
            if (
                x + 1 + i < N
                and board[y][x] == board[y][x + 1 + i]
                and checked[y][x + 1 + i] == 0
            ):
                flag = True
                board[y][x + 1 + i] *= 2
                board[y][x] = 0
                checked[y][x + 1 + i] = 1
            elif i != 0:
                flag = True
                board[y][x + i] = board[y][x]
                board[y][x] = 0

    return flag, board


def game_2048(cnt: int, board: list[list[int]]) -> None:
    global max_value

    if cnt == 5:
        for b in board:
            max_value = max(max_value, max(b))
        return

    flag, board_up = move_up(copy.deepcopy(board))
    if flag:
        game_2048(cnt + 1, board_up)
    flag, board_down = move_down(copy.deepcopy(board))
    if flag:
        game_2048(cnt + 1, board_down)
    flag, board_left = move_left(copy.deepcopy(board))
    if flag:
        game_2048(cnt + 1, board_left)
    flag, board_right = move_right(copy.deepcopy(board))
    if flag:
        game_2048(cnt + 1, board_right)


if __name__ == "__main__":
    N = int(INPUT())
    max_value = 0
    BOARD = []
    for _ in range(N):
        tmp = list(map(int, INPUT().split()))
        max_value = max(max_value, max(tmp))
        BOARD.append(tmp)
    game_2048(0, BOARD)
    print(max_value)
