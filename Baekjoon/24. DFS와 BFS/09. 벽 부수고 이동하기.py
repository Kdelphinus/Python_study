"""2206 벽 부수고 이동하기

주의 사항
- 벽을 뚫었을 때와 뚫지 않을 때를 함께 조사하면 두 개의 루트가 섞에 도착할 수 있는 것도 도착하지 못한 것으로 계산됨을 유의할 것
"""

import sys
from collections import deque

input = sys.stdin.readline


def BFS(x, y, wall):
    """BFS

    Args:
        x (int): 가로 좌표
        y (int): 세로 좌표
        wall (int): 벽을 부순 유무(0은 부수지 않음)

    Returns:
        cnt (int): 도착지점까지 가는데 걸린 거리
        -1 (int): 도착지점까지 가지 못했을 때
    """
    # 오른쪽, 왼쪽, 아래, 위
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    cnt = 1  # 움직인 횟수
    visit[y][x][0] = 1  # 벽을 뚫지 않고 탐색한 위치 표시
    visit[y][x][1] = 1  # 벽을 뚫고 탐색한 위치 표시

    queue = deque()  # 현재 좌표와 벽을 부순 유무를 저장할 큐
    queue.append([x, y, wall, cnt])  # x좌표, y좌표, 벽을 부순 유무(0은 안 부숨)

    while queue:
        x, y, wall, cnt = queue[0][0], queue[0][1], queue[0][2], queue[0][3]
        queue.popleft()

        if x == m - 1 and y == n - 1:  # 도착지점까지 탐색했다면
            return cnt  # 걸린 횟수를 리턴하고 종료

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:  # 지도 범위 안에 있고
                if wall:  # 벽을 이미 뚫었다면
                    if (
                        visit[ny][nx][1] == 0 and maze[ny][nx] == "0"
                    ):  # 탐색하지 않았으며 길이 있을 때
                        queue.append(
                            [nx, ny, wall, cnt + 1]
                        )  # 현재 좌표, 벽을 부순 유무, 지금까지 온 거리를 추가하고
                        visit[ny][nx][1] = 1  # 벽을 뚫고 탐색한 위치 표시를 하고
                else:  # 아직 벽을 뚫지 않았다면
                    if (
                        visit[ny][nx][0] == 0 and maze[ny][nx] == "0"
                    ):  # 탐색하지 않았으며 길이 있을 때
                        queue.append(
                            [nx, ny, wall, cnt + 1]
                        )  # 현재 좌표, 벽을 부순 유무, 지금까지 온 거리를 추가하고
                        visit[ny][nx][0] = 1  # 탐색 표시를 하고
                    elif (
                        visit[ny][nx][1] == 0 and maze[ny][nx] == "1" and wall == 0
                    ):  # 막혀있으나 아직 벽을 안 부셨다면
                        queue.append(
                            [nx, ny, 1, cnt + 1]
                        )  # 현재 좌표, 벽을 부숨, 지금까지 온 거리를 추가하고
                        visit[ny][nx][1] = 1  # 탐색 표시를 하고

    return -1


n, m = map(int, input().split())  # 세로, 가로
maze = [list(input().strip()) for _ in range(n)]  # 지도

# 탐색했는지 확인하는 리스트
visit = [
    [[0, 0] for _ in range(m)] for _ in range(n)
]  # [벽을 뚫지 않고 간 루트, 벽을 뚫고 간 루트]로 저장


print(BFS(0, 0, 0))
