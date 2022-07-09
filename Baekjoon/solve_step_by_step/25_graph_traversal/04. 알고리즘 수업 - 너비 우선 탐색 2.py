"""24445 알고리즘 수업 - 너비 우선 탐색 2 / silver II"""

import sys
from collections import deque

INPUT = sys.stdin.readline


def bfs(r: int, n: int, linked: list):
    cnt = 1
    visited = [0] * (n + 1)

    queue = deque()
    queue.append(r)
    while queue:
        curr = queue.popleft()
        visited[curr] = cnt
        cnt += 1
        for l in linked[curr]:
            if not visited[l]:
                visited[l] = 1
                queue.append(l)

    for v in visited[1:]:
        print(v)


def main():
    n, m, r = map(int, INPUT().split())
    linked = [[] for _ in range(n + 1)]
    for _ in range(m):
        n1, n2 = map(int, INPUT().split())
        linked[n1].append(n2)
        linked[n2].append(n1)
    for l in linked:
        l.sort(reverse=True)
    bfs(r, n, linked)


if __name__ == "__main__":
    main()
