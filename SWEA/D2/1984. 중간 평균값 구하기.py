test = int(input())

for t in range(test):
    num = sorted(list(map(int, input().split())))
    mean = sum(num[1:-1]) / (len(num) - 2)
    print("#{} {}".format(t + 1, round(mean)))