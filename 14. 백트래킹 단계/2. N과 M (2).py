"""15650 N과 M (2)"""

"""내장 함수 이용"""
from itertools import combinations

# 1부터 n까지 숫자 중 m의 원소를 이용하여 조합을 만들 예정
n, m = map(int, input().split())

# 1 ~ n까지 m을 이용하며 만든 조합
C = combinations(range(1, n + 1), m)

# 출력
for i in C:
    print(" ".join(map(str, i)))

# ------------------------------------------------------------------------------

"""직접 구현"""


def DFS(l, num, count):
    """combinations를 구현한 함수"""
    if l == count:
        print(*result)
        return

    for i in range(num):
        if l == 0:  # 처음 값을 넣을 때
            result.append(i + 1)
            DFS(l + 1, num, count)
            result.pop()
        elif result[-1] < i + 1:  # 이전 값보다 큰 값만 들어가야 한다
            result.append(i + 1)
            DFS(l + 1, num, count)
            result.pop()


num, count = map(int, input().split())
result = []
DFS(0, num, count)