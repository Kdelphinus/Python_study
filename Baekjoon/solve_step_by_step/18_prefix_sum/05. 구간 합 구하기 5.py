"""11660 구간 합 구하기 5 / silver I"""

# 코드: https://pacific-ocean.tistory.com/459
# 설명: https://castlerain.tistory.com/100

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
table = [[0] * (n + 1)]
table += [[0] + list(map(int, input().split())) for _ in range(n)]

# (1, 1) ~ (n, n)의 순서로 누적 합 계산
for y in range(n):
    for x in range(n):
        table[y + 1][x + 1] += table[y][x + 1] + table[y + 1][x] - table[y][x]

# 설명 그림 참고
for _ in range(m):
    y1, x1, y2, x2 = map(int, input().split())
    print(table[y2][x2] - table[y2][x1 - 1] - table[y1 - 1][x2] + table[y1 - 1][x1 - 1])

#####################################################################################

"""시간초과"""
# n, m = map(int, input().split())
# table = [[0] + list(map(int, input().split())) for _ in range(n)]
#
# for i in range(n):
#     for j in range(1, n + 1):
#         table[i][j] += table[i][j - 1]
#
# for _ in range(m):
#     y1, x1, y2, x2 = map(int, input().split())
#     if y1 == y2:
#         print(table[y1 - 1][x2] - table[y1 - 1][x1 - 1])
#     else:
#         result = 0
#         for y in range(y1 - 1, y2):
#             result += table[y][x2] - table[y][x1 - 1]
#         print(result)
