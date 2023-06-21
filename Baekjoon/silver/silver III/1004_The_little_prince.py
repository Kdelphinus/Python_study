"""1004 어린 왕자 / 실버 III"""


def check_circle(planet: list, position: list):
    """
    position이 planet 안에 있는지 확인하는 함수
    Args:
        planet: [중심 좌표 x, 중심 좌표 y, 반지름]
        position: [현재 좌표 x, 현재 좌표 y]

    Returns:
        안에 있으면 1, 없으면 0
    """
    cx, cy, r = planet
    x, y = position

    if r**2 > (cx - x) ** 2 + (cy - y) ** 2:
        return 1
    return 0


def space(start: list, end: list):
    n = int(input())
    cnt = 0
    planets = [list(map(int, input().split())) for _ in range(n)]
    for planet in planets:
        if check_circle(planet, start) + check_circle(planet, end) == 1:
            cnt += 1
    return cnt


t = int(input())
for _ in range(t):
    tmp = list(map(int, input().split()))
    print(space(tmp[:2], tmp[2:]))
