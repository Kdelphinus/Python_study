"""2775 부녀회장이 될테야"""
t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())  # k: floor, n: number
    value = []
    basic = list(range(1, n + 1))
    for f in range(1, k + 1):
        for h in range(1, n + 1):
            value.append(sum(basic[:h]))
        if f == k:
            print(value[n - 1])
        else:
            basic = value
            value = []
            h = 1

# --------------------------------------------------------------------

"""모범답안"""
t = int(input())
for _ in range(t):
    floor = int(input())
    num = int(input())
    f = [x for x in range(1, num + 1)]  # 0층 리스트
    for k in range(floor):
        for i in range(1, num):
            f[i] += f[i - 1]
    print((f[-1]))  # 가장 마지막 수 출력

# --------------------------------------------------------------------
