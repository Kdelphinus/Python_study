"""10815 숫자 카드 / 실버 V"""

import sys

INPUT = sys.stdin.readline


def binary_search(tmp_list: list, start: int, end: int, target: int):
    if start > end:
        return 0

    mid = (start + end) // 2
    if tmp_list[mid] == target:
        return 1

    if tmp_list[mid] < target:
        return binary_search(tmp_list, mid + 1, end, target)
    else:
        return binary_search(tmp_list, start, mid - 1, target)


m = int(INPUT())
cards = sorted(list(map(int, INPUT().split())))
n = int(INPUT())
check = list(map(int, INPUT().split()))
for c in check:
    print(binary_search(cards, 0, m - 1, c), end=" ")
