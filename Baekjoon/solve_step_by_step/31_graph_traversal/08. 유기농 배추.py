"""1012 유기농 배추"""
import sys

sys.setrecursionlimit(10**8)  # 재귀 제한을 늘림
input = sys.stdin.readline


def DFS(x, y):
    """DFS

    Args:
        x (int): 가로 좌표
        y (int): 세로 좌표
    """
    visit[y][x] = 1  # 탐색했다고 표시

    # 순서대로 오른쪽, 왼쪽, 아래, 위에 배추가 심겨져있고 아직 탐색하지 않은 것인지 판단하여 진행
    if x + 1 < width and cabbages[y][x + 1] == 1 and visit[y][x + 1] == 0:
        DFS(x + 1, y)
    if x - 1 >= 0 and cabbages[y][x - 1] == 1 and visit[y][x - 1] == 0:
        DFS(x - 1, y)
    if y + 1 < height and cabbages[y + 1][x] == 1 and visit[y + 1][x] == 0:
        DFS(x, y + 1)
    if y - 1 >= 0 and cabbages[y - 1][x] == 1 and visit[y - 1][x] == 0:
        DFS(x, y - 1)


test = int(input())
for t in range(test):
    anw = 0  # 필요한 배추흰지렁이를 저장할 변수
    width, height, num = map(int, input().split())  # 가로, 세로, 배추의 수
    cabbages = [[0] * width for _ in range(height)]  # 배추가 심긴 위치를 저장할 리스트
    visit = [[0] * width for _ in range(height)]  # 탐색했는지 표시할 리스트

    for _ in range(num):  # 배추가 심긴 곳을 표시한다
        x, y = map(int, input().split())
        cabbages[y][x] = 1

    for y in range(height):
        for x in range(width):
            if visit[y][x] == 0 and cabbages[y][x] == 1:  # 탐색하지 않았고 배추가 심겨져 있으면 탐색
                DFS(x, y)
                anw += 1  # 배추가 연결된 곳에 지렁이 한 마리를 추가한다

    print(anw)

# -------------------------------------------------------------------------------------------------------------------
from collections import deque


def BFS(x, y):
    field[y][x] = 0
    queue = deque()
    queue.append([x, y])
    dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < width and 0 <= ny < height and field[ny][nx] == 1:
                queue.append([nx, ny])
                field[ny][nx] = 0


test = int(input())

for t in range(test):
    width, height, num = map(int, input().split())
    field = [[0] * width for _ in range(height)]
    earthworms = 0

    for _ in range(num):
        tmp_x, tmp_y = map(int, input().split())
        field[tmp_y][tmp_x] = 1

    for h in range(height):
        for w in range(width):
            if field[h][w]:
                BFS(w, h)
                earthworms += 1

    print(earthworms)
