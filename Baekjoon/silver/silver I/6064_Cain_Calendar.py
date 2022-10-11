# pypy3만 통과

import sys
from math import gcd

input = sys.stdin.readline


def lcm(a: int, b: int):
    return a * b / gcd(a, b)


def cain(m: int, n: int, x: int, y: int):
    limit = lcm(m, n)
    i, j = 0, 0
    tmpx, tmpy = x, y

    while tmpx <= limit and tmpy <= limit:
        if tmpx == tmpy:
            return tmpx
        if tmpx > tmpy:
            j += 1
        elif tmpx < tmpy:
            i += 1
        else:
            if tmpx + m > tmpy + n:
                j += 1
            else:
                i += 1
        tmpx, tmpy = x + m * i, y + n * j
    return -1


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        m, n, x, y = map(int, input().split())
        print(cain(m, n, x, y))

###################################################################################################################

"""
jys9047's code
- https://www.acmicpc.net/source/25358405
"""


def euc(x: int, y: int):
    queue = []
    while y:
        queue.append(x // y)
        x, y = y, x % y
    queue.pop()
    a, b = 0, 1
    for i in queue[::-1]:
        a, b = b, a - i * b
    return x, a, b


t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    d = x - y
    g, a, b = euc(m, n)
    if d % g:
        print(-1)
    else:
        k = x - (d // g) * a * m
        print((k - 1) % (m // g * n) + 1)

###################################################################################################################

"""
https://pacific-ocean.tistory.com/126
"""


def num(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1


t = int(input())
for i in range(t):
    m, n, x, y = map(int, input().split())
    print(num(m, n, x, y))
