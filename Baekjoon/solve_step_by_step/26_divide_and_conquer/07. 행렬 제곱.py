"""10830 행렬 제곱"""
import sys

input = sys.stdin.readline


def matrix_power(A, num):
    """행렬 A를 num만큼 곱하는 함수"""
    if num == 1:
        for i in range(len(A)):
            for j in range(len(A)):
                A[i][j] %= 1000
        return A
    else:
        temp = matrix_power(A, num // 2)
        if num % 2:  # 홀수일 때
            return matrix_multiplication(matrix_multiplication(temp, temp), A)
        else:  # 짝수일 때
            return matrix_multiplication(temp, temp)


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
            temp_list.append(temp % 1000)
        anw.append(temp_list)

    return anw


# n x n 행렬과 제곱수 k 입력
n, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

anw = matrix_power(matrix, k)

for i in anw:
    print(*i)
