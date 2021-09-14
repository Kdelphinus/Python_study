"""7569 토마토(3차원)"""
import sys
from collections import deque

input = sys.stdin.readline


def BFS(m, n, h, boxes):
    """BFS

    Args:
        m (int): 박스의 가로 길이
        n (int): 박스의 세로 길이
        h (int): 쌓여있는 박스의 높이
        boxes (3d-list): 토마토가 담겨져있는 박스들

    Returns:
        days (int): 모든 토마토가 익는데 걸리는 날짜
    """
    # 오른쪽, 왼쪽, 뒤, 앞, 위, 아래
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    days = -1  # 처음 익은 것은 날짜에 포함하지 않음

    while queue:
        days += 1  # 하루가 지나고
        for _ in range(len(queue)):  # 오늘 익은 토마토들만 탐색한다
            x, y, z = queue.popleft()

            for i in range(6):  # 6방향을 확인
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]

                if (
                    0 <= nx < m
                    and 0 <= ny < n
                    and 0 <= nz < h
                    and boxes[nz][ny][nx] == 0
                ):  # 가로, 세로, 높이가 모두 박스 범위 내이고 아직 토마토가 익지 않았다면
                    boxes[nz][ny][nx] = boxes[z][y][x] + 1  # 토마토를 익은 것으로 바꾸고
                    queue.append([nx, ny, nz])  # 익은 토마토의 위치를 추가한다

    for box in boxes:
        for b in box:
            if 0 in b:  # 아직 안 익은 토마토가 있다면
                return -1
    return days


m, n, h = map(int, input().split())  # 가로, 세로, 높이
boxes = []  # 토마토가 든 박스들이 들어갈 리스트
queue = deque()  # 익은 토마토의 위치가 들어갈 큐
for z in range(h):
    box = []  # 하나의 박스
    for y in range(n):
        tmp = list(map(int, input().split()))
        for x in range(m):
            if tmp[x] == 1:
                queue.append([x, y, z])
        box.append(tmp)
    boxes.append(box)  # 박스를 차례대로 쌓는다

print(BFS(m, n, h, boxes))
