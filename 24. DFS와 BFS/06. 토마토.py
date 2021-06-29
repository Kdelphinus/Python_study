"""7576 토마토"""
import sys
from collections import deque

input = sys.stdin.readline


def BFS(m, n, box):
    # 아래, 위, 오른쪽, 왼쪽
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    days = -1  # 첫 시작은 하루로 취급하지 않기에

    while queue:  # 큐에 아무것도 없을 때까지 반복
        days += 1  # 하루가 지나고
        for _ in range(len(queue)):  # 시작할 때 익은 토마토까지만 확인(반복문 안에서 익은 토마토들은 다음 날에 확인하게 됨)
            x, y = queue.popleft()  # 큐에 들어가있는 x, y좌표를 불러옴

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if (
                    0 <= nx < m and 0 <= ny < n and box[ny][nx] == 0
                ):  # 박스 크기를 벗어나지 않고 토마토가 안 익었다면
                    box[ny][nx] = box[y][x] + 1  # 토마토가 익고
                    queue.append([nx, ny])  # 익은 토마토의 좌표를 추가

    for b in box:
        if 0 in b:  # 안 익은 토마토가 있다면
            return -1
    return days


m, n = map(int, input().split())  # 가로, 세로
tomato_box = []  # 토마토를 넣을 박스
queue = deque()


for y in range(n):
    tmp = list(map(int, input().split()))
    for x in range(m):
        if tmp[x] == 1:  # 토마토가 익은 토마토라면
            queue.append([x, y])
    tomato_box.append(tmp)

print(BFS(m, n, tomato_box))
