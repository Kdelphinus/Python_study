"""연습문제"""


def solution(n):
    cnt = format(n, 'b').count("1")
    m = n + 1
    while True:
        bm = format(m, 'b')
        if bm.count("1") == cnt:
            return m
        m += 1


print(solution(78))
