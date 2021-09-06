"""2018 KAKAO BLIND RECRUITMENT"""


def solution(m, n, board):
    answer = 0
    board = [[j for j in i] for i in board]
    while True:
        check = []
        for i in range(1, m):
            for j in range(1, n):
                if (
                    board[i][j] != "0"
                    and board[i][j]
                    == board[i][j - 1]
                    == board[i - 1][j]
                    == board[i - 1][j - 1]
                ):
                    if [i, j] not in check:
                        check.append([i, j])
                    if [i, j - 1] not in check:
                        check.append([i, j - 1])
                    if [i - 1, j] not in check:
                        check.append([i - 1, j])
                    if [i - 1, j - 1] not in check:
                        check.append([i - 1, j - 1])
        answer += len(check)

        if check:
            for c in check:
                y, x = c[0], c[1]
                board[y][x] = "0"

            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    if board[i][j] == "0":
                        tmp = 1
                        while i - tmp >= 0:
                            if board[i - tmp][j] != "0":
                                board[i][j] = board[i - tmp][j]
                                board[i - tmp][j] = "0"
                                break
                            tmp += 1
        else:
            return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
