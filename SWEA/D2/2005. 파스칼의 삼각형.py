test = int(input())

for t in range(test):
    n = int(input())
    print("#{}".format(t + 1))

    # n은 1이상이므로 기본 조건
    number = [1]
    print(*number)

    if n > 1:
        # n이 2일 때
        number.append(1)
        print(*number)

        for _ in range(2, n):  # n이 3이상이면
            temp = []
            for i in range(len(number)):
                if i == 0:  # 왼쪽 끝
                    temp.append(1)
                else:
                    temp.append(number[i - 1] + number[i])
            temp.append(1)  # 오른쪽 끝
            number = temp
            print(*number)
