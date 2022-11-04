"""15652 N과 M (4)"""

""" 내장 함수 이용"""
from itertools import combinations_with_replacement

# 1부터 n까지 숫자 중 m의 원소를 이용하여 조합을 만들 예정
n, m = map(int, input().split())

# 중복 조합을 만들어 출력
print(
    "\n".join(
        list(map(" ".join, combinations_with_replacement(map(str, range(1, n + 1)), m)))
    )
)

# ------------------------------------------------------------------------------

"""직접 구현"""
import sys

input = sys.stdin.readline


def DFS(l, num, count):
    if l == count:
        print(*result)
        return

    for i in range(num):
        if not result:
            result.append(i + 1)
            DFS(l + 1, num, count)
            result.pop()
        elif result[-1] <= i + 1:
            result.append(i + 1)
            DFS(l + 1, num, count)
            result.pop()


num, count = map(int, input().split())
result = []
DFS(0, num, count)