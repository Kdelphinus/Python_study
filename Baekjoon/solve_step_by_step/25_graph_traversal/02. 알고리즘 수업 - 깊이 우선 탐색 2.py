"""24480 알고리즘 수업 - 깊이 우선 탐색 2 / silver II"""

import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline
CNT = 1


def dfs(current: int):
    global CNT

    visited[current] = CNT
    CNT += 1

    for n in linked[current]:
        if not visited[n]:
            dfs(n)


n, m, r = map(int, input().split())
visited = [0] * (n + 1)
linked = [[] for _ in range(n + 1)]
for _ in range(m):
    n1, n2 = map(int, input().split())
    linked[n1].append(n2)
    linked[n2].append(n1)
for l in linked:
    l.sort(reverse=True)
dfs(r)
for i in visited[1:]:
    print(i)
