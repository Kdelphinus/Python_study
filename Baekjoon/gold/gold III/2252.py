import sys
from collections import deque

INPUT = sys.stdin.readline


def topological_sorting() -> bool:
    queue = deque()
    for idx, degree_list in enumerate(INDEGREE):
        if VISITED[idx] == len(degree_list) == 0:
            queue.append(idx)
            VISITED[idx] = 1

    if not queue:
        return False

    while queue:
        node = queue.popleft()
        LINE.append(node)
        for degree in OUTDEGREE[node]:
            INDEGREE[degree].remove(node)

    return True


if __name__ == "__main__":
    N, M = map(int, INPUT().split())
    VISITED = [0] * (N + 1)
    VISITED[0] = 1
    LINE = []
    INDEGREE = [[] for _ in range(N + 1)]
    OUTDEGREE = [[] for _ in range(N + 1)]
    for _ in range(M):
        FIRST, SECOND = map(int, INPUT().split())
        INDEGREE[SECOND].append(FIRST)
        OUTDEGREE[FIRST].append(SECOND)

    while topological_sorting():
        pass

    print(*LINE)
