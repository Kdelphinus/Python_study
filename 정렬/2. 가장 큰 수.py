# ----------------------------------------------------------------------------------------------
"""시간 초과"""
from itertools import permutations


def solution(numbers):
    answer = ""
    numbers = [str(i) for i in numbers]
    nums = list(map("".join, permutations(numbers, len(numbers))))
    nums.sort()

    return nums[-1]
