"""위클리 챌린지 10주차"""
INF = float("inf")


def intersection_point(line1, line2):
    if (line1[0] * line2[1] - line1[1] * line2[0]) == 0:
        return 0

    if (line1[1] * line2[2] - line1[2] * line2[1]) % (
        line1[0] * line2[1] - line1[1] * line2[0]
    ):
        return 0

    if (line1[2] * line2[0] - line1[0] * line2[2]) % (
        line1[0] * line2[1] - line1[1] * line2[0]
    ):
        return 0

    x = (line1[1] * line2[2] - line1[2] * line2[1]) // (
        line1[0] * line2[1] - line1[1] * line2[0]
    )
    y = (line1[2] * line2[0] - line1[0] * line2[2]) // (
        line1[0] * line2[1] - line1[1] * line2[0]
    )

    return [x, y]


def solution(line):
    answer = []
    inter_points = []
    boundary = [-INF, -INF, INF, INF]  # 위, 오른쪽, 아래, 왼쪽 / 시계 방향

    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            inter_point = intersection_point(line[i], line[j])
            if inter_point != 0 and inter_point not in inter_points:
                inter_points.append(inter_point)

                boundary[0] = max(boundary[0], inter_point[1])
                boundary[1] = max(boundary[1], inter_point[0])
                boundary[2] = min(boundary[2], inter_point[1])
                boundary[3] = min(boundary[3], inter_point[0])

    if len(inter_points) == 1:
        return ["*"]

    idx = 0
    inter_points.sort(key=lambda x: (-x[1], x[0]))
    width = boundary[1] - boundary[3] + 1
    while boundary[0] >= boundary[2] and idx < len(inter_points):
        if inter_points[idx][1] == boundary[0]:
            tmp = ""
            for i in range(boundary[3], boundary[1] + 1):
                if (
                    idx < len(inter_points)
                    and i == inter_points[idx][0]
                    and inter_points[idx][1] == boundary[0]
                ):
                    tmp += "*"
                    idx += 1
                else:
                    tmp += "."
            answer.append(tmp)
        else:
            answer.append("." * width)
        boundary[0] -= 1

    return answer


# -----------------------------------------------------------------------------------------------------

"""다른 답안"""


def solution(line):
    answer = []
    intersection = []
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            a = line[i]
            b = line[j]
            if a[0] * b[1] == a[1] * b[0]:
                continue
            if (a[1] * b[2] - a[2] * b[1]) % (a[0] * b[1] - a[1] * b[0]) or (
                a[2] * b[0] - a[0] * b[2]
            ) % (a[0] * b[1] - a[1] * b[0]):
                continue
            x = (a[1] * b[2] - a[2] * b[1]) // (a[0] * b[1] - a[1] * b[0])
            y = (a[2] * b[0] - a[0] * b[2]) // (a[0] * b[1] - a[1] * b[0])
            intersection.append([y, x])

    minx = min([p[1] for p in intersection])
    miny = min([p[0] for p in intersection])
    for i in intersection:
        i[1] -= minx
        i[0] -= miny

    maxx = max([p[1] for p in intersection])
    maxy = max([p[0] for p in intersection])

    leastSquare = [[0 for _ in range(maxx + 1)] for _ in range(maxy + 1)]
    for i in intersection:
        leastSquare[maxy - i[0]][i[1]] = 1

    for i in range(maxy + 1):
        temp = ""
        for j in range(maxx + 1):
            t = "."
            if leastSquare[i][j]:
                t = "*"
            temp += t
        answer.append(temp)

    return answer
