"""1358 하키 / 실버 IV"""


cnt = 0
w, h, x, y, p = map(int, input().split())
r = h / 2
positions = [list(map(int, input().split())) for _ in range(p)]


def in_rink(px: int, py: int):
    if x <= px <= x + w and y <= py <= y + h:
        return 1
    if r ** 2 >= (x - px) ** 2 + (y + r - py) ** 2:
        return 1
    if r ** 2 >= (x + w - px) ** 2 + (y + r - py) ** 2:
        return 1
    return 0


for px, py in positions:
    cnt += in_rink(px, py)
print(cnt)
