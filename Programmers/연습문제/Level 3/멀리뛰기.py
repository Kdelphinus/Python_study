"""연습문제"""


def solution(n):
    mod = 1234567
    previous, current = 0, 1
    while n > 0:
        current, previous = (previous + current) % mod, current % mod
        n -= 1

    return current
