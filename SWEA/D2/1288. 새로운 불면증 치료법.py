test = int(input())

for t in range(test):
    num = int(input())
    number = []
    value = num

    while True:
        temp = value

        while temp > 0:
            if not temp % 10 in number:
                number.append(temp % 10)
            temp //= 10

        if len(number) == 10:
            print("#{} {}".format(t + 1, value))
            break
        else:
            value += num