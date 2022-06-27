"""11478 서로 다른 부분 문자열의 개수 / 실버 III"""

import sys
from collections import defaultdict

input = sys.stdin.readline
subset = defaultdict(int)
# subset = set()으로 해서 중복을 제거한 길이를 구하는게 조금 더 빠르다
string = input().strip()
for i in range(len(string)):
    for j in range(i, len(string)):
        tmp = string[i : j + 1]
        if subset[tmp] == 0:
            subset[tmp] += 1
# string = input() # readline이기 때문에 끝에 \n까지 있음, 즉 len(string)이 원래 생각보다 하나 더 김
# for i in range(len(string)):
#     for j in range(i + 1, len(string)):
#         tmp = string[i:j]
#         if subset[tmp] == 0:
#             subset[tmp] += 1
print(len(subset.keys()))
