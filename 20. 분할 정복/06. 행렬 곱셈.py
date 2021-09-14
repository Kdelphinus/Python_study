"""2740 행렬 곱셈"""
import sys

input = sys.stdin.readline


def matrix_multiplication(A, B):
    """행렬 곱셈하는 함수"""
    n = len(A)
    anw = []
    for i in range(n):
        m = len(A[0])
        k = len(B[0])
        temp_list = []

        for u in range(k):
            temp = 0
            for j in range(m):
                temp += A[i][j] * B[j][u]
            temp_list.append(temp)
        anw.append(temp_list)

    return anw


# n x m 크기의 행렬 A 저장
n, m = map(int, input().split())
matrix_A = [list(map(int, input().split())) for _ in range(n)]

# m x k 크기의 행렬 B 저장
m, k = map(int, input().split())
matrix_B = [list(map(int, input().split())) for _ in range(m)]

anw = matrix_multiplication(matrix_A, matrix_B)

for i in anw:
    print(*i)
