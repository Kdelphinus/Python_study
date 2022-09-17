"""위클리 챌린지 8주차"""


def solution(sizes):
    height = 0
    width = 0

    for size in sizes:
        size.sort()
        width = max(width, size[0])
        height = max(height, size[1])

    return width * height
