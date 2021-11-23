# 백준 24-9의 심화 버전
from collections import deque


def BFS(height, width, initial_mp):
    """BFS 초급 마법사가 숲을 탈출하는 최단 시간을 출력하는 함수

    Args:
        height (int): 숲의 높이
        width (int): 숲의 길이
        initial_mp (int): 나무를 부시고 갈 수 있는 횟수

    Returns:
        time (int): 출구에 도착했을 때 시간을 리턴
        -1 (int): 출구에 갈 방법이 없을 때 리턴
    """
    queue = deque()
    queue.append([0, 0, initial_mp, 0])  # y, x, 마법 횟수, 시간
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited[0][0] = [1] * 11  # 시작지점은 이미 방문 완료

    while queue:
        y, x, mp, time = queue.popleft()

        # 출구에 도착하면 종료
        if y == height - 1 and x == width - 1:
            return time

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < width and 0 <= ny < height:  # 숲 범위 안에 있고
                # 나무 너머를 아직 가지 않았고 나무를 뚫고 지나갈 수 있다면
                if (
                    mp > 0
                    and forest[ny][nx] == "1"
                    and 0 <= nx + dx[i] < width
                    and 0 <= ny + dy[i] < height
                    and forest[ny + dy[i]][nx + dx[i]] == "0"
                    and visited[ny + dy[i]][nx + dx[i]][mp - 1] == 0
                ):
                    # 방문을 표시하고 다음 탐색 위치로 추가
                    visited[ny + dy[i]][nx + dx[i]][mp - 1] = 1
                    queue.append([ny + dy[i], nx + dx[i], mp - 1, time + 1])

                # 나무가 없고 아직 방문하지 않았다면
                elif forest[ny][nx] == "0" and visited[ny][nx][mp] == 0:
                    # 방문을 표시하고 다음 탐색 위치로 추가
                    visited[ny][nx][mp] = 1
                    queue.append([ny, nx, mp, time + 1])

    # 모든 탐색 위치를 돌아도 출구에 도착하지 못했을 때
    return -1


height, width, mp = map(int, input().split())
forest = [input() for _ in range(height)]

# 최대 mp가 100이기에 나무를 10번까지 부실 수 있다
# visited[h][w][num]: (h, w)좌표에 num번 마법을 사용할 수 있는 상태로 방문했었는가? -> 0: 아직 방문 안 함, 1: 이미 방문함
visited = [[([0] * 11) for i in range(width)] for _ in range(height)]

print(BFS(height, width, mp // 10))
