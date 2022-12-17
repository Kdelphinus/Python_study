pyramid = [0, 1]
while True:
    n = int(input())
    if n == 0:
        break
    if n >= len(pyramid) - 1:
        for i in range(len(pyramid), n + 1):
            pyramid.append(pyramid[-1] + i)
    print(pyramid[n])
