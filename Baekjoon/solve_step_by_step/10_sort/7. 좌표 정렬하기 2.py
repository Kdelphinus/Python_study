"""11651 좌표 정렬하기 2"""

import sys

n = int(sys.stdin.readline())

temp = []

for _ in range(n):
    temp.append(list(map(int, sys.stdin.readline().split())))

temp.sort(key=lambda x: (x[1], x[0]))

for i, j in temp:
    print(i, j)