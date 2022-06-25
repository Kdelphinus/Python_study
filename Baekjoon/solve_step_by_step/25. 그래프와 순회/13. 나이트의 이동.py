"""7562 나이트의 이동"""
import sys
from collections import deque

input = sys.stdin.readline


def BFS(n, x, y, gx, gy):
    """BFS

    Args:
        n (int): 체스판 크기, n x n
        x (int): 현재 위치의 가로 좌표
        y (int): 현재 위치의 세로 좌표
        gx (int): 목표 위치의 가로 좌표
        gy (int): 목표 위치의 세로 좌표

    Returns:
        dist[gy][gx] (int): 목표 위치까지 가는데 걸린 횟수
        -1 (int): 목표 위치까지 가지 못했을 경우 리턴
    """
    # 1시 방향부터 시계방향으로 갈 수 있는 좌표들
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]

    dist = [[0] * n for _ in range(n)]  # 현재 좌표까지 가는데 걸리는 최소 횟수가 저장된 리스트
    visit = [[0] * n for _ in range(n)]  # 현재 좌표를 탐색했는지 확인하는 리스트
    visit[y][x] = 1  # 현재 위치는 탐색 완료

    queue = deque()  # 탐색해야 할 좌표를 저장할 큐
    queue.append([x, y])  # 현재 위치 저장

    while queue:
        x, y = queue[0][0], queue[0][1]
        queue.popleft()

        if x == gx and y == gy:  # 목표 위치에 도달했다면
            return dist[gy][gx]  # 목표 위치에 도달할 때까지 걸린 횟수 리턴

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[ny][nx] == 0:  # 탐색하지 않았다면
                visit[ny][nx] = 1  # 탐색했다고 표시
                queue.append([nx, ny])  # 탐색해야 할 좌표 추가
                dist[ny][nx] = dist[y][x] + 1  # 횟수 추가
    return -1  # 목표 위치에 도달하지 못했다면


test = int(input())  # 테스트 횟수
for _ in range(test):
    n = int(input())  # 체스판 크기, n x n
    x, y = map(int, input().split())  # 현재 좌표
    gx, gy = map(int, input().split())  # 목표 좌표

    print(BFS(n, x, y, gx, gy))
