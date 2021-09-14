"""11049 행렬 곱셈 순서"""
import sys
import math

input = sys.stdin.readline


def matrix_multiplication(num, matrix):
    # dp[i][j]: i번째 행렬부터 j번째 행렬까지 곱한 총 횟수
    dp = [[0 for i in range(num)] for _ in range(num)]

    for gap in range(1, num):  # gap: 첫 행렬과 끝 행렬 사이 간격
        for start in range(num - gap):  # start: 첫 행렬
            end = start + gap  # end: 끝 행렬
            dp[start][end] = math.inf  # 초기값 설정
            for i in range(start, end):  # i: 곱하는 부분
                dp[start][end] = min(  # 곱하는 부분을 바꿔가면서 최소 횟수인 경우를 구한다
                    dp[start][end],
                    dp[start][i]
                    + dp[i + 1][end]
                    + matrix[start][0] * matrix[i][1] * matrix[end][1],
                )
    print(dp[0][-1])


num = int(input())  # 행렬 개수
matrix = [list(map(int, input().split())) for _ in range(num)]  # 행렬의 크기
matrix_multiplication(num, matrix)