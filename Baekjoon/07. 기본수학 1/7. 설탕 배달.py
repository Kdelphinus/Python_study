"""2839 설탕 배달"""
N = int(input())
n1 = [4, 7]
n2 = [6, 9, 12]
if N in n1:
    print(-1)
elif N in n2:
    print(N // 3)
elif N % 5 == 0:
    print(N // 5)
elif (N % 5) % 3 == 0:
    print(N // 5 + (N % 5) // 3)
else:
    for i in range(1, N // 3):
        if (N - 3 * i) % 5 == 0:
            print(i + (N - 3 * i) // 5)

# --------------------------------------------------------------------

"""모범 답안"""
N = int(input())
Box = 0
while True:
    if (N % 5) == 0:
        Box += N // 5
        print(Box)
        break
    N -= 3
    Box += 1
    if N < 0:
        print(-1)
        break
