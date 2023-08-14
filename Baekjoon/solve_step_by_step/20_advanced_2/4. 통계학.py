"""2108 통계학"""
import decimal
import sys
from collections import Counter

INPUT = sys.stdin.readline


def arithmetic_mean(num: list) -> int:
    """산술 평균을 구하는 함수"""
    return round(decimal.Decimal(sum(num) / len(num)))


def median(num: list) -> int:
    """중앙값을 구하는 함수"""
    return num[len(num) // 2]


def mode(num: list) -> int:
    """최빈값을 구하는 함수"""
    count = Counter(num).most_common()  # (수, 들어있는 수의 개수)를 리턴함

    if len(num) > 1:
        if count[0][1] == count[1][1]:
            return count[1][0]
        else:
            return count[0][0]
    else:
        return count[0][0]


def reach(num: list) -> int:
    """범위를 구하는 함수"""
    return num[len(num) - 1] - num[0]


N = int(INPUT())  # 수의 개수
NUM = []  # 수를 저장할 리스트

for _ in range(N):
    temp = int(INPUT())
    NUM.append(temp)

NUM.sort()  # 정렬

print(arithmetic_mean(NUM))
print(median(NUM))
print(mode(NUM))
print(reach(NUM))
