"""15651 N과 M (3)"""

from itertools import product

# 1부터 n까지 숫자 중 m의 원소를 이용하여 조합을 만들 예정
n, m = map(int, input().split())

# 중복 순열을 만들어 출력
for i in product(range(1, n + 1), repeat=m):
    print(" ".join(map(str, i)))

# 한 줄로 쓸 때
print("\n".join(list(map(" ".join, product(map(str, range(1, n + 1)), repeat=m)))))
