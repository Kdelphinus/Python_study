test = int(input())

for t in range(test):
    month_1, day_1, month_2, day_2 = map(int, input().split())
    list1 = [1, 3, 5, 7, 8, 10, 12]
    list2 = [4, 6, 9, 11]

    while month_1 > 1:
        month_1 -= 1

        if month_1 == 2:
            day_1 += 28
        elif month_1 in list1:
            day_1 += 31
        else:
            day_1 += 30

    while month_2 > 1:
        month_2 -= 1

        if month_2 == 2:
            day_2 += 28
        elif month_2 in list1:
            day_2 += 31
        else:
            day_2 += 30

    print("#{} {}".format(t + 1, day_2 - day_1 + 1))
