"""24479 알고리즘 수업 - 깊이 우선 탐색 1 / silver II"""

import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline
cnt = 1


def dfs(r: int):
    global cnt

    visited[r] = cnt
    cnt += 1
    for l in linked[r]:
        if not visited[l]:
            dfs(l)


n, m, r = map(int, input().split())
linked = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    n1, n2 = map(int, input().split())
    linked[n1].append(n2)
    linked[n2].append(n1)

for i in range(1, n + 1):
    linked[i].sort()

dfs(r)
for i in visited[1:]:
    print(i)
