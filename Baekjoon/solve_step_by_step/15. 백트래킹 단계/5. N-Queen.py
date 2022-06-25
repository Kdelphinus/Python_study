"""9663 N-Queen"""
"""i - j + n - 1과 i + j는 사진 참고"""

import sys

input = sys.stdin.readline

N = int(input().rstrip())  # N x N 체스판

cnt = 0  # 퀸을 놓을 수 있는 수
height = [False] * N  # 세로
left_diagonal = [False] * (2 * N - 1)  # 왼쪽으로 내려가는 대각선
right_diagonal = [False] * (2 * N - 1)  # 오른쪽으로 내려가는 대각선


def N_queen(i):
    """퀸을 놓는 방법을 구하는 함수"""
    global cnt

    if i == N:  # 퀸을 다 두었을 때
        cnt += 1
        return

    for j in range(N):  # 세로, 왼쪽 대각선, 오른쪽 대각선에 퀸이 없을 경우 두고 다음 행으로 이동
        if not (height[j] or left_diagonal[i + j] or right_diagonal[i - j + N - 1]):
            height[j] = left_diagonal[i + j] = right_diagonal[i - j + N - 1] = True
            N_queen(i + 1)
            height[j] = left_diagonal[i + j] = right_diagonal[i - j + N - 1] = False


N_queen(0)
print(cnt)
