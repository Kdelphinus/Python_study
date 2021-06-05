test = int(input())

for t in range(test):
    n = int(input())
    test_list = [[0] * n for _ in range(n)]

    # 방향 전환
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 초기값
    mode = 0
    x, y = 0, 0
    test_list[x][y] = 1

    for num in range(2, n * n + 1):
        x += dx[mode]
        y += dy[mode]
        test_list[x][y] = num

        if not (
            0 <= x + dx[mode] < n
            and 0 <= y + dy[mode] < n
            and not test_list[x + dx[mode]][y + dy[mode]]
        ):  # 다음 인덱스 값이 범위를 벗어나거나 이미 값이 있는 경우라면
            if mode < 3:
                mode += 1
            else:
                mode = 0

    print("#{}".format(t + 1))
    for i in test_list:
        print(*i)