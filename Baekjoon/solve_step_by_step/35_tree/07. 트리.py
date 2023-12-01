"""4803 트리"""


import sys
from collections import deque

INPUT = sys.stdin.readline


def is_tree(start: int) -> bool:
    flag = True
    queue = deque([start])

    while queue:
        curr_node = queue.popleft()

        # 시작 노드에서 방문할 수 있는 모든 곳을 확인해야 함
        if VISITED[curr_node]:
            flag = False

        # queue에 넣을 때, VISITED를 판단하면 1 - 2 - 3 같은 구조의 트리에서 2로 시작되는 트리를 무시함
        VISITED[curr_node] = True

        for next_node in GRAPHS[curr_node]:
            if not VISITED[next_node]:
                queue.append(next_node)
    return flag


if __name__ == "__main__":
    T = 1
    while True:
        N, M = map(int, INPUT().split())
        if N == M == 0:
            break
        GRAPHS = [[] for _ in range(N + 1)]
        VISITED = [False for _ in range(N + 1)]
        for _ in range(M):
            S, E = map(int, INPUT().split())
            GRAPHS[S].append(E)
            GRAPHS[E].append(S)
        COUNT = 0
        for NODE in range(1, N + 1):
            if not VISITED[NODE] and is_tree(NODE):
                COUNT += 1
        if COUNT == 0:
            print(f"Case {T}: No trees.")
        elif COUNT == 1:
            print(f"Case {T}: There is one tree.")
        else:
            print(f"Case {T}: A forest of {COUNT} trees.")
        T += 1
