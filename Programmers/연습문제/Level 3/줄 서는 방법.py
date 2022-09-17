"""연습문제"""
# 링크: https://velog.io/@ansrjsdn/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level3-%EC%A4%84-%EC%84%9C%EB%8A%94-%EB%B0%A9%EB%B2%95-Python

from math import factorial


def solution(n, k):
    answer = []
    number = [i for i in range(1, n + 1)]

    while n > 0:
        tmp = factorial(n - 1)
        index = k // tmp
        k %= tmp
        if k:
            answer.append(number.pop(index))
        else:
            answer.append(number.pop(index - 1))
        n -= 1

    return answer


# ------------------------------------------------------------------------------------

"""시간초과"""
from itertools import permutations


def solution(n, k):
    return list(permutations(range(1, n + 1), n))[k - 1]
