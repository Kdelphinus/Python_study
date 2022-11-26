import sys
from collections import Counter


text = sys.stdin.read().replace("\n", "").replace(" ", "")
alpha = sorted(Counter(text).most_common(), key=lambda x: (-x[1], x[0]))
cnt = -1

for a, c in alpha:
    if cnt == -1:
        print(a, end="")
        cnt = c
    elif c == cnt:
        print(a, end="")
    else:
        break
