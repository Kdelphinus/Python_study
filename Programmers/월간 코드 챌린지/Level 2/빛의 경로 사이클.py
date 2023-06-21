"""월간 코드 챌린지 시즌 3"""


def move(dr, dc, dd, row, column):
    """빛이 가야할 다음 위치를 알려주는 함수

    Args:
        dr (int): 현재 row
        dc (int): 현재 column
        dd (int): 현재 방향
        row (int): grid의 row 개수
        column (int): grid의 column 개수

    Returns:
        dr, dc (int): 이동한 위치의 row와 column
    """
    if dd == 3:  # 왼쪽으로 갈 때
        dc -= 1
        if dc < 0:
            dc = column - 1
    elif dd == 1:  # 오른쪽으로 갈 때
        dc += 1
        if dc >= column:
            dc = 0
    elif dd == 0:  # 위로 갈 때
        dr -= 1
        if dr < 0:
            dr = row - 1
    elif dd == 2:  # 아래로 갈 때
        dr += 1
        if dr >= row:
            dr = 0
    return dr, dc


def rotate(dd, spot):
    """방향을 회전하는 함수

    Args:
        dd (int): 현재 방향
        spot (str): 이동한 곳에 저장된 방향

    Returns:
        dd (int): 바뀐 방향
    """
    if spot == "L":  # 방향을 왼쪽으로 바꿔야 한다면
        dd -= 1  # 반시계 방향으로 한 칸 이동
        if dd < 0:
            dd = 3
    elif spot == "R":  # 방향을 오른쪽으로 바꿔야 한다면
        dd += 1  # 시계 방향으로 한 칸 이동
        if dd > 3:
            dd = 0
    return dd


def solution(grid):
    answer = []
    row = len(grid)
    column = len(grid[0])

    # 방향도 확인해야 하기에 하나의 위치 당 4개로 나눔
    # 0: 위, 1: 오른쪽, 2: 아래, 3: 왼쪽 (시계방향)
    visited = [[[False] * 4 for i in range(column)] for _ in range(row)]

    for r in range(row):
        for c in range(column):
            for d in range(4):
                if not visited[r][c][d]:  # 아직 방문하지 않은 곳일 때
                    dr, dc, dd = r, c, d
                    cnt = 0
                    while not visited[dr][dc][dd]:  # 방문한 곳이 나오기 전까지 계속 확인
                        visited[dr][dc][dd] = True  # 방문했다고 표시
                        dr, dc = move(dr, dc, dd, row, column)  # 다음 칸으로 이동
                        dd = rotate(dd, grid[dr][dc])  # 다음 칸의 방향에 따라 방햔 변경
                        cnt += 1  # 이동한 횟수 추가
                    answer.append(cnt)  # 이동이 끝나면 루트의 길이 추가
    return sorted(answer)


# -------------------------------------------------------------------------------------------------
"""DFS를 이용한 풀이"""
import sys

sys.setrecursionlimit(10**6)


def out(x, y, d, grid, dic):
    nx = x + dic[d][0]
    ny = y + dic[d][1]

    if nx >= len(grid):
        nx = 0
    elif nx < 0:
        nx = len(grid) - 1

    if ny >= len(grid[0]):
        ny = 0
    elif ny < 0:
        ny = len(grid[0]) - 1

    return nx, ny


def dfs(state, org, route, grid):
    dic = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}
    x = state[0]
    y = state[1]
    d = state[2]
    visited[d][x][y] = 1

    nx, ny = out(x, y, d, grid, dic)
    value = grid[nx][ny]

    if value == "R":
        d = (d + 5) % 4

    elif value == "L":
        d = (d + 7) % 4

    if org[0] == nx and org[1] == ny and org[2] == d:
        answer.append(route)
        return

    if not visited[d][nx][ny]:
        dfs([nx, ny, d], org, route + 1, grid)


def solution(grid):
    global answer, visited

    answer = []
    visited = [[[0] * len(grid[0]) for _ in range(len(grid))] for _ in range(4)]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for d in range(4):
                dfs([i, j, d], [i, j, d], 1, grid)

    return sorted(answer)
