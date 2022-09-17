"""위클리 챌린지"""


def solution(price, money, count):
    origin = price
    for i in range(2, count + 1):
        price += origin * i

    answer = money - price
    if answer >= 0:
        return 0

    return -answer
