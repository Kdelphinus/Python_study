test = int(input())

for t in range(test):
    num = int(input())
    result = 1

    for n in range(2, num + 1):
        if n % 2 == 0:
            result -= n
        else:
            result += n

    print("#{} {}".format(t + 1, result))