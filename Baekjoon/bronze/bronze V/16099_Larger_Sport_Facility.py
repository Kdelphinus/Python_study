for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 * y1 > x2 * y2:
        print("TelecomParisTech")
    elif x1 * y1 < x2 * y2:
        print("Eurecom")
    else:
        print("Tie")
