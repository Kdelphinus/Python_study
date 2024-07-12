# 풀이: https://hongcoding.tistory.com/94
# DFS로 접근하였으나 예외가 많아 실패 -> 위상 정렬 방법으로 풀어야 함

import sys
import heapq

INPUT = sys.stdin.readline


def topological_sorting():
    heap, ans = [], []

    # 선수 문제가 없는 문제를 heap에 삽입
    for i in range(1, N + 1):
        if DEGREE[i] == 0:
            heapq.heappush(heap, i)

    # 선수문제 유무를 확인하면서 문제 해결
    while heap:
        tmp = heapq.heappop(heap)
        ans.append(tmp)
        for i in GRAPH[tmp]:
            DEGREE[i] -= 1
            if DEGREE[i] == 0:
                heapq.heappush(heap, i)
    return ans


if __name__ == "__main__":
    N, M = map(int, INPUT().split())
    GRAPH = [list() for _ in range(N + 1)]
    DEGREE = [0] * (N + 1)
    for _ in range(M):
        pre_quest, quest = map(int, INPUT().split())
        GRAPH[pre_quest].append(quest)
        DEGREE[quest] += 1
    print(*topological_sorting())
