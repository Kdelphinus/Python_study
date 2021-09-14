test = int(input())

for t in range(test):
    len_1, len_2 = map(int, input().split())
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))

    max_sum = 0

    if len_1 < len_2:
        for i in range(len_2 - len_1 + 1):
            total = 0
            for j in range(len_1):
                total += list1[j] * list2[j + i]
            max_sum = max(total, max_sum)
    elif len_1 > len_2:
        for i in range(len_1 - len_2 + 1):
            total = 0
            for j in range(len_2):
                total += list1[j + i] * list2[j]
            max_sum = max(total, max_sum)
    else:
        for i in range(len_2):
            total += list1[i] * list2[i]
        max_sum = total

    print("#{} {}".format(t + 1, max_sum))
