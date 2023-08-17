# https://velog.io/@enchantee/%EB%B0%B1%EC%A4%80-1005-Python-kvth6jbu

import sys
from collections import deque

INPUT = sys.stdin.readline


def acm_craft(goal: int) -> int:
    queue, dp = deque(), [0 for _ in range(NUM + 1)]

    # 진입 차수가 0인 것을 찾아 큐에 넣음
    for i in range(1, NUM + 1):
        if IN_DEGREE[i] == 0:
            queue.append(i)
            dp[i] = BUILD_TIME[i]

    # 진입 차수를 줄여가며 건설 비용 갱신
    while queue:
        b = queue.popleft()
        for i in GRAPH[b]:
            IN_DEGREE[i] -= 1
            dp[i] = max(dp[b] + BUILD_TIME[i], dp[i])
            if IN_DEGREE[i] == 0:
                queue.append(i)

    return dp[goal]


if __name__ == "__main__":
    T = int(INPUT())
    for _ in range(T):
        NUM, RULE_NUM = map(int, INPUT().split())
        BUILD_TIME = [0] + list(map(int, INPUT().split()))
        GRAPH = [[] for _ in range(NUM + 1)]
        IN_DEGREE = [0 for _ in range(NUM + 1)]
        for _ in range(RULE_NUM):
            B1, B2 = map(int, INPUT().split())
            GRAPH[B1].append(B2)
            IN_DEGREE[B2] += 1
        GOAL = int(INPUT())
        print(acm_craft(GOAL))
