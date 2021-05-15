"""15652 N과 M (4)"""

from itertools import combinations_with_replacement

# 1부터 n까지 숫자 중 m의 원소를 이용하여 조합을 만들 예정
n, m = map(int, input().split())

# 중복 조합을 만들어 출력
print(
    "\n".join(
        list(map(" ".join, combinations_with_replacement(map(str, range(1, n + 1)), m)))
    )
)
