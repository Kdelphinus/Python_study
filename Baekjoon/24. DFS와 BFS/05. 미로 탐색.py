"""2178 미로 탐색"""
# import sys
#
# input = sys.stdin.readline
#
#
# def BFS(x, y):
#     """BFS
#
#     Args:
#         x (int): 가로 좌표
#         y (int): 세로 좌표
#     """
#     # 아래, 위, 오른쪽, 왼쪽
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#
#     visit[y][x] = 1  # 탐색했음을 표시
#     queue = [[x, y]]  # 시작지점을 저장
#
#     while queue:  # 큐에 아무것도 없을 때까지 반복
#         x, y = queue[0][0], queue[0][1]  # 큐에 들어가있는 x, y좌표를 불러옴
#         del queue[0]  # 꺼낸 좌표는 삭제
#
#         for i in range(4):  # 네 방향을 확인해봄
#             nx, ny = x + dx[i], y + dy[i]
#             if 0 <= nx < width and 0 <= ny < height:  # 지도 범위 안에 있고
#                 if visit[ny][nx] == 0 and maze[ny][nx] == "1":  # 탐색하지 않았으며 길이 있을 때
#                     queue.append([nx, ny])  # 그 좌표를 추가하고
#                     visit[ny][nx] = 1  # 탐색 표시를 하고
#                     dist[ny][nx] = dist[y][x] + 1  # 그 좌표로 가는 최소 거리를 저장
#
#         # 밑의 코드를 압축하면 위의 코드
#         # if y + 1 < height and visit[y + 1][x] == 0 and maze[y + 1][x] == "1":
#         #    queue.append([x, y + 1])
#         #    visit[y + 1][x] = 1
#         #    dist[y + 1][x] = dist[y][x] + 1
#         # if y - 1 >= 0 and visit[y - 1][x] == 0 and maze[y - 1][x] == "1":
#         #    queue.append([x, y - 1])
#         #    visit[y - 1][x] = 1
#         #    dist[y - 1][x] = dist[y][x] + 1
#         # if x + 1 < width and visit[y][x + 1] == 0 and maze[y][x + 1] == "1":
#         #    queue.append([x + 1, y])
#         #    visit[y][x + 1] = 1
#         #    dist[y][x + 1] = dist[y][x] + 1
#         # if x - 1 >= 0 and visit[y][x - 1] == 0 and maze[y][x - 1] == "1":
#         #    queue.append([x - 1, y])
#         #    visit[y][x - 1] = 1
#         #    dist[y][x - 1] = dist[y][x] + 1
#
#
# height, width = map(int, input().split())  # 세로와 가로
# maze = [list(input().strip()) for _ in range(height)]  # 미로
# visit = [[0] * width for _ in range(height)]  # 탐색 여부를 저장할 리스트
# dist = [[0] * width for _ in range(height)]  # 그 좌표까지 가는 최소 거리를 저장할 리스트
# dist[0][0] = 1  # 출발 지점도 거리에 포함
#
# BFS(0, 0)  # 출발지점에서 시작
# print(dist[height - 1][width - 1])  # 목표 지점에 도착하는 최소 거리


##############################################################################################################

"""2022.03.18"""
from collections import deque


def BFS(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    visit[y][x] = True
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue[0][0], queue[0][1]
        queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (
                0 <= nx < column
                and 0 <= ny < row
                and not visit[ny][nx]
                and maze[ny][nx] == "1"
            ):
                visit[ny][nx] = True
                dist[ny][nx] = dist[y][x] + 1
                queue.append([nx, ny])


row, column = map(int, input().split())
maze = [list(input().strip()) for _ in range(row)]
visit = [[False] * column for _ in range(row)]
dist = [[0] * column for _ in range(row)]
dist[0][0] = 1

BFS(0, 0)
print(dist[row - 1][column - 1])
