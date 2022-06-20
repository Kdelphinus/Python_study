import sys
from collections import defaultdict

num = int(sys.stdin.readline())
cards = defaultdict(int)
for _ in range(num):
    cards[int(sys.stdin.readline())] += 1
cards = sorted(cards.items(), key=lambda x: (-x[1], x[0]))
print(cards[0][0])

# 시간 초과
# from collections import Counter
#
# num = int(input())
# cards = Counter([int(input()) for _ in range(num)])
# print(cards.most_common()[0][0])
