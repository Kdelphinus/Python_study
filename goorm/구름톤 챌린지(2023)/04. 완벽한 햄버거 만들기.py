def buger(n, ele):
    if n == 1:
        return ele[0]

    flag, curv = 1, False
    for i in range(1, n):
        if ele[i] == ele[i - 1]:
            continue
        tmp = 1 if ele[i] - ele[i - 1] > 0 else -1
        if flag != tmp and curv:
            return 0
        elif flag != tmp:
            flag = -1
            curv = True
    return sum(ele)


N = int(input())
elements = list(map(int, input().split()))
print(buger(N, elements))
