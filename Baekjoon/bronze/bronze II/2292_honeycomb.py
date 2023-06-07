"""2292 벌집"""

N = int(input())
start = 2
end = 2
if N == 1:
    print(1)
else:
    for i in range(N):
        start += 6 * i
        end += 6 * (i + 1)
        if N in range(start, end):
            print(i + 2)  # i가 0부터 시작하므로
