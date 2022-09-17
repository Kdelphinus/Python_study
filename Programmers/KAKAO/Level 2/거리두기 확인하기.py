# """2021 카카오 채용연계형 인턴십"""
#
#
# def check(watting):
#     """check 거리두기가 잘 되어있는지 확인하는 함수
#
#     Args:
#         watting (2d-list): 현재 대기석 상태를 나타내는 리스트
#
#     Returns:
#         [int]: 거리두기가 잘 되고 있으면 1, 안되고 있으면 0을 리턴
#     """
#
#     # 사람이 위치한 곳을 저장
#     person = []
#     for i in range(5):
#         for j in range(5):
#             if watting[i][j] == "P":
#                 person.append([i, j])
#
#     # 거리두기 확인
#     for i in range(len(person) - 1):
#         for j in range(i + 1, len(person)):
#             y, x = person[i]  # 기준이 되는 사람의 좌표
#             ny, nx = person[j]  # 기준이 되는 사람과 거리두기를 했는지 확인하지 않은 사람의 좌표
#
#             if abs(ny - y) + abs(nx - x) == 2:  # 맨해튼 거리가 2일 때
#                 # 일직선 상이면 파티션이 가운데 있어야 거리두기 잘 된 것이다
#                 if x == nx and watting[min(y, ny) + 1][x] == "O":
#                     return 0
#                 elif y == ny and watting[y][min(x, nx) + 1] == "O":
#                     return 0
#
#                 # 대각선 상이면 두 개의 파티션이 있어야 거리두기가 잘 된 것이다
#                 elif watting[ny][x] == "O" or watting[y][nx] == "O":
#                     return 0
#             elif abs(ny - y) + abs(nx - x) == 1:  # 맨해튼 거리가 1이면, 즉 붙어있으면 거리두기가 안 된 것이다
#                 return 0
#
#     return 1
#
#
# def solution(places):
#     answer = []
#     for place in places:
#         watting = [list(i.strip()) for i in place]  # 주어진 상황을 2d-list로 저장한다
#         answer.append(check(watting))  # 거리두기가 잘 되었는지 확인 후, 결과에 저장
#
#     return answer
#
#
# # --------------------------------------------------------------------------------------------------------------------------------
# """BFS를 이용한 풀이"""
# from collections import deque
#
#
# def check(place, x, y):
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, 1, -1]
#     queue = deque()
#     queue.append([x, y, 0])
#     visited = set()
#     visited.add(tuple([x, y]))
#     while queue:
#         a, b, c = queue.popleft()
#         if c == 2:
#             continue
#         for i in range(4):
#             nx = a + dx[i]
#             ny = b + dy[i]
#             if nx >= 0 and nx <= len(place) - 1 and ny >= 0 and ny <= len(place[0]) - 1:
#                 if tuple([nx, ny]) not in visited:
#                     visited.add(tuple([nx, ny]))
#                     if place[nx][ny] == "P":
#                         return False
#                     if place[nx][ny] == "X":
#                         continue
#                     queue.append([nx, ny, c + 1])
#
#     return True
#
#
# def solution(places):
#     answer = []
#
#     for place in places:
#         people = []
#         for i in range(len(place)):
#             for j in range(len(place[0])):
#                 if place[i][j] == "P":
#                     people.append([i, j])
#
#         flag = True
#         for x, y in people:
#             if not check(place, x, y):
#                 flag = False
#                 break
#
#         if flag:
#             answer.append(1)
#         else:
#             answer.append(0)
#
#     return answer


#####################################################################################################
"""2022-04-12 풀이"""
from collections import deque


def check(place, x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append([y, x, 0])
    visited = []
    visited.append([y, x])

    while queue:
        ny, nx, dist = queue.popleft()
        if dist >= 2:
            continue

        for i in range(4):
            nny = ny + dy[i]
            nnx = nx + dx[i]
            if (
                0 <= nny < len(place)
                and 0 <= nnx < len(place[0])
                and [nny, nnx] not in visited
            ):
                visited.append([nny, nnx])
                if place[nny][nnx] == "P":
                    return False

                if place[nny][nnx] == "X":
                    continue

                queue.append([nny, nnx, dist + 1])

    return True


def solution(places):
    answer = []
    for place in places:
        people = []
        for i in range(len(place)):
            for j in range(len(place[0])):
                if place[i][j] == "P":
                    people.append([i, j])

        flag = True
        for y, x in people:
            if not check(place, x, y):
                flag = False
                break

        if flag:
            answer.append(1)
        else:
            answer.append(0)

    return answer


print(
    solution(
        [
            ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
            ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
            ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
            ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
        ]
    )
)
