test = int(input())

for t in range(test):
    time = list(map(int, input().split()))
    minute = time[1] + time[3]
    hour = time[0] + time[2]

    if minute >= 60:
        minute -= 60
        hour += 1
    if hour > 12:
        hour -= 12

    print("#{} {} {}".format(t + 1, hour, minute))