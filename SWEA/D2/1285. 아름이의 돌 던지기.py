"""파이썬 지원 안됨"""
test = int(input())

for t in range(test):
    num = int(input())
    number = list(map(int, input().split()))

    for i in range(len(number)):
        number[i] = abs(number[i])

    number.sort()
    cnt = number.count(number[0])

    print("#{} {} {}".format(t + 1, number[0], cnt))
