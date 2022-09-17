test = int(input())

for t in range(test):
    num = int(input())
    temp = []

    for _ in range(num):
        word, cnt = input().split()
        for i in range(int(cnt)):
            temp.append(word)

    print("#{}".format(t + 1))
    for i in range(len(temp)):
        print(temp[i], end="")
        if (i + 1) % 10 == 0:
            print()
    print()
