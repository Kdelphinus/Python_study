"""Summer/Winter Coding(~2018)"""


def solution(dirs):
    position = [0, 0]  # 시작 위치
    route = set()  # 지나갔던 길들을 저장할 집합

    # 움직일 수 있는 좌표는 최대 -5 ~ 5
    # 양방향을 모두 저장해야 한다
    for d in dirs:
        x, y = position[0], position[1]
        if d == "U" and position[1] < 5:  # 위로 갔을 때
            route.add((x, y, x, y + 1))
            route.add((x, y + 1, x, y))
            position[1] += 1
        elif d == "L" and position[0] > -5:  # 왼쪽으로 갔을 때
            route.add((x, y, x - 1, y))
            route.add((x - 1, y, x, y))
            position[0] -= 1
        elif d == "R" and position[0] < 5:  # 오른쪽으로 갔을 때
            route.add((x, y, x + 1, y))
            route.add((x + 1, y, x, y))
            position[0] += 1
        elif d == "D" and position[1] > -5:  # 아래로 갔을 때
            route.add((x, y, x, y - 1))
            route.add((x, y - 1, x, y))
            position[1] -= 1

    return len(route) / 2  # 양방향을 저장했기에 절반을 리턴한다


print(solution("ULURRDLLU"))  # 7
print(solution("LULLLLLLU"))  # 7

# ------------------------------------------------------------------------------------

"""같은 원리, 간단한 구현"""


def solution(dirs):
    s = set()
    d = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x, y, nx, ny))
            s.add((nx, ny, x, y))
            x, y = nx, ny
    return len(s) // 2
