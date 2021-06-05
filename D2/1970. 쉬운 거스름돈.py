test = int(input())

for t in range(test):
    num = int(input())
    result = []

    result.append(num // 50000)
    num %= 50000

    result.append(num // 10000)
    num %= 10000

    result.append(num // 5000)
    num %= 5000

    result.append(num // 1000)
    num %= 1000

    result.append(num // 500)
    num %= 500

    result.append(num // 100)
    num %= 100

    result.append(num // 50)
    num %= 50

    result.append(num // 10)
    num %= 10

    print("#{}".format(t + 1))
    print(*result)