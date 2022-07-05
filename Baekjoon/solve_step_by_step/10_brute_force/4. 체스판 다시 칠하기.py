"""1018 체스판 다시 칠하기"""

# n, m = map(int, input().split())  # n x m 보드
# board = []  # 입력된 보드를 저장할 리스트
# cnts = []  # 색칠한 횟수들을 저장할 리스트
#
# # 보드를 입력 받는다
# for _ in range(n):
#     board.append(input())
#
# # 몇 번 색칠해야 하는지 판단
# for i in range(n - 7):
#     for j in range(m - 7):
#         first_black = 0  # 체스판의 시작이 검정일 때 색칠할 횟수
#         first_white = 0  # 체스판의 시작이 하양일 때 색칠할 횟수
#
#         # 8 x 8로 만든다
#         for a in range(i, i + 8):
#             for b in range(j, j + 8):
#                 if (a + b) % 2 == 0:  # 둘의 합이 짝수인 경우는 둘 다 홀수이거나 둘 다 짝수일 때
#                     if board[a][b] != "B":
#                         first_black += 1  # 처음이 검정일 때, 이 위치는 검정이어야 한다
#                     if board[a][b] != "W":
#                         first_white += 1  # 처음이 하양일 때, 이 위치는 하양이어야 한다
#                 else:  # 둘의 합이 홀수인 경우는 하나는 짝수, 하나는 홀수일 때
#                     if board[a][b] != "W":
#                         first_black += 1  # 처음이 검정일 때, 이 위치는 하양이어야 한다
#                     if board[a][b] != "B":
#                         first_white += 1  # 처음이 하양일 때, 이 위치는 검정이어야 한다
#
#         # 횟수를 추가한다
#         # 처음이 검정일 경우, first_white는 무조건 first_black보다 크기에 넣어도 결과에 영향을 못 미친다, 역도 마찬가지
#         cnts.append(first_white)
#         cnts.append(first_black)
#
# # 구한 색칠 횟수 중 가장 작은 것을 출력
# print(min(cnts))


#################################################################################################
"""2022.03.18 풀이"""

board = []
cnts = []
n, m = map(int, input().split())
for _ in range(n):
    board.append(input())

for i in range(n - 7):
    for j in range(m - 7):
        first_black = 0
        first_white = 0

        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if board[a][b] == "W":
                        first_black += 1
                    else:
                        first_white += 1
                else:
                    if board[a][b] == "B":
                        first_black += 1
                    else:
                        first_white += 1

        cnts.append(first_black)
        cnts.append(first_white)

print(min(cnts))
