"""11444 피보나치 수 6"""

"""행렬 곱셈을 이용하여 피보나치 수를 구할 수 있다
[[F_n+1, F_n], [F_n, F_n-1]] = [[1, 1], [1, 0]] ** n"""

import sys

input = sys.stdin.readline

p = 1000000007


def matrix_power(A, num):
    """행렬 A를 num만큼 곱하는 함수"""
    if num == 1:
        for i in range(len(A)):
            for j in range(len(A)):
                A[i][j] %= p
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
            temp_list.append(temp % p)
        anw.append(temp_list)

    return anw


num = int(input())  # 숫자가 주어짐
matrix = [[1, 1], [1, 0]]  # 기본 배열

anw = matrix_power(matrix, num)
print(anw[0][1])