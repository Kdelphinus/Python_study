test = int(input())

for t in range(test):
    num = int(input())
    result = [0, 0, 0, 0, 0]

    while num > 1:
        if num % 2 == 0:
            result[0] += 1
            num //= 2
        elif num % 3 == 0:
            result[1] += 1
            num //= 3
        elif num % 5 == 0:
            result[2] += 1
            num //= 5
        elif num % 7 == 0:
            result[3] += 1
            num //= 7
        elif num % 11 == 0:
            result[4] += 1
            num //= 11
    print("#{}".format(t + 1), end=" ")
    print(*result)
