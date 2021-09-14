test = int(input())

for t in range(test):
    n, m = map(int, input().split())  # n x n, 파리채 면적
    fly = [list(map(int, input().split())) for _ in range(n)]  # 파리가 앉아있는 수
    total = 0
    temp = 0

    # 가로, 세로 길이 지정
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            # 파리채 크기 설정
            for a in range(i, i + m):
                for b in range(j, j + m):
                    temp += fly[a][b]
            total = max(temp, total)
            temp = 0
    print("#{} {}".format(t + 1, total))
