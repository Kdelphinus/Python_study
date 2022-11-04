"""14425 문자열 집합 / 실버 III"""
import sys

INPUT = sys.stdin.readline


def binary_search(tmp_list: list, start: int, end: int, target: str):
    if start > end:
        return 0

    mid = (start + end) // 2
    if tmp_list[mid] == target:
        return 1
    elif tmp_list[mid] > target:
        return binary_search(tmp_list, start, mid - 1, target)
    else:
        return binary_search(tmp_list, mid + 1, end, target)


cnt = 0
n, m = map(int, INPUT().split())
string = sorted([INPUT() for _ in range(n)])
for _ in range(m):
    tmp = INPUT()
    cnt += binary_search(string, 0, n - 1, tmp)
print(cnt)
