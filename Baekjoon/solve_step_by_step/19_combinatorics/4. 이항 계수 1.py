"""11050 이항 계수 1"""


def factorial(num):
    if num <= 1:
        return 1

    value = 1
    for i in range(2, num + 1):
        value *= i

    return value


def bino(num, k):
    return int(factorial(num) / (factorial(k) * factorial(num - k)))


NUM, K = map(int, input().split())  # 이항계수 (NUM, K)가 주어짐
print(bino(NUM, K))
