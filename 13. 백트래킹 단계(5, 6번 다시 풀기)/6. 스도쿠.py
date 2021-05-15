"""2580 스도쿠"""

# 스도쿠와 빈 칸
sudoku = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]


def is_possible(i, j):
    """빈 칸에 들어갈 수 있는 수를 구하는 함수"""
    possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 행열 검사
    for k in range(9):
        if sudoku[i][k] in possible:
            possible.remove(sudoku[i][k])
        if sudoku[k][j] in possible:
            possible.remove(sudoku[k][j])

    # 박스 검사
    i //= 3
    j //= 3
    for p in range(i * 3, i * 3 + 3):
        for q in range(j * 3, j * 3 + 3):
            if sudoku[p][q] in possible:
                possible.remove(sudoku[p][q])

    return possible


answer = False  # 답 출력 여부


def solution(x):
    global answer

    if answer:  # 이미 답이 출력된 경우
        return

    if x == len(zeros):  # 마지막 빈칸까지 다 채웠을 경우
        for row in sudoku:
            print(*row)  # 리스트 안에 수를 한 칸씩 띄어 차례대로 출력
        answer = True
        return

    else:
        (i, j) = zeros[x]
        possible = is_possible(i, j)

        for num in possible:
            sudoku[i][j] = num  # 가능한 수 중 하나를 넣음
            solution(x + 1)  # 다음 빈칸으로 이동
            sudoku[i][j] = 0  # 정답이 없을 경우 초기화


solution(0)