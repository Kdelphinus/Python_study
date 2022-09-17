"""2021 Dev-Matching: 웹 백엔드 개발자(상반기)"""


def rotation(y1, x1, y2, x2, matrix):
    """rotation 주어진 좌표들을 회전시키는 함수

    Args:
        y1 (int): 회전하는 사각형 왼쪽 상단 y좌표
        x1 (int): 회전하는 사각형 왼쪽 상단 x좌표
        y2 (int): 회전하는 사각형 오른쪽 하단 y좌표
        x2 (int): 회전하는 사각형 오른쪽 하단 x좌표
        matrix (2d-list): 주어진 행렬

    Returns:
        matrix (2d-list): 회전한 행렬
        min(change) (int): 회전한 값들 중 가장 작은 값
    """
    direction = 0  # 오른쪽으로 이동
    change = []  # 회전하는 숫자들
    x = x1 - 1  # 시작할 위치의 x좌표
    y = y1 - 1  # 시작할 위치의 y좌표
    before = matrix[y][x]  # 처음 이동할 수
    change.append(before)
    while True:
        if x == x2 - 1 and direction == 0:  # 우측 상단 도달 시
            direction = 1  # 아래로 이동
        elif y == y2 - 1 and direction == 1:  # 우측 하단 도달 시
            direction = 2  # 왼쪽으로 이동
        elif x == x1 - 1 and direction == 2:  # 좌측 하단 도달 시
            direction = 3  # 위로 이동

        if direction == 0:  # 오른쪽으로 이동
            tmp = matrix[y][x + 1]
            matrix[y][x + 1] = before
            x += 1
        elif direction == 1:  # 아래로 이동
            tmp = matrix[y + 1][x]
            matrix[y + 1][x] = before
            y += 1
        elif direction == 2:  # 왼쪽으로 이동
            tmp = matrix[y][x - 1]
            matrix[y][x - 1] = before
            x -= 1
        elif direction == 3:  # 위로 이동
            tmp = matrix[y - 1][x]
            matrix[y - 1][x] = before
            y -= 1
        before = tmp
        change.append(before)  # 회전한 것은 저장
        if x == x1 - 1 and y == y1 - 1:  # 다 돌았으면 종료
            break

    return matrix, min(change)  # 회전한 행렬, 회전한 수 중 가장 작은 수


def solution(rows, columns, queries):
    answer = []
    matrix = []

    # 행렬 초기화
    num = 1
    for y in range(rows):
        tmp = []
        for x in range(columns):
            tmp.append(num)
            num += 1
        matrix.append(tmp)

    # 주어진 좌표대로 회전
    for i in queries:
        matrix, result = rotation(i[0], i[1], i[2], i[3], matrix)
        answer.append(result)

    return answer


# ------------------------------------------------------------------------------------------------------------
"""다른 풀이"""


def solution(rows, columns, queries):
    answer = []

    board = [[i + (j) * columns for i in range(1, columns + 1)] for j in range(rows)]
    # print(board)

    for a, b, c, d in queries:
        stack = []
        r1, c1, r2, c2 = a - 1, b - 1, c - 1, d - 1

        for i in range(c1, c2 + 1):

            stack.append(board[r1][i])
            if len(stack) == 1:
                continue
            else:
                board[r1][i] = stack[-2]

        for j in range(r1 + 1, r2 + 1):
            stack.append(board[j][i])
            board[j][i] = stack[-2]

        for k in range(c2 - 1, c1 - 1, -1):
            stack.append(board[j][k])
            board[j][k] = stack[-2]

        for l in range(r2 - 1, r1 - 1, -1):
            stack.append(board[l][k])
            board[l][k] = stack[-2]

        answer.append(min(stack))

    return answer
