"""26069 붙임성 좋은 총총이"""

import sys

INPUT = sys.stdin.readline

N, DANCING = int(INPUT()), {"ChongChong"}
for _ in range(N):
    name1, name2 = INPUT().rstrip().split()
    if name1 in DANCING:
        DANCING.add(name2)
    elif name2 in DANCING:
        DANCING.add(name1)
print(len(DANCING))
