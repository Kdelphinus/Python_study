"""위클리 챌린지 10주차"""
INF = float("inf")


def intersection_point(line1, line2):
    """intersection_point 두 직선의 교점을 찾는 함수

    <equation>
    Ax + By + E = 0
    Cx + Dy + F = 0

    x = (BF - ED) / (AD - BC)
    y = (EC - AF) / (AD - BC)

    if AD - BC == 0: 평행 or 일치

    Args:
        line1 (list): ax + by + c = 0에서 [a, b, c]가 저장된 리스트
        line2 (list): ax + by + c = 0에서 [a, b, c]가 저장된 리스트

    Returns:
        [x, y] (list): 교점의 좌표
        0 (int): 교점이 없거나 무수히 많은 경우
    """
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
    answer = []  # 출력할 문자열들을 저장할 리스트
    inter_points = []  # 교점을 저장할 리스트
    boundary = [-INF, -INF, INF, INF]  # 위, 오른쪽, 아래, 왼쪽

    # 교점 찾기
    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            inter_point = intersection_point(line[i], line[j])

            # 아직 저장하지 않은 교점이 있을 때
            if inter_point != 0 and inter_point not in inter_points:
                inter_points.append(inter_point)  # 교점 추가

                # 교점들의 경계 최신화
                boundary[0] = max(boundary[0], inter_point[1])  # 위
                boundary[1] = max(boundary[1], inter_point[0])  # 오른쪽
                boundary[2] = min(boundary[2], inter_point[1])  # 왼쪽
                boundary[3] = min(boundary[3], inter_point[0])  # 아래

    # 교점이 한 개일 때
    if len(inter_points) == 1:
        return ["*"]

    idx = 0  # inter_points의 인덱스
    inter_points.sort(key=lambda x: (-x[1], x[0]))  # y좌표 내림차순, x좌표 오름차순
    width = boundary[1] - boundary[3] + 1  # 가로 길이
    while boundary[0] >= boundary[2] and idx < len(inter_points):
        # 현재 y좌표에 교점이 있을 때
        if inter_points[idx][1] == boundary[0]:
            tmp = ""
            for i in range(boundary[3], boundary[1] + 1):
                # 교점이 있는 위치라면
                if (
                    idx < len(inter_points)
                    and i == inter_points[idx][0]
                    and inter_points[idx][1] == boundary[0]
                ):
                    tmp += "*"
                    idx += 1  # 다음 교점 확인

                # 교점이 없는 위치라면
                else:
                    tmp += "."
            answer.append(tmp)

        # 교점이 없는 위치라면
        else:
            answer.append("." * width)
        boundary[0] -= 1  # y좌표를 하나 낮춘다

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
