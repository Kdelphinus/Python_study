"""연습문제"""


def solution(board):
    side = 0
    height = len(board)
    width = len(board[0])

    for i in range(height):
        for j in range(width):
            if i == 0 or j == 0:  # 맨 위나 맨 왼쪽일 경우
                if board[i][j] == 1:  # 그러면서 사각형이 있다면
                    side = max(side, board[i][j])  # 길이 최신화
                continue  # 바로 다음 칸으로 이동

            if board[i][j] == 1:  # 사각형이 있다면
                # 좌측, 상단, 좌측상단 중 최솟값 + 1의 값을 갖는다
                board[i][j] = (
                    min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1
                )
                side = max(side, board[i][j])  # 최댓값 최신화

    return side * side


print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))  # 9
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))  # 4


# ---------------------------------------------------------------------------------------------
"""내가 원래 구현하려고 했던 것, 효율도 이게 더 좋음"""


def solution(board):
    answer = 0
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] >= 1:
                board[i][j] += min(
                    board[i - 1][j - 1], board[i][j - 1], board[i - 1][j]
                )

    # 이 부분이 없어서 i나 j가 0인 부분만 사각형이 있을 때 답이 나오지 못했음
    for i in board:
        answer = max(answer, max(i))

    return answer * answer
