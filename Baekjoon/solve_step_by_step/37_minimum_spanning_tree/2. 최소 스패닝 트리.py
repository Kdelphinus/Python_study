# 해설: https://hillier.tistory.com/54

import heapq
import sys

INPUT = sys.stdin.readline


def kruskal() -> int:
    v_root = [i for i in range(V + 1)]
    graph = []
    for _ in range(E):
        graph.append(list(map(int, INPUT().split())))
    graph.sort(key=lambda x: x[2])

    def find(n: int) -> int:
        if n != v_root[n]:
            v_root[n] = find(v_root[n])
        return v_root[n]

    weight = 0
    for s, e, w in graph:
        s_root = find(s)
        e_root = find(e)
        if s_root == e_root:
            continue

        if s_root > e_root:
            v_root[s_root] = e_root
        else:
            v_root[e_root] = s_root
        weight += w

    return weight


def prim() -> int:
    visited = [False for _ in range(V + 1)]
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b, c = map(int, INPUT().split())
        graph[a].append((c, b))
        graph[b].append((c, a))

    cnt, weight = 0, 0
    heap = [[0, 1]]
    while heap:
        if cnt == V:
            return weight

        w, s = heapq.heappop(heap)
        if not visited[s]:
            visited[s] = True
            weight += w
            cnt += 1
            for i in graph[s]:
                heapq.heappush(heap, i)

    return weight


if __name__ == "__main__":
    V, E = map(int, INPUT().split())
    print(kruskal())  # 268 ms
    print(prim())  # 480 ms
