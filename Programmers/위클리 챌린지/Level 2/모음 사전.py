"""위클리 챌린지 5주차"""
from itertools import product


def my_solution(word):
    words = "AEIOU"
    dictionary = []

    for i in range(1, 6):
        dictionary += map("".join, product(words, repeat=i))
    dictionary = sorted(list(set(dictionary)))

    return dictionary.index(word) + 1


# ----------------------------------------------------------------------------------------------
"""중복 순열 안쓰고 찾기"""


def solution(word, cnt=1):
    w = {"A": "E", "E": "I", "I": "O", "O": "U", "U": 0}

    def nxt(i):
        return i[:-1] + w[i[-1]] if w[i[-1]] else nxt(i[:-1])

    i = "A"
    while i != word:
        if len(i) < 5:
            i += "A"
        elif i[-1]:
            i = nxt(i)
        cnt += 1
    return cnt


# 테스트
my_solution("AAAAE")  # 6
my_solution("AAAE")  # 10
my_solution("I")  # 1563
my_solution("EIO")  # 1189
