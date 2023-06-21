test = int(input())

for t in range(test):
    num = int(input())

    if num < 10:
        print("#{} Yes".format(t + 1))
    else:
        for i in range(2, 10):
            if num % i == 0 and num // i < 10:
                print("#{} Yes".format(t + 1))
                break
            if i == 9:
                print("#{} No".format(t + 1))
