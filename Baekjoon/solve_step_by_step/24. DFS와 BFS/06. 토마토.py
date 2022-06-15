"""7576 토마토"""
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
#
# def BFS(m, n, box):
#     """BFS
#
#     Args:
#         m (int): 가로 길이
#         n (int): 세로 길이
#         box (2d list): 토마토가 들어있는 박스
#
#     Returns:
#         days(int): 모든 토마토가 익는데 걸리는 날짜
#     """
#     # 아래, 위, 오른쪽, 왼쪽
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#
#     days = -1  # 첫 시작은 하루로 취급하지 않기에
#
#     while queue:  # 큐에 아무것도 없을 때까지 반복
#         days += 1  # 하루가 지나고
#         for _ in range(len(queue)):  # 시작할 때 익은 토마토까지만 확인(반복문 안에서 익은 토마토들은 다음 날에 확인하게 됨)
#             x, y = queue.popleft()  # 큐에 들어가있는 x, y좌표를 불러옴
#
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#
#                 if (
#                     0 <= nx < m and 0 <= ny < n and box[ny][nx] == 0
#                 ):  # 박스 크기를 벗어나지 않고 토마토가 안 익었다면
#                     box[ny][nx] = box[y][x] + 1  # 토마토가 익고
#                     queue.append([nx, ny])  # 익은 토마토의 좌표를 추가
#
#     for b in box:
#         if 0 in b:  # 안 익은 토마토가 있다면
#             return -1
#     return days
#
#
# m, n = map(int, input().split())  # 가로, 세로
# tomato_box = []  # 토마토를 넣을 박스
# queue = deque()
#
#
# for y in range(n):
#     tmp = list(map(int, input().split()))
#     for x in range(m):
#         if tmp[x] == 1:  # 토마토가 익은 토마토라면
#             queue.append([x, y])
#     tomato_box.append(tmp)
#
# print(BFS(m, n, tomato_box))


##########################################################################################################
"""2022.03.18"""

from collections import deque


def BFS():
    days = -1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        for _ in range(len(queue)):
            y, x = queue[0][0], queue[0][1]
            queue.popleft()

            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]

                if 0 <= ny < row and 0 <= nx < column and box[ny][nx] == 0:
                    box[ny][nx] = 1
                    queue.append([ny, nx])
        days += 1

    for r in box:
        if 0 in r:
            return -1
    return days


queue = deque()
column, row = map(int, input().split())
box = []
for r in range(row):
    tmp_list = list(map(int, input().split()))
    for j in range(column):
        if tmp_list[j] == 1:
            queue.append([r, j])
    box.append(tmp_list)

print(BFS())
