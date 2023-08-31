import sys
from collections import deque

INPUT = sys.stdin.readline


def bfs(s):
    queue = deque([s])
    visit = [0 for _ in range(N + 1)]
    visit[s] = 1

    while queue:
        c = queue.popleft()

        for i in sorted(GRAPH[c]):
            if not visit[i]:
                visit[i] = 1
                queue.append(i)
                break

    return sum(visit), c


if __name__ == "__main__":
    N, M, K = map(int, INPUT().split())
    GRAPH = [[] for _ in range(N + 1)]
    for _ in range(M):
        start, end = map(int, input().split())
        GRAPH[start].append(end)
        GRAPH[end].append(start)
    print(*bfs(K))
