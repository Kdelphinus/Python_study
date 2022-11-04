"""1269 대칭 차집합 / 실버 III"""

import sys
from collections import Counter

input = sys.stdin.readline

len_a, len_b = map(int, input().split())
sd = len_a + len_b  # symmetric difference
a, b = list(map(int, input().split())), list(map(int, input().split()))
cnt_a, cnt_b = Counter(a), Counter(b)
for i in a:
    if i in cnt_b:
        sd -= 1
for j in b:
    if j in cnt_a:
        sd -= 1
print(sd)
