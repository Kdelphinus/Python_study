def board_game(position):
    dire = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}

    flag, cnt = True, 1
    visit = [[0 for _ in range(N)] for __ in range(N)]
    visit[position[0]][position[1]] = 1
    while flag:
        tmp = list(BOARD[position[0]][position[1]])
        num, order = "".join(tmp[:-1]), str(tmp[-1])
        for _ in range(int(num)):
            for i in range(2):
                position[i] += dire[order][i]
                if position[i] == N:
                    position[i] = 0
                if position[i] == -1:
                    position[i] = N - 1
            if visit[position[0]][position[1]] == 1:
                flag = False
                break
            visit[position[0]][position[1]] = 1
            cnt += 1

    return cnt


N = int(input())
GOORM = list(map(int, input().split()))
GOORM[0] -= 1
GOORM[1] -= 1
PLAYER = list(map(int, input().split()))
PLAYER[0] -= 1
PLAYER[1] -= 1
BOARD = [list(input().split()) for _ in range(N)]
goorm = board_game(GOORM)
player = board_game(PLAYER)
print(f"goorm {goorm}") if goorm > player else print(f"player {player}")
