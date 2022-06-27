"""1764 듣보잡 / 실버 IV"""

import sys
from collections import Counter

input = sys.stdin.readline

n, m = map(int, input().split())
no_hear = [input() for _ in range(n)]
cnt = Counter(no_hear)
no_hear_seen = []
for _ in range(m):
    no_seen = input()
    if no_seen in cnt:
        no_hear_seen.append(no_seen)
no_hear_seen.sort()
print(len(no_hear_seen))
print("\n".join(nhs.strip() for nhs in no_hear_seen))
