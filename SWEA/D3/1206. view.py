for t in range(1, 11):
    anw = 0
    num = int(input())
    building = list(map(int, input().split()))
    for i in range(2, num - 2):
        side = max(building[i - 2], building[i - 1], building[i + 1], building[i + 2])
        if building[i] > side:
            anw += building[i] - side
    print(f"#{t} {anw}")
