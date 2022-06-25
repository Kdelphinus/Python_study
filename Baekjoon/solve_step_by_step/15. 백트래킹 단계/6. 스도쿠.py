"""2580 스도쿠"""

import sys

input = sys.stdin.readline

sudoku = [list(map(int, input().split())) for _ in range(9)]  # 완성되지 않은 스도쿠
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]  # 빈 칸의 좌표


def is_possible(i, j):
    """빈 칸에 들어갈 수 있는 수를 구하는 함수"""
    possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for k in range(9):
        if sudoku[i][k] in possible:  # 열에 들어있는 숫자 확인
            possible.remove(sudoku[i][k])
        if sudoku[k][j] in possible:  # 행에 들어있는 숫자 확인
            possible.remove(sudoku[k][j])

    i = i // 3 * 3  # 박스 가로 길이
    j = j // 3 * 3  # 박스 세로 길이

    for p in range(i, i + 3):  # 박스 안에 들어있는 숫자 확인
        for q in range(j, j + 3):
            if sudoku[p][q] in possible:
                possible.remove(sudoku[p][q])

    return possible


flag = False  # 정답을 출력했는지 확인하는 변수


def sudoku_solution(x):
    """스도쿠 빈 칸을 채워주는 함수"""
    global flag

    if flag:  # 답을 이미 출력했을 때
        return

    if x == len(zeros):  # 모든 빈 칸을 채웠을 때
        for row in sudoku:
            print(*row)
        flag = True
        return

    i, j = zeros[x]  # 빈 칸의 좌표를 가져옴
    possible = is_possible(i, j)  # 들어갈 수 있는 숫자를 계산

    for num in possible:
        sudoku[i][j] = num  # 들어갈 수 있는 숫자를 채움
        sudoku_solution(x + 1)  # 다음 빈 칸으로 넘어감
        sudoku[i][j] = 0  # 지금 숫자가 정답이 아니면 다시 빈 칸으로 비워둠


sudoku_solution(0)  # 첫 번째 빈칸부터 확인
