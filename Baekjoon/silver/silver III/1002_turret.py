""" 1002 터렛 """

from math import sqrt

# 테스트 수
test = int(input())
cnt = 0

while cnt != test:
    # 좌표와 거리
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    # 두 원의 위치 관계
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif abs(r1 - r2) < sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) < r1 + r2:
        print(2)
    elif (
        abs(r1 - r2) == sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        or sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) == r1 + r2
    ):
        print(1)
    else:
        print(0)

    # 테스트 횟수
    cnt += 1
