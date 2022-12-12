import math


def is_line(coors: list) -> bool:
    if coors[0] == coors[2] == coors[4] or coors[1] == coors[3] == coors[5]:
        return True
    if (
        coors[0] != coors[2]
        and coors[0] != coors[4]
        and (coors[1] - coors[3]) / (coors[0] - coors[2])
        == (coors[1] - coors[5]) / (coors[0] - coors[4])
    ):
        return True
    elif (
        coors[2] != coors[4]
        and coors[2] != coors[0]
        and (coors[3] - coors[5]) / (coors[2] - coors[4])
        == (coors[3] - coors[1]) / (coors[2] - coors[0])
    ):
        return True
    elif (
        coors[4] != coors[2]
        and coors[4] != coors[0]
        and (coors[5] - coors[1]) / (coors[4] - coors[0])
        == (coors[5] - coors[3]) / (coors[4] - coors[2])
    ):
        return True
    return False


def line_length(dot_o: list, dot_t: list) -> float:
    return math.sqrt((dot_o[0] - dot_t[0]) ** 2 + (dot_o[1] - dot_t[1]) ** 2)


def parallel(coors: list) -> float:
    if is_line(coors):
        return -1.0

    perimeter = list()
    perimeter.append(
        line_length([coors[0], coors[1]], [coors[2], coors[3]])
        + line_length([coors[0], coors[1]], [coors[4], coors[5]])
    )
    perimeter.append(
        line_length([coors[2], coors[3]], [coors[0], coors[1]])
        + line_length([coors[2], coors[3]], [coors[4], coors[5]])
    )
    perimeter.append(
        line_length([coors[4], coors[5]], [coors[2], coors[3]])
        + line_length([coors[4], coors[5]], [coors[0], coors[1]])
    )

    return max(perimeter) * 2 - min(perimeter) * 2


if __name__ == "__main__":
    coordinates = list(map(int, input().split()))
    print(f"{parallel(coordinates)}")
