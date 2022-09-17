test = int(input())

for t in range(test):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    list_90 = []
    list_180 = []
    list_270 = []

    for i in range(n):  # 90도 회전
        temp = []
        for j in range(n - 1, -1, -1):
            temp.append(arr[j][i])
        list_90.append(temp)

    for i in range(n):  # 180도 회전
        temp = []
        for j in range(n - 1, -1, -1):
            temp.append(list_90[j][i])
        list_180.append(temp)

    for i in range(n):  # 270도 회전
        temp = []
        for j in range(n - 1, -1, -1):
            temp.append(list_180[j][i])
        list_270.append(temp)

    print("#{}".format(t + 1))

    for i_90, i_180, i_270 in zip(list_90, list_180, list_270):
        for i in i_90:
            print(i, end="")
        print(" ", end="")

        for i in i_180:
            print(i, end="")
        print(" ", end="")

        for i in i_270:
            print(i, end="")
        print()
