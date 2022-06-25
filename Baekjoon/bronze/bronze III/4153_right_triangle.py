""" 4153 직각삼각형 """

while True:
    x, y, z = map(int, input().split())

    # 0, 0, 0이 입력되면 종료
    if x == 0 and y == 0 and z == 0:
        break

    # 세 값을 크기순으로 정렬
    side = sorted([x, y, z])

    if side[2] ** 2 == side[1] ** 2 + side[0] ** 2:
        print("right")
    else:
        print("wrong")
