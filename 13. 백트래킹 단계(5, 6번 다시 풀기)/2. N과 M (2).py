"""15650 N과 M (2)"""

from itertools import combinations

# 1부터 n까지 숫자 중 m의 원소를 이용하여 조합을 만들 예정
n, m = map(int, input().split())

# 1 ~ n까지 m을 이용하며 만든 조합
C = combinations(range(1, n + 1), m)

# 출력
for i in C:
    print(" ".join(map(str, i)))