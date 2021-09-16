"""월간 코드 챌린지 시즌 3"""


def move(dr, dc, dd, row, column):
    # direction = [up, rigth, down, left] 인덱스 순서대로
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
    if spot == "L":
        dd -= 1
        if dd < 0:
            dd = 3
    elif spot == "R":
        dd += 1
        if dd > 3:
            dd = 0
    return dd


def solution(grid):
    answer = []
    row = len(grid)
    column = len(grid[0])
    visited = [[[False] * 4 for i in range(column)] for _ in range(row)]

    direction = ["U", "R", "D", "L"]
    for r in range(row):
        for c in range(column):
            for d in range(4):
                if not visited[r][c][d]:
                    dr, dc, dd = r, c, d
                    cnt = 0
                    while not visited[dr][dc][dd]:
                        visited[dr][dc][dd] = True
                        dr, dc = move(dr, dc, dd, row, column)
                        dd = rotate(dd, grid[dr][dc])
                        cnt += 1
                    answer.append(cnt)
    return answer
