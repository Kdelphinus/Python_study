"""10250 ACM호텔"""
T = int(input())  # T: test num
a = 0
for t in range(T):
    H, W, N = map(int, input().split())  # H: floor num, W: room num, N: cutomer
    for i in range(1, W + 1):
        if a == N:
            a = 0
            break
        for j in range(1, H + 1):
            a += 1
            if a == N:
                f = str(j) + str(i).zfill(2)
                print(f)
                break

# --------------------------------------------------------------------

"""모범답안"""
t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    f = 0
    ho = 0
    if n % h == 0:
        f = h * 100
        ho = n // h
    else:
        f = (n % h) * 100
        ho = 1 + n // h
    print(f + ho)
# 등차일 때 나머지를 사용하면 간단해짐
