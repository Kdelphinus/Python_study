"""연습문제"""


def solution(n):
    mod = 1234567
    idx = 1
    past = 0
    current = 1

    while idx < n:
        tmp = current
        current = (current + past) % mod
        past = tmp % mod
        idx += 1

    return current % mod
