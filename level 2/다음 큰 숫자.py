"""연습문제"""


def binary_number(n):
    cnt = 1
    while n >= 2 ** cnt:
        cnt += 1

    number = ["0"] * cnt
    number[0] = "1"

    while n > 2:
        n -= 2 ** (cnt - 1)
        cnt = 1
        while n >= 2 ** cnt:
            cnt += 1
        number[len(number) - cnt] = "1"

    return "".join(number)


def solution(n):
    cnt = str(binary_number(n)).count("1")
    m = n + 1
    bm = binary_number(m)
    while True:
        bm = binary_number(m)
        if bm.count("1") == cnt:
            return m
        m += 1


print(solution(78))
