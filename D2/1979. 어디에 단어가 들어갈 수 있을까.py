test = int(input())

for t in range(test):
    n, k = map(int, input().split())  # n x n, 단어 길이
    board = [list(map(int, input().split())) for _ in range(n)]
    cnt_width = 0
    cnt_height = 0
    result = 0

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:  # 가로 확인
                cnt_width += 1
            elif board[i][j] == 0:
                if cnt_width == k:
                    result += 1
                cnt_width = 0

            if board[j][i] == 1:  # 세로 확인
                cnt_height += 1
            elif board[j][i] == 0:
                if cnt_height == k:
                    result += 1
                cnt_height = 0

        if cnt_width == k:
            result += 1
        if cnt_height == k:
            result += 1
        cnt_height = 0
        cnt_width = 0

    print("#{} {}".format(t + 1, result))
